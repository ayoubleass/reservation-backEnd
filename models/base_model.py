"""
"""
from sqlalchemy.orm import declarative_base
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from models import credentials
import uuid
TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
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
                self.updated_at = datetime.strptime(kwargs["updated_at"], TIME_FORMAT)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], TIME_FORMAT)

    def to_dict(self):
        """Convert instance into dict format"""
        new_dict = self.__dict__.copy()

        if '_sa_instance_state' in new_dict:
            del new_dict['_sa_instance_state']

        # Safe conversion for dates
        if hasattr(self, 'created_at') and self.created_at is not None:
            new_dict["created_at"] = self.created_at.strftime(TIME_FORMAT)
        else:
            new_dict["created_at"] = datetime.utcnow().strftime(TIME_FORMAT)
            
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            new_dict["updated_at"] = self.updated_at.strftime(TIME_FORMAT)
        else:
            new_dict["updated_at"] = datetime.utcnow().strftime(TIME_FORMAT)
            
        new_dict["__class__"] = self.__class__.__name__
        return new_dict 
    

    def get(self, key):
        return getattr(self, key)
