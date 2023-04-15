"""
This is a boilerplate pipeline 'Treinamento'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import (train_lr_model, compute_lr_metrics, train_ada_model, compute_ada_metrics)

# Definição dos nós do pipeline
def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=train_lr_model,
                name="train_lr_model",
                inputs=dict(
                    x_train="preprocessed_train_x",
                    y_train="preprocessed_train_y",
                    session_id="params:inicializador_pycaret",
                ),
                outputs="lr_model",
            ),
                        node(
                func=train_ada_model,
                name="train_ada_model",
                inputs=dict(
                    x_train="preprocessed_train_x",
                    y_train="preprocessed_train_y",
                    session_id="params:inicializador_pycaret",
                ),
                outputs="ada_model",
            ),
            node(
                func=compute_lr_metrics,
                name="compute_lr_metrics",
                inputs=dict(
                    model="lr_model",
                    x_test="preprocessed_test_x",
                    y_test="preprocessed_test_y"
                ),
                outputs="lr_metrics",
            ),
            node(
                func=compute_ada_metrics,
                name="compute_ada_metrics",
                inputs=dict(
                    model="ada_model",
                    x_test="preprocessed_test_x",
                    y_test="preprocessed_test_y"
                ),
                outputs="ada_metrics",
            ),
        ]
    )
