from .utils import *
from ..routers.users import get_db, get_current_user
from fastapi import status


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get("/user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()[0]['username'] == 'shalwinastest1'
    assert response.json()[0]['email'] == 'shalwinastest1@gmail.com'
    assert response.json()[0]['first_name'] == 'shalwin'
    assert response.json()[0]['last_name'] == 'a s'
    assert response.json()[0]['role'] == 'admin'
    assert response.json()[0]['phone_number'] == '1234567891'

def test_change_password_success(test_user):
    response = client.put('/user/change_password', json= {'password':'testpassword','new_password':'newpassword'})
    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_change_password_invalid_current_password(test_user):
    response = client.put('/user/change_password', json= {'password':'wrongpassword','new_password':'newpassword'})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Error on password change'}

def test_change_phone_number_success(test_user):
    response = client.put("/user/update_phone_number/8887776666")
    assert response.status_code == status.HTTP_204_NO_CONTENT