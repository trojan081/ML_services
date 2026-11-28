import streamlit as st
import pandas as pd
from streamlit.elements.lib.color_util import Color

pg = st.navigation([
    st.Page('views/page.py', title='Главная страница')
        
])

pg.run()
