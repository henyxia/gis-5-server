from sklearn.tree import DecisionTreeRegressor

import challenge.common as common

def algo_decision_tree_reg(team):
    return common.algo_common_reg_score(
        team=team,
        version="0.0.22",
        url="/algo/decision-tree/reg",
        classifier=DecisionTreeRegressor(random_state=team.id),
    )
