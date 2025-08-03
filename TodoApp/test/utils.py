import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.pool.impl import StaticPool
from sqlalchemy.sql.expression import text
from ..database import Base
from fastapi.testclient import TestClient
from ..main import app
from ..models import Todos, Users
from ..routers.auth import bcrypt_context

SQLALCHEMY_DATABASE_URL = "sqlite:///./testdb.db"  #--testing database
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args= {"check_same_thread": False},
    poolclass = StaticPool
)

TestingSessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base.metadata.create_all(bind= engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def override_get_current_user():
    return {"username":"shalwinas", "id":1, "user_role": "Admin"}

client = TestClient(app)

@pytest.fixture
def test_todos():
    todo = Todos(
        title = "Learn to code!",
        description = "Need to learn everyday!",
        priority = 1,
        complete = False,
        owner_id = 1,
    )
    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo #--- run until the endof our function
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))
        connection.commit()


@pytest.fixture
def test_user():
    db = TestingSessionLocal()
    db.query(Users).delete()
    db.commit()
    user = Users(
        username= 'shalwinastest1',
        email= 'shalwinastest1@gmail.com',
        first_name= 'shalwin',
        last_name= 'a s',
        hashed_password= bcrypt_context.hash('testpassword'),
        role= 'admin',
        phone_number= 1234567891
    )
    db.add(user)
    db.commit()
    yield user
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM users;"))