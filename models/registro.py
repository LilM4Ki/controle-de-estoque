from flask_login import UserMixin
from peewee import AutoField, BooleanField, CharField, Model

from models.produtos import mysql_db


class Usuarios(UserMixin, Model):
    id = AutoField()
    username = CharField(max_length= 150)
    senha = CharField(max_length=255)
    
    class Meta:
        database = mysql_db
    