import streamlit as st
import pandas as pd
import requests
import json


# _____________________________ Шаг 0. Настройка _____________________________


API_URL='http://127.0.0.1:8000'


# _____________________________ Шаг 1. Данные _____________________________


st.title('Главная страница')

# http://127.0.0.1:8000/load_data
def get_data():
    response = requests.get(f'{API_URL}/load_data')
    return response.json()


def get_stats():
    response = requests.get(f'{API_URL}/stats')
    return response.json()


if 'show_data' not in st.session_state:
    st.session_state['show_data'] = False


def show_data():
    st.session_state['show_data'] = True


def hide_data():
    st.session_state['show_data'] = False


col1, col2 = st.columns(2)
with col1:
    st.button(
        label='Показать данные',
        on_click=show_data,
        width='stretch'
    )

with col2:
    st.button(
        label='Скрыть данные',
        on_click=hide_data,
        width='stretch'
    )

if st.session_state.get('show_data', False):
    data = pd.DataFrame(get_data())
    st.dataframe(data)



if st.button(label='Отобразить статистику'):
    data = get_stats()
    st.dataframe(data)


# _____________________________ Шаг 2. CRUD-операции _____________________________

with st.expander('CRUD - операции'):

    records = get_data()
    record_by_id = {r['id']: r for r in records}
    students_ids = list(record_by_id.keys())

    tab_create, tab_delete, tab_put = st.tabs(
        ['Создать', 'Удалить', 'Обновление записи']
    )
    with tab_create:
        with st.form('Добавить запись (CREATE)'):

            name = st.text_input('Имя')
            course = st.number_input('Курс', 1, 4, 1)
            math = st.number_input('Математика', 2, 5, 4)
            computer_science = st.number_input('Программирование', 2, 5, 4)
            physics = st.number_input('Физика', 2, 5, 4)

            if st.form_submit_button('POST'):
                data = {
                        'student': name,
                        'course': course,
                        'math': math,
                        'computer_science': computer_science,
                        'physics': physics
                        }

                r = requests.post(f'{API_URL}/students',
                            json=data
                            )
                
                st.write(r.status_code)

                if not r.status_code == 201:
                    st.error(r.json)
    with tab_delete:
        with st.form('Удалить запись (DELETE)'):
            target = st.selectbox(
                'Запись для удаления',
                students_ids
            )

            if st.form_submit_button('DELETE'):
                r = requests.delete(
                f'{API_URL}/students/{target}'
            )

                st.write(r.status_code)

    with tab_put:
        with st.form('Обновить запись (PUT)'):
            id = st.selectbox(
                'Запись для обновления',
                students_ids
            )

            record = record_by_id[id]
            
            name = st.text_input('Имя', record['student'])
            course = st.number_input('Курс', 1, 4, record['course'])
            math = st.number_input('Математика', 2, 5, record['math'])
            computer_science = st.number_input('Программирование', 2, 5, record['computer_science'])
            physics = st.number_input('Физика', 2, 5, record['physics'])

            if st.form_submit_button('PUT'):

                data = {
                        'student': name,
                        'course': course,
                        'math': math,
                        'computer_science': computer_science,
                        'physics': physics
                        }

                r = requests.put(
                    f'{API_URL}/students/{id}',
                    json=data
                )
