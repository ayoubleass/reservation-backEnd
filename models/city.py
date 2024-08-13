from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship



class City(BaseModel, Base):
    __tablename__ = "cities"
    name = Column(String(255), nullable=False)
    country_id = Column(String(60), ForeignKey('countries.id'), nullable=False)
    places = relationship("Place", backref="cities")
    country = relationship("Country", back_populates="cities")
    
    allowed_fields = ["id", "name", "country_id", "updated_at", "created_at", "country"]
    
    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)