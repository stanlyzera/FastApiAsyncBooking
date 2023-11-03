import pytest
from httpx import AsyncClient


@pytest.mark.parametrize('email, password, status_code', [
    ('papa@mail.ru', 'papa123', 200),
    ('papa@mail.ru', 'papa1223', 409),
    ('papamail.ru', 'papa1223', 422)
])
async def test_register_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post('/auth/register', json={
        "email": email,
        "password": password
    })

    assert response.status_code == status_code


@pytest.mark.parametrize('email, password, status_code', [
    ('test@test.com', 'test', 200),
    ('artem@example.com', 'artem', 200),
    ('wrong@example.com', 'artem', 401)
])
async def test_login_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post('/auth/login', json={
        "email": email,
        "password": password
    })

    assert response.status_code == status_code
