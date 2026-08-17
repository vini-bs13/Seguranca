import redis
from flask import Flask

app = Flask(__name__)
db = redis.Redis(host='redis' ,port=6379)

def incrementa_contador():
    try:
        return db.incr('contador')
    except redis.exceptions.ConectionError:
        return -1

@app.route('/')
def inicial():
    contador = incrementa_contador()
    return f'Valor do contador: {contador}.\n'