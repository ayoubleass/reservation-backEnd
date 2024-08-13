from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship



user_role = Table(
        "user_role",
        Base.metadata,
        Column('user_id', String(60),ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'),
                                            primary_key=True),
        Column('role_id', String(60),
                                 ForeignKey('roles.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True));

class User(BaseModel, Base):
    __tablename__ = 'users'
    email = Column(String(255), nullable=False, unique=True)
    first_name =  Column(String(255),nullable=False)
    last_name = Column(String(255),nullable=False)
    password = Column(String(255), nullable=False)
    phone_number = Column(String(255), nullable=False)
    reservations = relationship("Reservation", back_populates="user")
    roles = relationship('Role', secondary=user_role,  backref="user_role", viewonly=False)
    places = relationship("Place", backref="user")
    allowed_fields = ["email", "first_name", "last_name", 
                      "phone_number", "id", "created_at", "updated_at"]
    
    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

        
    
        

