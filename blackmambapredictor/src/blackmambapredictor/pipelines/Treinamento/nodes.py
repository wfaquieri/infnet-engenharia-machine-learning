"""
Módulo com funções para treinamento e avaliação de modelos de regressão logística e AdaBoostClassifier.

Este módulo utiliza a biblioteca PyCaret para treinar os modelos e as métricas de avaliação utilizadas são log_loss e f1_score.

Funções disponíveis:
- train_model_lr: treina um modelo de regressão logística com os dados de treinamento.
- metrics_lr: avalia um modelo de regressão logística com os dados de teste, retornando o valor da métrica log_loss.
- train_model_ada: treina um modelo AdaBoostClassifier com os dados de treinamento.
- metrics_ada: avalia um modelo AdaBoostClassifier com os dados de teste, retornando os valores das métricas log_loss e f1_score.

"""
import pandas as pd
from pycaret.classification import *
from sklearn.metrics import log_loss, f1_score
from kedro_mlflow.io.metrics import MlflowMetricDataSet

# Treina um modelo de regressão logística com pyCaret
def train_lr_model(x_train, y_train, session_id):

    # inicializa a configuração do pyCaret com os dados de treinamento e identificador de sessão
    setup(data=x_train, target=y_train, session_id=session_id)

    # treina o modelo de regressão logística
    lr_model = create_model('lr')

    return lr_model


# Calcula a métrica log loss para um modelo de regressão logística
def compute_lr_metrics(model, x_test: pd.DataFrame, y_test):
    # faz a previsão com o modelo no conjunto de teste
    test_predictions = predict_model(model, data=x_test)
    # extrai o valor real do conjunto de teste
    test_y = y_test
    # calcula a métrica log loss entre a previsão e os valores reais
    log_loss_value = log_loss(test_y, test_predictions['prediction_label'])

    metrics = {'log_loss_lr': log_loss_value}

    return {
        key: {'value': value, 'step': 1}
        for key, value in metrics.items()
    }


# Treina um modelo AdaBoost com pyCaret
def train_ada_model(x_train: pd.DataFrame, y_train, session_id):
    # inicializa a configuração do pyCaret com os dados de treinamento e identificador de sessão
    setup(data=x_train, target=y_train, session_id=session_id)

    # treina o modelo AdaBoost com os hiperparâmetros padrão
    ada_model = create_model('ada')

    return ada_model

# Calcula as métricas log loss e F1 score para um modelo AdaBoost
def compute_ada_metrics(model, x_test: pd.DataFrame, y_test):
    # faz a previsão com o modelo no conjunto de teste
    test_predictions = predict_model(model, data=x_test)
    # extrai o valor real do conjunto de teste
    test_y = y_test
    # calcula as métricas log loss e F1 score entre a previsão e os valores reais
    log_loss_value = log_loss(test_y, test_predictions['prediction_label'])
    f1_score_value = f1_score(test_y, test_predictions['prediction_label'])
    
    metrics = {
        'log_loss_ada': log_loss_value, 
        'f1_score_ada': f1_score_value
               }

    # retorna as métricas com um dicionário em um formato adequado para o MLflow
    return {
        key: {'value': value, 'step': 1}
        for key, value in metrics.items()
    }
