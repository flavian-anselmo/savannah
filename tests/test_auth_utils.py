from app.utils.auth_utils import get_hashed_password, verify_password, password_conxt

def test_get_hashed_password_and_verify_func():
    password = '12345678'

    hash_1 = get_hashed_password(password=password)
    hash_2 = password_conxt.hash(password)
    assert hash_1 != hash_2
    assert type(hash_1) == type('str')

    verfy_1 = verify_password(password, hash_1)
    verfy_2 = verify_password(password, hash_2)
    assert verfy_1 == (True,  None)
    assert verfy_2 == (True, None)





