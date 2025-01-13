# 🚗🔍 Previsão de Sinistros de Seguro de Carro

Bem-vindo ao repositório do projeto de **Previsão de Sinistros de Seguro de Carro**! Aqui você encontrará todo o código, estrutura e documentação necessários para entender e replicar o projeto. 🛠️

---

## 📖 Visão Geral

O objetivo deste projeto é prever a probabilidade de um cliente acionar o seguro do seu carro. Utilizamos dados demográficos, comportamentais e informações do veículo para treinar um modelo preditivo. 

A aplicação final foi implementada em **Streamlit**, permitindo aos usuários interagir com os dados e visualizar as previsões de forma dinâmica e intuitiva. 🚀

---

## 📂 Estrutura do Repositório

- **`data/`**: Contém o dataset utilizado no projeto. O dataset foi obtido do [Kaggle](https://www.kaggle.com/datasets/sagnik1511/car-insurance-data).
- **`notebooks/`**: Notebooks com a análise exploratória e o treinamento do modelo.
- **`app/`**: Código para a interface interativa do projeto.
- **`models/`**: Modelo Random Forest treinado e salvo em formato `.joblib`.
- **`visuals/`**: Gráficos gerados durante o projeto, como a curva ROC e a importância das variáveis.
- **`README.md`**: Este arquivo com toda a explicação do projeto.

---

## 🎬 Demonstração

https://github.com/user-attachments/assets/7feff6f4-9834-4df2-9a97-832d9af471aa

---

## 📊 Dataset

- **Fonte**: [Car Insurance Data - Kaggle](https://www.kaggle.com/datasets/sagnik1511/car-insurance-data)
- **Descrição**: Este dataset contém informações sobre clientes e seus históricos de comportamento ao volante, como infrações de trânsito, acidentes anteriores e quilometragem anual.

### 📈 Variáveis Mais Importantes no Modelo

1. `CREDIT_SCORE` 🏦 - Pontuação de crédito do cliente.
2. `ANNUAL_MILEAGE` 📏 - Quilometragem anual percorrida pelo veículo.
3. `VEHICLE_OWNERSHIP` 🚘 - Indica se o cliente é proprietário do veículo.
4. `SPEEDING_VIOLATIONS` 🚦 - Número de infrações por excesso de velocidade.
5. `PAST_ACCIDENTS` 💥 - Número de acidentes anteriores.

---

## 🧰 Tecnologias Utilizadas

- **Linguagem**: Python 🐍
- **Bibliotecas**:
  - Scikit-Learn
  - Pandas
  - Matplotlib
  - Streamlit
- **Modelo Preditivo**: Random Forest 🌳

---

## 🖥️ Como Executar o Projeto

### 1. Clone o Repositório
```bash
git clone https://github.com/matheuscsf/previsao-de-seguro-automovel.git
cd car-insurance-prediction
```
### 2. Clone o Repositório
- Certifique-se de que o Python 3.8+ está instalado e execute:
```bash
pip install -r app/requirements.txt
```
### 3. Execute a Aplicação
- Na pasta `app/`, execute:
```bash
streamlit run app.py
```

---

# 📊 Resultados
🔑 Importância das Variáveis

Veja abaixo as variáveis mais relevantes para o modelo preditivo:

![feature_importance](https://github.com/user-attachments/assets/8aa034bb-7f36-42b8-9135-28510ee7d25e)

🧪 Curva ROC

O modelo alcançou uma área sob a curva ROC de 88.69%, indicando uma boa capacidade de separação entre as classes.

![roc_curve](https://github.com/user-attachments/assets/91fc2b7b-f3e1-4f0c-96ff-297d131e73ca)

---

# 🔗 Referências

- Dataset: Car Insurance Data - [Kaggle](https://www.kaggle.com/datasets/sagnik1511/car-insurance-data).
- Streamlit Documentation: [Streamlit.io](https://streamlit.io).

---

# 📜 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

# 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---

✨ Obrigado por explorar este projeto! Sinta-se à vontade para sugerir melhorias ou compartilhar seu feedback. ✨

---
