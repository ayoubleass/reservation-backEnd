from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Table, Date
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates
from models.place import place_reservation



class Reservation(BaseModel, Base):
    __tablename__ = "reservations"
    arrival_date = Column(Date, nullable=False)
    depart_date = Column(Date, nullable=False)
    user_id  = Column(String(60), ForeignKey('users.id'), nullable=False)
    places = relationship(
        "Place",
        secondary="place_reservation",
        back_populates="reservations"
    )
    user = relationship("User", back_populates="reservations") 
    
    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
    
    @validates('depart_date')
    def validate_depart_date(self, key, depart_date):
        if self.arrival_date and depart_date <= self.arrival_date:
            raise ValueError("Departure date must be after arrival date")
        return depart_date