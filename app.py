from fastapi import FastAPI,HTTPException
import pandas as pd
from database import Sessionlocal,insert_contents_list,insert_contents
from fastapi.middleware.cors import CORSMiddleware
from models import ContentsList,Contents
import json
from utils.config import CONTENTS_LIST,CONTENTS_PAGE

app = FastAPI()

origins = ['http://localhost:3000','http://localhost:3001','http://192.168.1.4:3000']

#add middileware
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


session = Sessionlocal()
def get_db():
    session = Sessionlocal()
    try: 
      yield session
    finally:
      session.close()

@app.post('/getContentsList/')
def get_contents(selected_language : dict):
  selected_language = selected_language.get('language')
  insert_contents_list(CONTENTS_LIST)
  data = session.query(ContentsList).filter(ContentsList.language== selected_language.lower()).all()
  return data


@app.post('/getContents/')
def get_contents(selected_content : dict):
  selected_content = selected_content.get('language_content')
  insert_contents(CONTENTS_PAGE)
  data = session.query(Contents).filter(Contents.language_content== selected_content).all()
  return data

