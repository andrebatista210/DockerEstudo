from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import psycopg2

conn = psycopg2.connect(database="desafio",
                        user='postgres', password='123456',
                        host='localhost', port='5433'
                        )
cursor = conn.cursor()

app = Flask(__name__)

@app.route('/dados', methods=['GET'])
def obter_todos():
    sql3 = '''SELECT json_agg(country) FROM public.country;'''
    cursor.execute(sql3)
    dados = cursor.fetchall()
    return jsonify (dados)

@app.route('/dados/<id>', methods=['GET'])
def obter_dados(id):
    sql3 = '''select json_agg(x) from (
select a.tablename,a.region, a.incomegroup,b.*   from public.country a
inner join public.mktp_trat b on a."Country Code" = b."Country Code"
) as x where (UPPER(x."Country Code") = UPPER('%s') or UPPER(x.tablename) = UPPER('%s')) ;''' %(id,id)
    cursor.execute(sql3)
    dados = cursor.fetchall()
    return (dados)

@app.route('/pib/<id>', methods=['GET'])
def obter_pib(id):
    sql3 = '''select json_agg(x) from (
select a.region, b.*   from public.country a
inner join public.mktp_trat b on a."Country Code" = b."Country Code"
) as x where x.region = '%s';''' %(id)
    cursor.execute(sql3)
    dados = cursor.fetchall()
    return (dados)

@app.route('/perc/<id>', methods=['GET'])
def obter_perc(id):
    sql3 = '''select json_agg(x)  from (
                select b.tablename,
                    a.*,
                    case when  
                            lag(a.valor_pib,1)over(order by a."Country Code", ano) is null 
                            or a.valor_pib is null 
                            or lag(a.valor_pib,1)over(order by a."Country Code", ano) = 0 
                            or a.valor_pib = 0
                            then 0
                        else 100*(lag(a.valor_pib,1)over(order by a."Country Code", ano) - a.valor_pib)/lag(a.valor_pib,1)over(order by a."Country Code", ano)
                    end perc_crescimento_anual
                    from public.mktp_trat a
                    inner join public.country b on a."Country Code" = b."Country Code"
                    where (UPPER(a."Country Code") = UPPER('%s') or UPPER(b.tablename) = UPPER('%s'))
                    ) as x;''' %(id,id)
    cursor.execute(sql3)
    dados = cursor.fetchall()
    return (dados)



@app.route('/rank/<ano_inicio>/<ano_fim>', methods=['GET'])
def obter_rank(ano_inicio, ano_fim):
    if not ano_inicio.isdigit() or not ano_fim.isdigit() :
        return 'ano digitado não é um numerico'
    else:
        sql_rank = '''
        select 
            RANK, "Country Name", "Country Code", "Indicator Name", "Indicator Code",media as "AVG" 
        from (
                select 
                    - row_number()over(order by x.media asc) as rank,	
                    *
                from (
                    SELECT 
                        "Country Name", "Country Code", "Indicator Name", "Indicator Code", avg(valor_pib) as media
                    FROM public.mktp_trat A
                    WHERE valor_pib is not null
                    and ano between %s and %s
                    group by "Country Name", "Country Code", "Indicator Name", "Indicator Code"
            ) as x
            limit 10
        ) k
        UNION ALL 
        select 
        RANK, "Country Name", "Country Code", "Indicator Name", "Indicator Code",media as "AVG" 
            from (
                select 
                    row_number()over(order by x.media desc) as RANK,	
                    *
                from (
                    SELECT 
                        "Country Name", "Country Code", "Indicator Name", "Indicator Code", avg(valor_pib) as media
                    FROM public.mktp_trat A
                    WHERE valor_pib is not null
                    and ano between %s and %s
                    group by "Country Name", "Country Code", "Indicator Name", "Indicator Code"
                    
                ) as x
            limit 10
        ) z;''' %(ano_inicio,ano_fim,ano_inicio, ano_fim)
        cursor.execute(sql_rank)
        dados = cursor.fetchall()
        return (dados)
if __name__ == '__main__':
    app.run(debug=True)