import pandas as pd
import streamlit as st
from datetime import datetime
import time


FILE = r'data\walmart-product-with-embeddings-dataset-usa.csv'


st.title('Основы кэша')
st.markdown('Датасет [Walmart + embedding](https://www.kaggle.com/datasets/mauridb/product-data-from-walmart-usa-with-embeddings)')

# df = pd.read_csv(FILE)

st.dataframe(pd.read_csv(FILE, nrows=5))


st.header('Шаг 1. Время выполнения скрипта страницы')
st.metric('Скрипт страницы выполнен в', datetime.now().strftime("%H:%M:%S"))
st.button('Just button')

st.header('Шаг 2. Загрузка данных с кэшем')


def load_products():
    return pd.read_csv(FILE)

@st.cache_data(show_spinner='Загрузка...')
def load_products_cached():
    return pd.read_csv(FILE)


if st.button('Сравнить загрузку'):
    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Без кэша')
        start = time.time()
        products_without_cache = load_products()
        end = time.time()
        st.metric('Время загрузки: ', f'{end - start:.2f}')
        st.write(f"Количество товаров: {len(products_without_cache)}")

    with col2:
        st.subheader('С кэшем кэша')
        start = time.time()
        products_with_cache = load_products_cached()
        end = time.time()
        st.metric('Время загрузки: ', f'{end - start:.2f}')
        st.write(f"Количество товаров: {len(products_with_cache)}")

st.header('Шаг 3. Cache_data & cache_resourse')


@st.cache_data
def load_data():
    return [1,2,3]

@st.cache_resource
def load_resourse():
    return [1,2,3]


if st.button('Сравнить поведение кэша'):
    col1, col2 = st.columns(2)

    with col1:
        first = load_data()
        first.append(4) # [1,2,3,4]
        second = load_data()  # [1,2,3]
        st.write('cache_data:')
        st.code(str(second))

    with col2:
        first = load_resourse()
        first.append(4)  # [1,2,3,4]
        second = load_resourse()   # [1,2,3]
        st.write('cache_resourse:')
        st.code(str(second))



st.header('Шаг 4. Срок жизни кэша')

# Наш объект в кэше живёт бесконечно
@st.cache_data
def load_time():
    return datetime.now().strftime("%H:%M:%S")

# Наш объект в кэше живёт 3 секунды
@st.cache_data(ttl=3)
def load_time_ttl():
    return datetime.now().strftime("%H:%M:%S")

st.button('Обновить значения с ttl')

col1, col2 = st.columns(2)

with col1:
    st.metric('Без ttl загружено в', load_time())
with col2:
    st.metric('C ttl загружено в', load_time_ttl())


st.header('Шаг 5. Ограничение количества записей')

@st.cache_data(max_entries=3, show_spinner='Считаем ...', scope='session')
def limited_demo(query):
    time.sleep(1)
    return datetime.now().strftime("%H:%M:%S")

limit_query = st.text_input('Ваш запрос', '1')

if st.button('Выполнить запрос'):
    start = time.time()
    result = limited_demo(limit_query)
    end = time.time()

    st.metric('Время загрузки: ', f'{end - start:.2f}')
    st.write(f"Результат получен в: {result}")

# max = 3
# [1, 2, 3]             [4, 5, 6]
