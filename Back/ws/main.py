#author: Hernandez  Lopez Raul  @Neo
#email:     freeenergy1975@gmail.com
#date:Miercoles 19 de enero del 2022

from fastapi import FastAPI
from conexion import User
from conexion import SatisfactionSurvey
from conexion import Surveys
from esquema import UserBaseModel
from esquema import SurveysBaseModel
from esquema import SatisfactionSurveyBaseModel
from conexion import database as conexion


app = FastAPI(title = 'Conexion',
                description = 'Establece una conexion a la base de datos de mariadb',
                version = '1')

#Creates an event to establish the connection to the database before the server starts.
@app.on_event('startup')
def startup():
    if conexion.is_closed():
        conexion.connect()
        conexion.create_tables([User, SatisfactionSurvey, Surveys])
        print('Conexion exitosa')

#Creates an event to close the connection to the database before the server shuts down.
@app.on_event('shutdown')
def shutdown():
    if not conexion.is_closed():
        conexion.close()
        print('Apagando...');

#Allows multiple requests to be executed and resolved asynchronously. 
@app.get('/')
async def index():
    return 'Hola Mundo :D'

#Specifies a path to create users in the database for the users table, not without
#verifying that the data entered are of the requested type.
@app.post('/user/')
async def create_user(user: UserBaseModel):
    user = User.create(
            id_user = user.id_user,
            type_of_user = user.type_of_user,
            name_of_user = user.name_of_user,
            password = user.password,
            status = user.status
            )
    return user.id_user
#Creates a record for the survey table
@app.post('/survey/')
async def create_survey(survey: SurveysBaseModel):
    survey = Surveys.create(
        id_survey = survey.id_survey,
        name_survey = survey.name_survey
        )

    return survey.id_survey

#Test version, unstable
@app.post('/satisfaction_system/')
async def create_satisfaction_survey(satisfaction_system: SatisfactionSurveyBaseModel):
            satisfaction_survey = SatisfactionSurvey.create(
                    id_satisfaction_survey = SatisfactionSurvey.id_satisfaction_survey,
                    survey = SatisfactionSurvey.survey,
                    user = SatisfactionSurvey.user,
                    date_and_time = SatisfactionSurvey.date_and_time,
                    level_of_satisfaction = SatisfactionSurvey.level_of_satisfaction,
                    coment = SatisfactionSurvey.coment,
                    folio_ticket = SatisfactionSurvey.folio_ticket
                    )



