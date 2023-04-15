# Importar bibliotecas
from sklearn.datasets import load_iris
import pandas as pd
import streamlit as st
from sklearn.ensemble import AdaBoostClassifier

# Carregar conjunto de dados iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
target_names = iris.target_names

# Treinar o modelo AdaBoost
X = iris.data
y = iris.target
model = AdaBoostClassifier(n_estimators=100, random_state=0)
model.fit(X, y)

# Cabeçalho do aplicativo
st.write("""
# Dashboard de Monitoramento da Operação

Este aplicativo classifica a espécie de flor do conjunto de dados iris.
""")

# Sidebar do aplicativo
st.sidebar.header('Parâmetros do Modelo')
    
def user_input_features():
    sepal_length = st.sidebar.slider('Comprimento da Sépala', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Largura da Sépala', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Comprimento da Pétala', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Largura da Pétala', 0.1, 2.5, 0.2)
    data = {'Comprimento da Sépala': sepal_length,
            'Largura da Sépala': sepal_width,
            'Comprimento da Pétala': petal_length,
            'Largura da Pétala': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

# Obter entrada do usuário
df_user = user_input_features()

# Exibir entrada do usuário
st.subheader('Parâmetros do Usuário')
st.write(df_user)

# Fazer previsão e exibir resultados
prediction = model.predict(df_user)
prediction_proba = model.predict_proba(df_user)

st.subheader('Classificação')
st.write(target_names[prediction][0])

st.subheader('Probabilidades')
st.write(prediction_proba)
