import streamlit as st
import pandas as pd
from streamlit.elements.lib.color_util import Color

st.title('Первое приложение на Streamlit')

# ____________________ ТЕКСТ _________________________

# Заголовки
st.header('Это заголовок')
st.subheader('Это подзаголовок')

# Универсальная функция
st.write('Just some text')

# Пояснительные подписи
st.caption(
    'Пояснительная подпись',
    help='Всплывающая подсказка'
    )

st.markdown('# Markdown 1')
st.markdown('## Markdown 2')
st.markdown('### Markdown 3')

st.markdown("""
- level 1
    - level 2
        - level 3

"""  
)

st.markdown("<span style='color:red'>Красный текст</span>", unsafe_allow_html=True)

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


st.write('test_for_commit')
