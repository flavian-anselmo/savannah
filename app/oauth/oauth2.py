from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from app.config.config import settings
from fastapi.security import OAuth2PasswordBearer
from app.schema import schema
from app.models import models
from app.database.database import get_db
from sqlalchemy.orm import session



ooauth2_schema = OAuth2PasswordBearer(tokenUrl = 'auth/sign-in')

SECRET_KEY:str =  settings.secret_key
ALGORITHM:str = settings.algorithm
ACCESS_TOKEN_EXPIRATION_TIME:int =  1440 


def create_access_token (payload:dict):
    to_encode_payload = payload.copy()
    expire_time = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_EXPIRATION_TIME)
    print(expire_time)
    to_encode_payload.update({'exp':expire_time})
    encoded_jwt = jwt.encode(to_encode_payload, SECRET_KEY, ALGORITHM)
    return encoded_jwt 


def verify_access_token(token:str, credential_exceptions):
    try:
        payload:dict = jwt.decode(token, SECRET_KEY, ALGORITHM)
        customer_id:int = payload.get('customer_id')
        exp_date:datetime = payload.get("exp")
        if datetime.fromtimestamp(exp_date) < datetime.now():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token Expired', headers={"WWW-Authenticate": "Bearer"})
        if customer_id is None:
            raise credential_exceptions
        token_data = schema.TokenPayLoad(customer_id = customer_id)   
        return token_data
    except JWTError:
        raise credential_exceptions    



def get_current_user_logged_in(db:session = Depends(get_db), access_token:str = Depends(ooauth2_schema)):
    credential_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Not authenticated",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token = verify_access_token(token = access_token, credential_exceptions = credential_exception)
    user = db.query(models.Customers).filter(models.Customers.customer_id  == token.customer_id).first()
    return user
