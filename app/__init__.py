# app/__init__.py

from .main import app

from .database import engine, Base
Base.metadata.create_all(bind=engine)

from . import models, crud, image_processor, tasks
