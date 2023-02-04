import psycopg2
import redis
import json
from bottle import Bottle, request

# pode colocar o nome do serviço no host
#DNS = 'dbname=email_sender user=postgres password=postgres host=db'


class Sender(Bottle):
    def __init__(self):
        super().__init__()
        self.route('/', method='POST', callback=self.send)
        self.fila = redis.StrictRedis(host='queue', port=6379, db=0)
        DNS = 'dbname=email_sender user=postgres host=db'
        self.conn = psycopg2.connect(DNS)

    def register_message(self, assunto, mensagem):
        SQL = 'INSERT INTO emails(assunto,mensagem) VALUES (%s,%s)'
        #conn = psycopg2.connect(DNS)
        cur = self.conn.cursor()
        cur.execute(SQL, (assunto, mensagem))
        self.conn.commit()
        cur.close()
        # self.conn.close()

        msg = {'assunto': assunto, 'mensagem': mensagem}
        self.fila.rpush('sender', json.dumps(msg))

        print('Mensagem registrada com sucesso !')

    # @route('/', method='POST')
    def send(self):
        assunto = request.forms.get('assunto')
        mensagem = request.forms.get('mensagem')

        self.register_message(assunto, mensagem)

        return 'mensagem enfileirada! Assunto {} Mensagem: {}'.format(assunto, mensagem)


if __name__ == '__main__':
    sender = Sender()
    sender.run(host='0.0.0.0', port=8080, debug=True)
