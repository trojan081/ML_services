import streamlit as st
import pandas as pd
from streamlit.elements.lib.color_util import Color

st.set_page_config(
    page_title="Analytics",
    # page_icon="assets/hse.png",
    # layout="wide",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help'
    }
)


df = pd.read_csv('data/food_delivery.csv')
st.markdown('## Виджеты')



# #_________________ Выпадающие списки (selectbox) ___________

st.markdown('### Выпадающие списки (selectbox)')

unique_oc = df['Occupation'].unique()
filter_2 = st.selectbox('Профессия', unique_oc)
if filter_2:
    ocuppation_df = df[df['Occupation'] == filter_2]
    st.dataframe(ocuppation_df)
    st.write(f'Количество клиентов с профессией {filter_2} : {len(ocuppation_df)}')

#_________________ Выпадающие списки (multiselect) ___________

st.markdown('### Выпадающие списки (selectbox)')

filter_3 = st.multiselect('Профессия', unique_oc)
if filter_3:
    ocuppation_df = df[df['Occupation'].isin(filter_3)]
    st.dataframe(ocuppation_df)
    st.write(f'Количество клиентов с профессией {filter_3} : {len(ocuppation_df)}')

#_________________ Radiobutton ___________

st.markdown('### Radiobutton')

filter_4 = st.radio('Выбор значения', ['Age', 'Family size', 'Marital Status'])
df_filter_4 = df[[filter_4]]
if not df_filter_4.empty:
    st.line_chart(df_filter_4)

# ____________ САЙДБАР (боковая панель)
with st.sidebar:
    # Кнопка
    st.markdown('### Button')
    button_show_random_cutomers = st.button('Показать 3 случайных клиентов')

    # Ввод числа
    st.markdown('### Ввод числа')
    age = st.number_input('Возраст:', 18, 60, 25)

    # Чекбокс (флажок)
    st.markdown('### Флажок (checkbox)')
    st.write('Флажок')
    filter_1 = st.checkbox(f'Только старше {age}') # Возвращает значение

    # Слайдер
    st.markdown('### Слайдер')
    bottom, top = st.slider('Возраст', 18, 60, (20, 25)) 



if button_show_random_cutomers:
    st.write('Три случайных клиента')
    st.write(df.sample(3))

if filter_1:
    df_filtered = df[df['Age'] > age]
    st.write(f'Количество клиентов старше {age}: {len(df_filtered)}')

if bottom:
    st.write(f'Количество клиентов от {bottom} до {top}')
    # st.bar_chart(df[df['Age'] > bottom]) # Как красиво отобразить

