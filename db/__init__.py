"""
Skylog backend - db/__init__.py
Database module
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database connection string
DATABASE_URL = "sqlite:///./skylog.db"  # Example for SQLite, change as needed

