# Importar bibliotecas
import pandas as pd
import streamlit as st
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split

# Carregar conjunto de dados 
df = pd.read_csv('../data/01_raw/data.csv')

data = data[data['shot_type'] == '2PT Field Goal']
data = data[['lat','lon','minutes_remaining','period','playoffs','shot_distance','shot_made_flag']]
data = data.dropna()
data

target_names = data.columns

# Treinar o modelo AdaBoost
X = data.drop('shot_made_flag', axis=1)
y = data['shot_made_flag'] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

model = AdaBoostClassifier(n_estimators=100, random_state=0)
model.fit(X, y)

# Cabeçalho do aplicativo
st.write("""
# Dashboard de Monitoramento da Operação

""")

# Sidebar do aplicativo
st.sidebar.header('Parâmetros do Modelo')
    
def user_input_features():
    lat = st.sidebar.slider('Latitude', 33.5433,34.0443,34.0883)
    lon = st.sidebar.slider('Longitude', -118.4878,-118.1318,-118.0498)
    minutes_remaining = st.sidebar.slider('Minutos Restantes', 2,6,11)
    period = st.sidebar.slider('Periodo', 1,4,7)
    playoffs = st.sidebar.slider('Playoffs', 0,0.5,1)
    shot_distance = st.sidebar.slider('Distancia do arremesso', 7, 26, 50)
    data = {'Latitude': lat,
            'Longitude': lon,
            'Minutos Restantes': minutes_remaining,
            'Periodo': period,
            'Playoffs': playoffs,
            'Distancia do arremesso': shot_distance            
            }
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
