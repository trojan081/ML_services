from fastapi import FastAPI
import pandas as pd


app = FastAPI()

# _____________________________ Шаг 0. Общие функции _____________________________

# http://127.0.0.1:8000/
@app.get('/')
def root():
    return {'message': 'Сервер работает, всё ок'}


@app.get('/health')
def health():
    return {'status': 'ok'}


# http://127.0.0.1:8000/hello/Artem
@app.get('/hello/{name}')
def hello(name: str, scream: bool = False):
    message = f'Привет, {name}'
    if scream == True:
        message += '!!!!!!!!!!'
    return {'msg': message}


# Документация Swagger
# http://127.0.0.1:8000/docs


@app.get('/square/{number}')
def square(number: int):
    return {'value': number, 'result': number ** 2}




# _____________________________ Шаг 1. Кастомные данные _____________________________



custom_data = [
    {
        'id': 1,
        'student': 'Alex',
        'course': 1,
        'math': 5,
        'computer_science': 4,
        'physics': 5
    },
    {
        'id': 2,
        'student': 'Maria',
        'course': 1,
        'math': 5,
        'computer_science': 5,
        'physics': 5
    },
    {
        'id': 3,
        'student': 'Anna',
        'course': 2,
        'math': 3,
        'computer_science': 4,
        'physics': 3
    },
    {
        'id': 4,
        'student': 'Oleg',
        'course': 2,
        'math': 3,
        'computer_science': 4,
        'physics': 3
    },
    {
        'id': 5,
        'student': 'Daria',
        'course': 1,
        'math': 4,
        'computer_science': 3,
        'physics': 4
    }
]


# http://127.0.0.1:8000/load_data
@app.get('/load_data')
def get_students():
    return custom_data


# http://127.0.0.1:8000/ и т.д.
@app.get('/stats')
def get_stats():
    df = pd.DataFrame(custom_data)
    stats =  {
        'lenght': len(custom_data),
        'average_grade': df[['math', 'computer_science', 'physics']].mean()
    }
    return stats

# http://127.0.0.1:8000/students
@app.post('/students', status_code=201)
def create_student(body: dict):
    record = {
        'id': len(custom_data) + 1,
        'student': body.get('student'),
        'course': body.get('course'),
        'math': body.get('math'),
        'computer_science': body.get('computer_science'),
        'physics': body.get('physics')
    }
    custom_data.append(record)
    return {'created': record}

# 'student': name,
# 'course': course,
# 'math': math,
# 'computer_science': computer_science,
# 'physics': physics


# # Ищем студента по айди
# def find_student(student_id: int):
#     for record in custom_data:
#         if record['id'] == student_id:
#             return record


# http://127.0.0.1:8000/students
@app.delete('/students/{student_id}')
def delete_student(student_id: int):
    for record in custom_data:
        if record['id'] == student_id:
            custom_data.remove(record)

    return {'message': 'deleted'}


@app.put('/students/{student_id}')
def update_student(student_id: int, body: dict):
    for record in custom_data:
        if record['id'] == student_id:
            updated_record = {
            'id': student_id,
            'student': body['student'],
            'course': body['course'],
            'math': body['math'],
            'computer_science': body['computer_science'],
            'physics': body['physics']
            }

            custom_data[student_id] = updated_record


            return {'msg': 'updated'}