import streamlit as st
import pandas as pd
import os
import pickle
from io import BytesIO


def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine="xlsxwriter")
    df.to_excel(writer, index=False, sheet_name="Sheet1")
    workbook = writer.book
    worksheet = writer.sheets["Sheet1"]
    format1 = workbook.add_format({"num_format": "0.00"})
    worksheet.set_column("A:A", None, format1)
    writer.close()
    processed_data = output.getvalue()
    return processed_data


def test_view():
    st.write(
        """
             ## Teste
             """
    )
    model_path = "models/my_model.pkl"
    if not os.path.isfile(model_path):
        st.warning(
            "Não existem modelos treinados. Volte à tela de treinamento e treine o modelo!"
        )
    else:
        uploaded_file = st.file_uploader("Escolha conjunto de teste")
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            st.dataframe(df)
            button_test = st.button("Executar previsão")
            if button_test:
                model = pickle.load(open(model_path, "rb"))
                min_max_scaler = pickle.load(open("models/min_max.pkl", "rb"))
                X_test = df.drop("id", axis=1).copy()
                y_pred = model.predict(min_max_scaler.transform(X_test))
                X_test["pred"] = y_pred
                st.dataframe(X_test)
                df_xlsx = to_excel(X_test)
                st.download_button(
                    label="📥 Download Current Result",
                    data=df_xlsx,
                    file_name="df_test.xlsx",
                )
