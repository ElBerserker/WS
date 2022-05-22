#author: Hernandez  Lopez Raul  @Neo
#email:     freeenergy1975@gmail.com
#date:Miercoles 19 de enero del 2022
from peewee import *
from datetime import datetime


#establishes the credentials for accessing the database
database = MySQLDatabase('Prueba', 
                        user='Berserker_db', 
                        password='Concorde1975#',
                        host='192.168.1.84',
                        port=3306)

#These templates create the database tables.
class User(Model):
    id_user = CharField(max_length = 30, unique = True, primary_key = True)
    type_of_user = CharField(max_length = 30)
    name_of_user = CharField(max_length = 30, unique = True)
    password = CharField(max_length = 30)
    status = CharField(max_length = 10)

    def __str__(self):
        return self.id_user

    class Meta:
        database = database
        table_name = 'users'

class Surveys(Model):
    id_survey = AutoField()
    name_survey = CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.id_survey

    class Meta:
        database = database
        table_name = 'surveys'

class SatisfactionSurvey(Model):
    id_satisfaction_survey = CharField(max_length = 30, unique = True, primary_key = True)
    survey = ForeignKeyField(Surveys, backref = 'level_of_satisfaction')
    user = ForeignKeyField(User, backref= 'level_of_satisfaction')
    date_and_time = DateTimeField(default = datetime.now)
    level_of_satisfaction = SmallIntegerField()
    coment = CharField(max_length = 120)
    folio_ticket = CharField(max_length = 30, unique = True)

    def __str__(self):
        return f'{self.user.id_user} - {self.id_satisfaction_survey}'

    class Meta:
        database = database
        table_name = 'satisfaction_survey'

