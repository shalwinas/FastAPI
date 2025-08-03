from .utils import override_get_db, override_get_current_user, TestingSessionLocal, client, test_todos
from ..main import app
from ..routers.todos import get_db, get_current_user
from fastapi import status
from ..models import Todos


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_read_all_authenticated(test_todos):
    response = client.get("/todos/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{"complete": False, 'title':'Learn to code!',
                                'description':'Need to learn everyday!','id':1,
                                'priority':1, 'owner_id':1}]

def test_read_one_authenticated(test_todos):
    response = client.get("/todos/todo/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"complete": False, 'title':'Learn to code!',
                                'description':'Need to learn everyday!','id':1,
                                'priority':1, 'owner_id':1}

def test_read_one_authenticated_not_found():
    response = client.get("/todos/todo/999")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Todo not found'}

def test_create_todo(test_todos):
    request_data = {
        'title': "New todo!",
        'description': 'New todo description',
        'priority': 5,
        'complete': False
    }
    response = client.post('/todos/todo/', json=request_data)
    assert response.status_code == 201
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 2).first()
    assert model.description == request_data.get('description')
    assert model.priority == request_data.get('priority')
    assert model.complete == request_data.get('complete')

def test_update_todo(test_todos):
    request_data = {
        'title': 'Change the title of the todo already saved!',
        'description':'Need to learn everyday!',
        'priority': 5,
        'complete':False,
    }
    response = client.put('/todos/todo/1', json= request_data)
    assert response.status_code == 204
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model.title == 'Change the title of the todo already saved!'

def test_update_todo_not_found(test_todos):
    request_data = {
        'title': 'Change the title of the todo already saved!',
        'description':'Need to learn everyday!',
        'priority': 5,
        'complete':False,
    }
    response = client.put('/todos/todo/999', json= request_data)
    assert response.status_code == 404
    assert response.json() == {'detail':'Todo not found'}

def test_delete_todo(test_todos):
    response = client.delete('/todos/todo/1')
    assert response.status_code == 204
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model is None

def test_delete_todo_not_found():
    response = client.delete('/todos/todo/999')
    assert response.status_code == 404
    assert response.json() == {'detail': 'Todo not found'}