import psycopg2
import pandas as pd

conn = psycopg2.connect(database="desafio",
                        user='postgres', password='123456',
                        host='localhost', port='5433'
                        )

conn.autocommit = True
cursor = conn.cursor()

sql = '''create table MKTP(
    "Country Name"          varchar(1000) null,
    "Country Code"          varchar(1000) null,
    "Indicator Name"        varchar(1000) null,
    "Indicator Code"        varchar(1000) null,
    "1960" NUMERIC null,
    "1961" NUMERIC null,
	"1962" NUMERIC null,
    "1963" NUMERIC null,
    "1964" NUMERIC null,
    "1965" NUMERIC null,
    "1966" NUMERIC null,
    "1967" NUMERIC null,
    "1968" NUMERIC null,
    "1969" NUMERIC null,
    "1970" NUMERIC null,
    "1971" NUMERIC null,
    "1972" NUMERIC null,
    "1973" NUMERIC null,
    "1974" NUMERIC null,
    "1975" NUMERIC null,
    "1976" NUMERIC null,
    "1977" NUMERIC null,
    "1978" NUMERIC null,
    "1979" NUMERIC null,
    "1980" NUMERIC null,
    "1981" NUMERIC null,
    "1982" NUMERIC null,
    "1983" NUMERIC null,
    "1984" NUMERIC null,
    "1985" NUMERIC null,
    "1986" NUMERIC null,
    "1987" NUMERIC null,
    "1988" NUMERIC null,
    "1989" NUMERIC null,
    "1990" NUMERIC null,
    "1991" NUMERIC null,
    "1992" NUMERIC null,
    "1993" NUMERIC null,
    "1994" NUMERIC null,
    "1995" NUMERIC null,
    "1996" NUMERIC null,
    "1997" NUMERIC null,
    "1998" NUMERIC null,
    "1999" NUMERIC null,
    "2000" NUMERIC null,
    "2001" NUMERIC null,
    "2002" NUMERIC null,
    "2003" NUMERIC null,
    "2004" NUMERIC null,
    "2005" NUMERIC null,
    "2006" NUMERIC null,
    "2007" NUMERIC null,
    "2008" NUMERIC null,
    "2009" NUMERIC null,
    "2010" NUMERIC null,
    "2011" NUMERIC null,
    "2012" NUMERIC null,
    "2013" NUMERIC null,
    "2014" NUMERIC null,
    "2015" NUMERIC null,
    "2016" NUMERIC null,
    "2017" NUMERIC null,
    "2018" NUMERIC null,
    "2019" NUMERIC null,
    "2020" NUMERIC null,
    "2021" NUMERIC null
);'''

#cursor.execute(sql)

sql_country = '''CREATE TABLE COUNTRY(
"Country Code" 	varchar(100) null,
region			varchar(1000) null,
incomeGroup		varchar(1000) null,
specialNotes	varchar(8000) null,
tableName		varchar(1000) null
);'''
#cursor.execute(sql_country)

sql_INDICADORES = '''CREATE TABLE INDICADOR(
	"INDICATOR_CODE" VARCHAR(100)
	,"INDICATOR_NAME" VARCHAR(200)
	,"SOURCE_NOTE" VARCHAR(8000)
	,"SOURCE_ORGANIZATION" VARCHAR(1000)
);'''
#cursor.execute(sql_INDICADORES)

sql_country = '''CREATE TABLE COUNTRY(
"Country Code" 	varchar(100) null,
region			varchar(1000) null,
incomeGroup		varchar(1000) null,
specialNotes	varchar(8000) null,
tableName		varchar(1000) null
);'''
#cursor.execute(sql_country)

sql_MKTP_TRAT = '''CREATE TABLE MKTP_TRAT(
	ID SERIAL,
	"Country Name"          varchar(1000) null,
    "Country Code"          varchar(1000) null,
    "Indicator Name"        varchar(1000) null,
    "Indicator Code"        varchar(1000) null,
	ANO NUMERIC,
	VALOR_PIB NUMERIC
);'''
#cursor.execute(sql_MKTP_TRAT)


sql2t = '''truncate table MKTP;'''
cursor.execute(sql2t)

sql2 = '''COPY MKTP("Country Name","Country Code","Indicator Name","Indicator Code","1960","1961","1962","1963","1964","1965","1966","1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021")
FROM 'D:/Arquivos/new_API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_4770541.csv'
DELIMITER ';'
CSV HEADER;'''

cursor.execute(sql2)

sql3tr = '''truncate table MKTP_TRAT;'''
cursor.execute(sql3tr)

slq_MKTP_TRAT = '''INSERT INTO MKTP_TRAT("Country Name", "Country Code", "Indicator Name", "Indicator Code", ANO, VALOR_PIB) 
SELECT "Country Name", "Country Code", "Indicator Name", "Indicator Code", 
	CAST(unnest(array['1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021'])AS INTEGER) AS ANO,
	unnest(array["1960", "1961", "1962", "1963", "1964", "1965", "1966", "1967", "1968", "1969", "1970", "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978", "1979", "1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]) AS VALOR_PIB
	FROM public.mktp;'''
cursor.execute(slq_MKTP_TRAT)

sql3t = '''truncate table COUNTRY;'''
cursor.execute(sql3t)

sql3 = '''COPY COUNTRY("Country Code","region","incomegroup","specialnotes","tablename")
FROM 'D:/Arquivos/new_Metadata_Country_API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_4770541.csv'
DELIMITER ';'
CSV HEADER;'''

cursor.execute(sql3)

sql4t = '''truncate table INDICADOR;'''
cursor.execute(sql4t)


sql4 = '''COPY INDICADOR("INDICATOR_CODE","INDICATOR_NAME","SOURCE_NOTE","SOURCE_ORGANIZATION")
FROM 'D:/Arquivos/new_Metadata_Indicator_API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_4770541.csv'
DELIMITER ';'
CSV HEADER;'''

cursor.execute(sql4)


sql3 = '''select * from MKTP;'''
cursor.execute(sql3)
for i in cursor.fetchall():
    print(i)

conn.commit()
conn.close()