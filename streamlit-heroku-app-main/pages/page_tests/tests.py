import streamlit as st
import import_ipynb


from pages.page_tests import graphiques
from pages.page_tests import entrees
from pages.page_tests import formes_textuelles
from pages.page_tests import Affichages
from pages.page_tests import Organisation_page
from pages.page_tests import Messages_temps
TESTS_name = {
    "formes textuelles": formes_textuelles,
    "Affichages":Affichages,
    "Organisation page":Organisation_page,
    "Entrees":entrees,
    "Graphiques":graphiques,
    "Messages, temps":Messages_temps,
    
}

def app(): 
    selection = st.sidebar.radio("Parties", list(TESTS_name.keys()))
    tests= TESTS_name[selection]
    tests.app()
