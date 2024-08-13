from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship



class Country(BaseModel, Base):
    __tablename__ = "countries"
    name = Column(String(255), nullable=False)
    region = Column(String(255),nullable=False)
    cities = relationship("City", cascade="all, delete-orphan")
    allowed_fields = ["name", "region", "id"]
    
    
    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)