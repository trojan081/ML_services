import streamlit as st
import pandas as pd
from streamlit.elements.lib.color_util import Color

pg = st.navigation([
    st.Page('views/text.py', title='Текст'),
    st.Page('views/analytics.py', title='Графики'),
    st.Page('views/widgets.py', title='Виджеты'),
    st.Page('views/cache.py', title='Кэш приложений'),
    st.Page(r'views\session_state.py', title='Состояние сессии'),
        
])

pg.run()
