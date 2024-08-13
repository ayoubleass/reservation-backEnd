from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship




class Role(BaseModel, Base):
    #roles = ["travler", "host", "Admin"]
    __tablename__ = "roles"
    name = Column(String(60), nullable=False)
    allowed_fields = ["name", "id"]
    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)    