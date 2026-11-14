import streamlit as st
import pandas as pd
from streamlit.elements.lib.color_util import Color

st.set_page_config(
    page_title="Analytics",
    # page_icon="assets/hse.png",
    layout="wide"
)


# ____________________ ТАБЛИЧНЫЕ ДАННЫЕ _________________________

# словарь
custom_dict = {
    'course' : [1,2,3,4,],
    'marks' : [8, 9, 10, 6, ]
}
st.write(custom_dict)
# Датафрейм
custom_df = pd.DataFrame(custom_dict)
st.write(custom_df)

st.header('Это загруженный датасет')

# CSV в датафрейм
df = pd.read_csv('data/food_delivery.csv')
st.write(df)

# ____________________ ГРАФИКИ _________________________

st.subheader('Linechart')
st.line_chart(
    df['Age'].head(50),
    x_label='Индекс',
    y_label='Возраст'
)

st.subheader('Barchart')

ages = df['Age'].value_counts()

st.bar_chart(
    ages,
    x_label='Возраст',
    y_label='Количество',
    color='#F39C12'
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric('Средний возраст клиентов', round(df['Age'].mean(), 1))
with col2:
    st.metric('Минимальный возраст клиента', round(df['Age'].min(), 1))
with col2:
    st.metric('Максимальный возраст клиента', round(df['Age'].max(), 1))

st.header('Scatter chart')
st.scatter_chart(df,
                 x='Age',
                 y='Family size',
                 x_label='Возраст',
                 y_label='Размер семьи'
                 )

st.header('Map')

coords = df[['latitude', 'longitude']]
st.map(coords)


st.header('График с фильтрацией')

mask = df['Output'] == 'Yes'
only_yes = df[mask]

col1, col2 = st.columns(2)
with col1:
    st.write('Всего клиентов: ', len(df), 'из них заказали: ', only_yes)
with col2:
    st.bar_chart(only_yes['Occupation'].value_counts(), horizontal=True)
    st.write('Количество студентов', len(only_yes[only_yes['Occupation'] == 'Student']))


st.subheader('Сравнение групп')
yes_by_age = df[df['Output'] == 'Yes']['Age'].value_counts()
no_by_age = df[df['Output'] == 'No']['Age'].value_counts()

compare = pd.DataFrame(
    {
        'Заказали': yes_by_age,
        'Не заказали':no_by_age
    }
)

with st.expander('Сравнительная таблица'):
    st.dataframe(compare)

st.line_chart(
    compare, 
    x_label='Возраст',
    y_label='Количество клиентов'
              )