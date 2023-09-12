from app.utils.auth_utils import get_hashed_password, verify_password, password_conxt




def test_get_hashed_password_and_verify_func():
    password = '12345678'
    # verify the hash 
    hash = get_hashed_password(password=password)
    hash_2 = password_conxt.hash(password)
    assert hash != hash_2
    assert type(hash) == type('str')

    # check if the pswd is verified 
    verfy = verify_password(password, hash)
    assert  verfy == True






