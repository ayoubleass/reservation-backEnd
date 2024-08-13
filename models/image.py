from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship



class Image(BaseModel, Base):
    __tablename__ = "images"
    url = Column(String(255))
    place_id = Column(String(60), ForeignKey('places.id'))
    allowed_fields = ['url', 'place_id' , 'id', 'created_at', 'updated_at']
    
    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)