import streamlit as st
import pandas as pd
from streamlit.elements.lib.color_util import Color


st.set_page_config(
    page_title="Text",
    # page_icon="assets/hse.png",
    layout="wide"
)


st.title('Текстовые форматы в Streamlit')

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
