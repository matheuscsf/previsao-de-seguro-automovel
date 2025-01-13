# Importando as bibliotecas necessárias
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Carregando o modelo treinado
modelo_rf = joblib.load("modelo_random_forest_final.joblib")

# Extraindo as colunas esperadas pelo modelo
colunas_modelo = modelo_rf.feature_names_in_

# Configurando o layout do Streamlit
st.title("🚗🔍 Previsão de Sinistros de Seguro de Carro")
st.write("Insira os dados do cliente abaixo para calcular a probabilidade de acionamento do seguro. 🎯")

# Inputs do usuário com interatividade
st.header("📋 Insira os Dados do Cliente:")
credit_score = st.slider("🌟 Pontuação de Crédito (CREDIT_SCORE):", min_value=0.0, max_value=1.0, step=0.01)
annual_mileage = st.number_input("📏 Quilometragem Anual (ANNUAL_MILEAGE):", min_value=0.0, step=500.0)
speeding_violations = st.slider("🚦 Violações de Velocidade (Box-Cox):", min_value=0.0, max_value=5.0, step=0.1)
past_accidents = st.slider("💥 Acidentes Anteriores (Box-Cox):", min_value=0.0, max_value=5.0, step=0.1)
vehicle_ownership = st.selectbox("🚘 Proprietário do Veículo?", [0, 1], format_func=lambda x: "Sim" if x == 1 else "Não")

# Inputs para variáveis categóricas (com nomes padronizados)
age_group = st.selectbox("🧓 Faixa Etária:", ['AGE_16-25', 'AGE_26-39', 'AGE_40-64', 'AGE_65+'])
driving_experience = st.selectbox("🛞 Experiência ao Volante:", ['DRIVING_EXPERIENCE_0-9y', 'DRIVING_EXPERIENCE_10-19y', 'DRIVING_EXPERIENCE_20-29y', 'DRIVING_EXPERIENCE_30y+'])
education_level = st.selectbox("🎓 Nível Educacional:", ['EDUCATION_none', 'EDUCATION_high school', 'EDUCATION_university'])
gender = st.selectbox("⚤ Gênero:", ['GENDER_male', 'GENDER_female'])
income_class = st.selectbox("💰 Classe Econômica:", ['INCOME_poverty', 'INCOME_working class', 'INCOME_middle class', 'INCOME_upper class'])
vehicle_year = st.selectbox("🚗 Ano do Veículo:", ['VEHICLE_YEAR_before 2015', 'VEHICLE_YEAR_after 2015'])

# Botão para calcular a probabilidade
if st.button("Clique aqui para calcular 🚀"):
    # Criando o DataFrame com todas as colunas esperadas pelo modelo
    input_data = pd.DataFrame(columns=colunas_modelo)
    input_data.loc[0] = 0  # Preenchendo todas as colunas com zero inicialmente

    # Atualizando as colunas com os valores fornecidos pelo usuário
    input_data['CREDIT_SCORE'] = credit_score
    input_data['ANNUAL_MILEAGE'] = annual_mileage
    input_data['SPEEDING_VIOLATIONS_BOXCOX'] = speeding_violations
    input_data['PAST_ACCIDENTS_BOXCOX'] = past_accidents
    input_data['VEHICLE_OWNERSHIP'] = vehicle_ownership
    input_data[age_group] = 1
    input_data[driving_experience] = 1
    input_data[education_level] = 1
    input_data[gender] = 1
    input_data[income_class] = 1
    input_data[vehicle_year] = 1

    # Fazendo a previsão
    probabilidade = modelo_rf.predict_proba(input_data)[:, 1][0]

    # Mostrando o resultado
    st.success(f"📊 A probabilidade de o cliente acionar o seguro é de **{probabilidade * 100:.2f}%**.")
