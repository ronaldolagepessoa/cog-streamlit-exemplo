import streamlit as st
import pandas as pd
import plotly.express as px
from train import train_model
from train_view import train_view
from test_view import test_view

st.title("App de classificação de preço de mobile")

view_selection = st.radio("Escolha a tela", ["Treinamento", "Teste"])

if view_selection == "Treinamento":
    train_view()
else:
    test_view()
