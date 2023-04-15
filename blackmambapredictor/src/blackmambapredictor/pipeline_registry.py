"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()
    pipelines["__default__"] = sum(pipelines.values())
    return pipelines

# from kedro.pipeline import Pipeline

# from src.pipeline import PreparacaoDadosPipeline
# from src.pipeline import TreinamentoPipeline

# def register_pipelines() -> Dict[str, Pipeline]:
#     """Register the project's pipelines.

#     Returns:
#     A dictionary with a mapping from a pipeline name to a
#     ``Pipeline`` object.

#     """
#     return {
#         'PreparacaoDados': PreparacaoDadosPipeline(),
#         'Treinamento': TreinamentoPipeline(),
#     }

