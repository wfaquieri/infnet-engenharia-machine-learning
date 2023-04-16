"""
This is a boilerplate pipeline 'PreparacaoDados'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import (select_data, filter_data, split_data, split_metrics)

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
        func=select_data,
        name='select_data',
        inputs=['data_raw','params:shot_type_filter'],
        outputs='df_filtrado',
        ),
        node(
        func=split_data,
        name='split_data',
        inputs=[
        'df_filtrado', 
        'params:test_size',
        'params:random_state'
        ],
        outputs=['preprocessed_train_x', 'preprocessed_test_x', 'preprocessed_train_y', 'preprocessed_test_y'],
        ),
          node(
        func=split_metrics,
        name='split_metrics',
        inputs=['preprocessed_train_x','preprocessed_test_x','params:test_size'],
        outputs='train_test_metrics',
        )
    ])
