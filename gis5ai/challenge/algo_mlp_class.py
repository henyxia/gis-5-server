from sklearn.neural_network import MLPClassifier

import challenge.common as common

def algo_mlp_class(team):
    return common.algo_common_class_precision(
        team=team,
        version="0.0.15",
        url="/algo/mlp/class",
        classifier=MLPClassifier(random_state=team.id),
    )
