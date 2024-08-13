"""
"""
from sqlalchemy.orm import declarative_base
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from models import credentials
import uuid

Base = declarative_base()

class BaseModel():
    """"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    allowed_fields = []
    
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
            if  kwargs.get("created_at", None) is None:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) is None:
                self.updated_at = datetime.utcnow()      
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
    
    def to_dict(self):
        time = "%Y-%m-%dT%H:%M:%S.%f"
        new_dict = self.__dict__.copy()
        new_dict = {key: value for key, value in new_dict.items() 
                    if key in self.allowed_fields}
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict
    

    def get(self, key):
        return getattr(self, key)
        

   


