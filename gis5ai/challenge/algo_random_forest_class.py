from sklearn.datasets import make_multilabel_classification
from sklearn.ensemble import RandomForestClassifier

import challenge.common as common

def algo_random_forest_class(team):
    res, r = common.check_api_version(team, "0.0.13")
    if not res.correct:
        return res

    dataset = make_multilabel_classification(n_features=2, n_classes=1)
    classifier = RandomForestClassifier(random_state=team.id)
    classifier.fit(dataset[0], dataset[1])

    test_value = [[1.12, 1.69]]
    correct_class = classifier.predict(test_value)
    precisions = classifier.predict_proba(test_value)

    print(correct_class[0])
    print(precisions[0][correct_class[0]])

    res = common.request_post(
        res=res,
        team=team,
        url="/algo/random-forest/class",
        data=dict(
            X=dataset[0].tolist(),
            Y=dataset[1].tolist(),
            test_value=test_value,
        ),
        validation=[
            dict(
                title="Correct class",
                key="predicted_class",
                value=correct_class[0],
            ),
            dict(
                title="Class precision",
                key="precision",
                value=precisions[0][correct_class[0]],
            ),
        ],
    )

    return res
