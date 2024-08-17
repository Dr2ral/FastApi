from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def Main_Page():
    return 'Главная страница'

@app.get('/user/admin')
async def Admin_Page():
    return 'Вы вошли как администратор'

@app.get('/user/{user_id}')
async def User_number(user_id):
    return f'Вы вошли как пользователь №{user_id}'

@app.get('/user')
async def User_Info(username: str, age: int):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'

