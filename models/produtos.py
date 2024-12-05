import os

from dotenv import load_dotenv
from peewee import CharField, FloatField, IntegerField, Model, MySQLDatabase

load_dotenv()

MYSQL_USER=os.getenv('MYSQL_USER')
MYSQL_PASSWORD=os.getenv('MYSQL_PASSWORD')
MYSQL_DB=os.getenv('MYSQL_DB')
MYSQL_HOST=os.getenv('MYSQL_HOST')

mysql_db = MySQLDatabase(MYSQL_DB, user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOST, port=3306)

class Produtos(Model):
    id = IntegerField(primary_key=True)
    nome = CharField(max_length=100)
    descricao = CharField(max_length=200)
    preco = FloatField()
    quantidade = IntegerField()
    class Meta:
        database = mysql_db
        