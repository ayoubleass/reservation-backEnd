"""This module"""


from models import credentials
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.role import Role
from models.amenity import Amenity
from models.place import Place
from models.country import Country
from models.city import City
from models.category import Category
from models.image import Image
from models.reservation import Reservation

classes = {"User" : User, "Role" : Role, 
           "Amenity" :Amenity , "Place" : Place, "City" : City,
           "Country" : Country, "Category" : Category, "Image" : Image,
           "Rservation" : Reservation }

class DB_Storage:
    __engine = None
    __session = None
    
    def __init__(self):
        db_credtite = credentials.config_credentials["db"];
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(db_credtite["user"],
                                            db_credtite["pwd"],
                                            db_credtite["host"],
                                            db_credtite["name"]))
                                
    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session
       

    def new(self, obj):
        self.__session.add(obj)
        return self
       
    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)
    
    def merge(self, obj):
        self.__session.merge(obj)
        return self


    def save(self):
        """Commit all changes of the current database session.
        try:
            self.__session.commit()
        except Exception as e:
            self.__session.rollback()  
        finally:
            self.__session.close()"""
        self.__session.commit()
        
        
    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    
    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for class_name , class_type in classes.items():
            if cls is None or cls is class_type or cls is class_name:
                objects = self.__session.query(class_type).all()
                for obj in objects:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict
    
    
    def get(self, cls, id):
        """Retrive an object using the id or none if not found"""
        objs = list(self.all(cls).values())
        for obj in objs:
            if obj.id == id:
                return obj
        return None       
    
    def getSession(self):
        return self.__session;   
            
       
