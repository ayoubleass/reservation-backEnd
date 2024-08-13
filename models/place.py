from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Table, Boolean
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id', onupdate='CASCADE',
                                        ondelete='CASCADE'),
                             primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id', onupdate='CASCADE',
                                        ondelete='CASCADE'),
                             primary_key=True))


place_reservation = Table(
    'place_reservation', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
    Column('reservation_id', String(60), ForeignKey('reservations.id'), primary_key=True)
)

class Place(BaseModel, Base):
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    address = Column(String(255), nullable=False)
    category_id = Column(String(255), ForeignKey('categories.id'))
    is_valid    = Column(Boolean, nullable=True)
    images = relationship("Image", backref="place", cascade="all, delete-orphan")
    amenities = relationship("Amenity", secondary="place_amenity",
                             backref="places",
                             viewonly=False)
    reservations = relationship(
        "Reservation",
        secondary=place_reservation,
        back_populates="places"
    )
    allowed_fields = ["name", "description", "user_id", 
                      "city_id", "number_rooms" , "number_bathrooms",
                      "max_guest" , "price_by_night" , "id", "category_id" , "address"]
    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)