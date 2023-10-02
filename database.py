from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import pandas as pd
from models import ContentsList, Base,Contents


# creating database
engine = create_engine(f"sqlite:///test_db.db", echo=True)
# conn = engine.connect()
Base.metadata.create_all(bind=engine)

Sessionlocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

session = Sessionlocal()


def insert_contents_list(contents_list: list):
    for content in contents_list:
        language_content, language = content
        insert_check = (
            session.query(ContentsList)
            .filter(ContentsList.language_content == language_content)
            .filter(ContentsList.language == language)
            .first()
        )
        if not insert_check:
            insert_data = ContentsList(
                language_content=language_content,
                language=language,
            )
            session.add(insert_data)
    session.commit()

def insert_contents(page_contents_list: list):
    for content in page_contents_list:
        page_topics, page_contents,language_content = content
        insert_page_check = (
            session.query(Contents)
            .filter(Contents.page_topics == page_topics)
            .filter(Contents.language_content == language_content)
            .first()
        )
        if not insert_page_check:
            insert_page_data = Contents(
                page_topics = page_topics,
                page_contents = page_contents,
                language_content=language_content
            )
            session.add(insert_page_data)
    session.commit()