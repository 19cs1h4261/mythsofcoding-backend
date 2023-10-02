from sqlalchemy import Column,Integer,Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ContentsList(Base):
    __tablename__ = 'contents_data'
    id = Column(Integer, primary_key = True, index= True, autoincrement=True)
    language_content = Column(Text)
    language = Column(Text)


class Contents(Base):
    __tablename__ = 'python_page_contents'
    id = Column(Integer, primary_key = True, index= True, autoincrement=True)
    page_topics = Column(Text)
    page_contents = Column(Text)
    language_content = Column(Text)

