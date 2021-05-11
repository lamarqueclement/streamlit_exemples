#app.py                           DASHBOARD
import import_ipynb
from pages.page1 import page1
from pages.page_tests import tests

PAGES = {
    "page1": page1,
    "page_tests": tests
}
######  DOCS  ######
# https://docs.streamlit.io/en/stable/getting_started.html#share-your-app
######  LAUNCH  #####
# cd Desktop\DASH or similar\example2
# streamlit run app.py                                      (local )
# streamlit run app.py --server.address=127.0.0.1           (local only)
# CTRL + C: arreter 
######  DEPLOY STREAMLIT ON WEB  #####
# https://medium.com/analytics-vidhya/how-to-deploy-streamlit-web-app-on-heroku-1235d827f1f
###### RQ ######
# use sidebar  st.sidebar.radio    (incorporation de l'élément dans le menu)
# CONNEXION : https://blog.jcharistech.com/2020/05/30/how-to-add-a-login-section-to-streamlit-blog-app/
import streamlit as st

#st.set_page_config(
#         page_title="Ex-stream-ly Cool App",
#         page_icon="🧊",
#         layout="wide",
#         initial_sidebar_state="expanded")
###########################################################
##################  SOMMAIRE GENERAL  #####################
###########################################################


selection = st.sidebar.radio("Navigation", list(PAGES.keys()))
page = PAGES[selection]
page.app()
 