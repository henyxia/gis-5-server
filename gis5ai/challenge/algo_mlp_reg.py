from sklearn.neural_network import MLPRegressor

import challenge.common as common

def algo_mlp_reg(team):
    return common.algo_common_reg_score(
        team=team,
        version="0.0.23",
        url="/algo/mlp/reg",
        classifier=MLPRegressor(random_state=team.id),
    )
