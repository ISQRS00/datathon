import streamlit as st
import pandas as pd
import joblib
import requests
from io import BytesIO

# 📌 Funções para carregar os arquivos salvos corretamente
@st.cache_data
def load_model():
    url = "https://raw.githubusercontent.com/ISQRS00/datathon/main/arquivos_utilizados/modelo_novo.pkl"
    try:
        response = requests.get(url)
        response.raise_for_status()
        model = joblib.load(BytesIO(response.content))  # Carrega o modelo da memória
        return model
    except Exception as e:
        st.error(f"Erro ao carregar o modelo: {e}")
        return None

@st.cache_data
def load_scaler():
    url = "https://raw.githubusercontent.com/ISQRS00/datathon/main/arquivos_utilizados/pipeline_scaler.pkl"
    try:
        response = requests.get(url)
        response.raise_for_status()
        scaler = joblib.load(BytesIO(response.content))  # Carrega o scaler da memória
        return scaler
    except Exception as e:
        st.error(f"Erro ao carregar o scaler: {e}")
        return None

@st.cache_data
def load_label_encoder():
    url = "https://raw.githubusercontent.com/ISQRS00/datathon/main/arquivos_utilizados/label_encoder.pkl"
    try:
        response = requests.get(url)
        response.raise_for_status()
        encoder = joblib.load(BytesIO(response.content))  # Carrega o LabelEncoder da memória
        return encoder
    except Exception as e:
        st.error(f"Erro ao carregar o LabelEncoder: {e}")
        return None

# 📌 Carregar os arquivos
modelo = load_model()
scaler = load_scaler()
label_encoder = load_label_encoder()

# 📌 Criar abas para organização
st.title(" Predição da Pedra-Conceito")

abas = st.tabs(["Introdução", "Predição"])

# 📌 1️⃣ Aba de Introdução
with abas[0]:
    st.markdown("""
    ### Sistema de Pedras-Conceito
    Para tornar a jornada educacional mais motivadora, criamos o **sistema de pedras-conceito**, representando diferentes faixas de desempenho, do menor ao maior nível.  
    As pedras - **Quartzo, Ágata, Ametista e Topázio** - simbolizam a progressão dos alunos, mostrando que eles são únicos e preciosos, assim como suas pedras.

    ---
    
    ### Faixas de Desempenho
    Os alunos são classificados de acordo com os seguintes critérios:

    - **Quartzo (Baixo desempenho)** → INDE até **6.1**
    - **Ágata (Desempenho intermediário)** → INDE entre **6.1 e 7.2**
    - **Ametista (Bom desempenho)** → INDE entre **7.2 e 8.2**
    - **Topázio (Alto desempenho)** → INDE acima de **8.2**

    A classificação é baseada em um modelo de **Machine Learning**, que analisa o desempenho acadêmico e engajamento do aluno para prever sua pedra correspondente.

    ---

    ### Como o modelo funciona?
    Utilizando técnicas de Machine Learning, testamos três modelos para encontrar a melhor abordagem:

    - **🌲 RandomForest:** Algoritmo baseado em árvores de decisão, capaz de lidar bem com dados complexos.  
      - **Acurácia:** 🟢 **83.7%**  
    - **📈 GradientBoosting:** Modelo que melhora continuamente os erros de predição para aumentar a precisão.  
      - **Acurácia:** 🟡 **77.0%**  
    - **📊 LogisticRegression:** Modelo estatístico usado para prever categorias.  
      - **Acurácia:** 🔴 **74.9%**  

    O **RandomForest** foi o modelo que obteve a melhor performance, atingindo **83.7% de acurácia**, sendo utilizado para as previsões desta ferramenta.

    ---

    ### Acesse o Notebook Completo
    Para mais detalhes sobre o treinamento do modelo e a análise dos dados, 
    acesse o notebook completo no GitHub:  
    👉 [Clique aqui para ver o código](https://github.com/ISQRS00/datathon/blob/main/nootbooks/modelo_final_1_pedra.ipynb)  


    ---
    
    ###  Base de entrada e saída utilizadas nesse modelo
    
    O modelo de previsão de pedras foi desenvolvido utilizando a base antiga. acesse os arquivos no GitHub:
    
    👉 [Clique aqui para baixar o arquivo de entrada](https://github.com/ISQRS00/datathon/blob/main/dados_de_entrada/PEDE_PASSOS_BASE_ANTIGA.csv)  
    
    👉 [Clique aqui para baixar o arquivo de saída](https://github.com/ISQRS00/datathon/blob/main/datasets/base_modelo_ponto_de_virada.csv)  
                

    """)
#  Aba de Predição
with abas[1]:
    st.write("Insira os dados abaixo (valores de 0 a 10) para obter uma predição:")

    # Inputs do usuário
    num_ida = st.number_input("Número IDA", min_value=0.0, max_value=10.0, value=5.0)
    num_ieg = st.number_input("Número IEG", min_value=0.0, max_value=10.0, value=5.0)
    num_ian = st.number_input("Número IAN", min_value=0.0, max_value=10.0, value=5.0)
    des_fase = st.number_input("Fase", min_value=0.0, max_value=10.0, value=5.0)

    # Criar DataFrame com os inputs do usuário
    entrada_usuario = pd.DataFrame([[num_ida, num_ieg, num_ian, des_fase]], 
                                   columns=["num_ida", "num_ieg", "num_ian", "des_fase"])

    # Aplicar o scaler nos dados digitados
    if scaler:
        entrada_tratada = scaler.transform(entrada_usuario)
    else:
        st.error("Scaler não carregado corretamente.")

    # Fazer a predição quando o botão for clicado
    if modelo and scaler and label_encoder and st.button("Descobrir Pedra"):
        pedra_predita = modelo.predict(entrada_tratada)[0]  # Fazer predição
        
        # Converter o número de volta para o nome da pedra usando LabelEncoder
        pedra_nome = label_encoder.inverse_transform([pedra_predita])[0]

        # Exibir resultado final
        st.success(f"🔷 Sua pedra correspondente é: {pedra_nome}")
