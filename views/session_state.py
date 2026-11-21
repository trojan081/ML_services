import streamlit as st
import pandas as pd


st.title('Состояние сессии (st.session_state)')
st.subheader('Шаг 1. Наивный счетчик')

count = 0
if st.button('Прибавить к переменной'):
    count += 1
st.metric('count', count)


st.subheader('Шаг 2. Счетчик с session_state')


if 'clicks' not in st.session_state:
    st.session_state.clicks = 0
    # st.session_state['clicks'] = 0

st.metric('st.session_state.clicks', st.session_state.clicks)

if st.button('Прибавить к clicks'):
    st.session_state.clicks += 1
st.metric('clicks', st.session_state.clicks)





st.subheader('Шаг 3. Текстовый ввод + key')

st.text_input('Ваше имя', 'noname', key='name')
st.write(f'Привет, {st.session_state.name}!')





st.subheader('Шаг 4. Корзина пользователя')
st.caption('Добавьте нужные блюда в корзину')

menu = {
    'Борщ': 350,
    'Оливье': 450,
    'Салат': 200,
    'Компот': 120
}

if 'cart' not in st.session_state:
    st.session_state.cart = []

# st.session_state.setdefault('cart', list())

dish = st.multiselect('Блюдо', list(menu))
if st.button('Добавить в корзину'):
    for d in dish:
        st.session_state.cart.append(d)

total = 0
for item in st.session_state['cart']:
    total += menu[item]

st.write('В корзине', st.session_state.cart)
st.metric('Сумма', total)



st.subheader('Шаг 5. Сброс состояния')

def clear_cart():
    del st.session_state.cart


def reset_all():
    st.session_state.clear()


col1, col2 = st.columns(2)
with col1:
    st.button('Очистить корзину', on_click=clear_cart)
with col2:
    st.button('Очистить session_state', on_click=reset_all)


st.subheader('Шаг 6. Callback')

if 'number' not in st.session_state:
    st.session_state.number = 0
if 'previous_number' not in st.session_state:
    st.session_state.previous_number = st.session_state.number


def math_operation(amount, operation='add'):
    st.session_state.previous_number = st.session_state.number
    if operation == 'add':
        st.session_state.number += amount
    elif operation == 'subtract':
        st.session_state.number -= amount


number = st.number_input('Введите число', on_change='rerun')

col1, col2 = st.columns(2)
with col1:
    st.button(f'+ {number}', on_click=math_operation, args=(number,))
with col2:
    st.button(
        f'- {number}', 
        on_click=math_operation,
        kwargs={
            'amount': number, 
            'operation': 'subtract'
                }
        )

st.metric(
    'Результат',
    st.session_state.number,
    delta=st.session_state.number - st.session_state.previous_number,
    delta_color='normal'
)

text = st.text_input('Введите число', live=True)
st.write(text)


st.write(st.session_state)

