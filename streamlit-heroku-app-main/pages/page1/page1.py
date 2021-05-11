import streamlit as st
import import_ipynb

from pages.page1 import p1f1
from pages.page1 import p1f2
PAGE1 = {
    "p1": p1f1,
    "p2": p1f2
}

def app(): 
    selection = st.sidebar.radio("Page1", list(PAGE1.keys()))
    page1= PAGE1[selection]
    page1.app()
