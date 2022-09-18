from sklearn.svm import LinearSVC

import challenge.common as common

def algo_linear_svc(team):
    return common.algo_common_class_score(
        team=team,
        version="0.0.14",
        url="/algo/svm/class",
        classifier=LinearSVC(random_state=team.id),
    )
