from sklearn.linear_model import LogisticRegression

import challenge.common as common

def algo_linear_reg(team):
    return common.algo_common_reg_precision(
        team=team,
        version="0.0.21",
        url="/algo/linear/reg",
        classifier=LogisticRegression()
    )
