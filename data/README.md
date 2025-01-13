# 📂 Pasta `data/`

Este diretório contém os dados utilizados no projeto **Previsão de Sinistros de Seguro de Carro**.

---

## 📊 Arquivos Disponíveis

### 1. `Car_Insurance_Claim.csv`
- **Descrição**: Este é o dataset principal utilizado no projeto. Ele contém informações sobre os clientes, incluindo dados demográficos, comportamentais e características do veículo, além da variável alvo (`OUTCOME`) que indica se o seguro foi acionado.
- **Fonte**: O dataset foi obtido do Kaggle. Você pode acessá-lo no seguinte link: [Car Insurance Data - Kaggle](https://www.kaggle.com/datasets/sagnik1511/car-insurance-data).

#### Estrutura do Dataset
| Coluna                     | Descrição                                                                 |
|----------------------------|---------------------------------------------------------------------------|
| `ID`                       | Identificador único do cliente                                           |
| `AGE`                      | Faixa etária do cliente                                                 |
| `GENDER`                   | Gênero do cliente                                                       |
| `DRIVING_EXPERIENCE`       | Anos de experiência ao volante                                          |
| `EDUCATION`                | Nível educacional do cliente                                            |
| `INCOME`                   | Classe econômica do cliente                                             |
| `VEHICLE_OWNERSHIP`        | Indica se o cliente é proprietário do veículo (1 = Sim, 0 = Não)         |
| `VEHICLE_YEAR`             | Ano de fabricação do veículo                                            |
| `MARRIED`                  | Estado civil do cliente (1 = Casado, 0 = Não)                           |
| `CHILDREN`                 | Número de filhos                                                        |
| `POSTAL_CODE`              | Código postal                                                          |
| `ANNUAL_MILEAGE`           | Quilometragem anual do veículo (em milhas)                              |
| `SPEEDING_VIOLATIONS`      | Número de infrações por excesso de velocidade                           |
| `PAST_ACCIDENTS`           | Número de acidentes anteriores                                          |
| `DUIS`                     | Número de infrações relacionadas ao consumo de álcool                  |
| `OUTCOME`                  | Variável alvo (1 = Seguro acionado, 0 = Seguro não acionado)            |

---

## ⚠️ Observações
1. **Integridade dos Dados**:
   - Certifique-se de que o arquivo `Car_Insurance_Claim.csv` esteja nesta pasta antes de executar os notebooks ou scripts do projeto.
   - Caso o arquivo original seja substituído, verifique se ele segue o mesmo formato descrito acima.

2. **Privacidade**:
   - O dataset é fictício e não contém informações sensíveis de clientes reais.
   - Qualquer uso fora do escopo deste projeto deve seguir as diretrizes do Kaggle.

---

## 🔗 Fonte
- [Car Insurance Data - Kaggle](https://www.kaggle.com/datasets/sagnik1511/car-insurance-data)

---

✨ _Obrigado por explorar este projeto! Para dúvidas ou sugestões, sinta-se à vontade para contribuir._ ✨
