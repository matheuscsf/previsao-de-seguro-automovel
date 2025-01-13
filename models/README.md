# 📂 Pasta `models/`

Este diretório contém os modelos treinados utilizados no projeto **Previsão de Sinistros de Seguro de Carro**.

---

## 📋 Conteúdo

### 1. `modelo_random_forest_final.joblib`
- **Descrição**: Modelo Random Forest treinado com os dados do projeto.
- **Finalidade**: Este modelo é usado para prever a probabilidade de acionamento do seguro com base nos dados do cliente.
- **Formato**: O modelo foi salvo utilizando a biblioteca `joblib` para facilitar o carregamento e a execução em diferentes ambientes.

---

## 🛠️ Como Utilizar

1. **Carregamento do Modelo**
   - Certifique-se de que a biblioteca `joblib` está instalada.
   - Carregue o modelo no seu código Python:
     ```python
     import joblib
     modelo_rf = joblib.load("models/modelo_random_forest_final.joblib")
     ```

2. **Entrada de Dados**
   - O modelo espera os dados no mesmo formato em que foi treinado, incluindo as colunas geradas pelo One-Hot Encoding.
   - Certifique-se de ajustar os dados de entrada para corresponder às colunas esperadas. Use a propriedade `modelo_rf.feature_names_in_` para verificar as colunas.

3. **Predições**
   - Calcule a probabilidade de acionamento do seguro:
     ```python
     probabilidade = modelo_rf.predict_proba(dados_entrada)[:, 1]
     ```

---

## ⚠️ Observações

1. **Compatibilidade**:
   - O modelo foi treinado usando **Scikit-Learn 1.0+**. Certifique-se de que sua versão do Scikit-Learn é compatível.
   - Verifique se todas as colunas do dataset original estão representadas nos dados de entrada.

2. **Manutenção**:
   - Este é o modelo final utilizado no projeto. Caso sejam feitos novos treinamentos ou ajustes, salve os modelos atualizados nesta pasta.

3. **Validação**:
   - Antes de usar o modelo em produção, valide seu desempenho com um conjunto de dados real.

---

## 📈 Detalhes do Modelo

- **Algoritmo**: Random Forest Classifier 🌳
- **Hiperparâmetros**:
  - Número de árvores (`n_estimators`): 100
  - Critério de divisão (`criterion`): Gini
  - Random State: 42
- **Métricas no Conjunto de Teste**:
  - AUC-ROC: **88.69%**
  - F1-Score: **70.11%**
  - Precision: **72.25%**
  - Recall: **68.10%**

---

## 📦 Estrutura da Pasta

```plaintext
models/
├── modelo_random_forest_final.joblib  # Modelo Random Forest treinado
````

---

## 🔗 Referências

- [Documentação do Scikit-Learn](https://scikit-learn.org/stable/).
- [Como salvar e carregar modelos no Scikit-Learn](https://saturncloud-io.translate.goog/blog/sklearn-how-to-save-a-model-created-from-a-pipeline-and-gridsearchcv-using-joblib-or-pickle/?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=wa).
