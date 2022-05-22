#!/bin/bash
#Author: Hernandez Lopez Raul @Neo
#e-mail:  freeenergy1974@gmail.com
#date: friday,   february 4,  2022
#is placed in the directory where the environment should be 
#found

cd ../Back/Python_WS/


if [ -d "environment" ]; then 
    printf "\nThe environment already exists and is configured\n"
    source environment/bin/activate
else	
    """Creation and configuration of the python environment"""	
    printf "\nConfiguring python environment...\n"		
    python -m venv environment

    source environment/bin/activate
   
    pip install peewee
    pip install uvicorn 
    pip install fastapi
    pip install PyMySQL
    pip install pydantic
fi    
