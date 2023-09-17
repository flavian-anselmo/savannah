from passlib.context import CryptContext


password_conxt = CryptContext(schemes=['bcrypt'])

def  get_hashed_password(password:str):
    '''
    takes plain password and returns the hashed version 
    
    '''
    hash = password_conxt.hash(password)
    return hash

def verify_password(password:str, hashed_password:str):
    '''
    confirms if the hash and the pswd match 
    
    '''
    return password_conxt.verify_and_update(password, hashed_password) 