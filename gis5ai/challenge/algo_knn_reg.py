from sklearn.neighbors import KNeighborsRegressor

import challenge.common as common

def algo_knn_reg(team):
    return common.algo_common_reg_score(
        team=team,
        version="0.0.20",
        url="/algo/knn/reg",
        classifier=KNeighborsRegressor()
    )
