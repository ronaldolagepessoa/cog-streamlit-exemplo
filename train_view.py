import streamlit as st
import pandas as pd
import plotly.express as px
from train import train_model


def train_view():
    st.write(
        """
             ## Treinamento
             """
    )
    uploaded_file = st.file_uploader("Escolha o conjunto de treinamento")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
        fig = px.bar(
            df["price_range"].value_counts().reset_index(name="Frequência"),
            x="price_range",
            y="Frequência",
        )
        st.plotly_chart(fig)
        button_train = st.button("Treinar modelo")
        if button_train:
            cm, accuracy, model = train_model(df)
