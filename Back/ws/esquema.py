#author: Hernandez  Lopez Raul  @Neo
#email:     freeenergy1975@gmail.com
#date:Miercoles 19 de enero del 2022


from pydantic import BaseModel

#Models for evaluating input data types
class UserBaseModel(BaseModel):
    id_user: str
    type_of_user: str
    name_of_user: str
    password: str
    status: str


class SurveysBaseModel(BaseModel):
    name_survey: str


class SatisfactionSurveyBaseModel(BaseModel):
    id_satisfaction_survey: str
    level_of_satisfaction: int
    coment: str
    folio_ticket: str

