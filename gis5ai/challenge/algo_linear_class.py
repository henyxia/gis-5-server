from sklearn.datasets import make_multilabel_classification
from sklearn.linear_model import RidgeClassifier

import challenge.common as common

def algo_linear_class(team):
    res, r = common.check_api_version(team, "0.0.11")
    if not res.correct:
        return res

    dataset = make_multilabel_classification(n_features=2, n_classes=1)
    classifier = RidgeClassifier()
    classifier.fit(dataset[0], dataset[1])
    precision = classifier.score(dataset[0], dataset[1])

    test_value = [[1.12, 1.69]]
    correct_class = classifier.predict(test_value)

    print(correct_class[0])
    print(precision)

    res = common.request_post(
        res=res,
        team=team,
        url="/algo/linear/class",
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
                value=precision,
            ),
        ],
    )

    return res
