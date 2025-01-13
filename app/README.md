# 📂 Pasta `app/`

Esta pasta contém os arquivos necessários para a implementação da interface interativa do projeto **Previsão de Sinistros de Seguro de Carro**, construída com **Streamlit**.

---

## 📋 Conteúdo

### 1. `app.py`
- **Descrição**: Arquivo principal da aplicação interativa.
- **Funcionalidades**:
  - Permite ao usuário inserir dados de clientes, como pontuação de crédito, infrações e acidentes anteriores.
  - Calcula a probabilidade de um cliente acionar o seguro com base nos dados fornecidos.
- **Execução**: Inicie o aplicativo com o comando:
  ```bash
  streamlit run app.py
 ### 2. `requirements.txt`
- **Descrição**: Lista as dependências necessárias para executar a aplicação Streamlit.
- **Instalação**: Instale as bibliotecas com o comando:
  ```bash
  pip install -r requirements.txt
### 3. **Principais Bibliotecas**:
- `streamlit:` Para criar a interface interativa.
- `pandas`: Para manipulação de dados.
- `joblib`: Para carregar o modelo treinado.
- `scikit-learn`: Utilizado para o modelo preditivo.

---

## 🖥️ **Como Executar a Aplicação**
1. **Certifique-se** de que o ambiente está configurado:
  - O Python 3.8+ deve estar instalado.
  - Instale as dependências com requirements.txt.
2.** Inicie a aplicação**: Na pasta app/, execute o seguinte comando:
  ```bash
  streamlit run app.py
```
3. **Acesse no navegador**: Após iniciar, a aplicação estará disponível no endereço:
  ```bash
http://localhost:8501
```

---

## ⚠️ Observações:

1. **Modelo Treinado**:
- Certifique-se de que o arquivo `modelo_random_forest_final.joblib` está disponível na pasta `models/`.
2. Colunas Esperadas pelo Modelo:
- O modelo foi treinado com um conjunto específico de colunas. A aplicação já está configurada para ajustar os dados fornecidos pelo usuário para corresponder ao modelo.
3. Debugging:
- Caso encontre erros, verifique se o arquivo do modelo foi carregado corretamente e se as dependências estão instaladas.

---

## 📦 Próximos Passos

1. **Adicione Gráficos Interativos**:
- Use bibliotecas como Plotly ou Altair para enriquecer a visualização.
2. **Personalize o Layout**:
- Atualize a interface para incluir mais explicações ou ajuda para o usuário.
3. **Implante a Aplicação**:
- Hospede a aplicação em serviços como Streamlit Cloud ou Heroku.


