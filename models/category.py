from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship



class Category(BaseModel, Base):
    
    __tablename__ = "categories"
    name = Column(String(255))
    places = relationship("Place", backref="category")
    icon = Column(String(255))
    allowed_fields = ["name", "id", "updated_at", "created_at" , 'icon']
    
    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
        
        



