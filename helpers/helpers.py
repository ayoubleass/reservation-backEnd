from models import storage
from models.user import User
from models.role import Role
from models.image import Image
from werkzeug.utils import secure_filename

import os


classes = {"User" : User, "Role" : Role}
current_dir = os.getcwd()
ROOT_DIR = os.getcwd()
UPLOAD_FOLDER =  os.path.join(current_dir, 'storage')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def unique(cls, key, value):
    if not value:
        return False
    for user in storage.all(cls).values():
        if user.get(key) == value:
            return False
    return True




def required(cls, fields):
    error_message = {}
    obj = classes.get(cls)
    if obj is None:
        raise ValueError(f"Class {cls} not found")

    valid_attributes = obj.__table__.columns.keys() 
                       
    for key, value in fields:
        if not value and key in valid_attributes:
            message[key] = "{} is required".format(key)
    return error_message

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_images(request,  id ,storage_path=None):
    for file_key in request.files:
        file = request.files[file_key]
        if file and allowed_file(file.filename):
            if storage_path is None:
                storage_path = UPLOAD_FOLDER
            filename = os.path.join(storage_path, file.filename)
            file.save(filename)
            image = Image(url=filename, place_id=id) 
            storage.new(image).save()
        else: 
            return '{}  need to have the follwing extension {}'.format(file.filename,
                                                                                ALLOWED_EXTENSIONS)
    return True
        
    



            
            
        
        



