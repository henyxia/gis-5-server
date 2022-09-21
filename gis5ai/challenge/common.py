from challenge.result import Result

import hmac
import uuid
import requests

from sklearn.datasets import make_multilabel_classification

def check_api_version(team, version):
    base_url = team.base_url
    res = Result()

    # check if the API responds to the /version endpoint
    try:
        r = requests.get(base_url+"/version")
        res.NewEntry(
            title="/version - Request API",
            correct=True,
            expected="Success",
            got="Success",
        )
    except requests.exceptions.RequestException as e:
        res.NewEntry(
            title="/version - Request API",
            correct=False,
            expected="Success",
            got=str(repr(e))
        )
        return res, None

    if not res.NewConditionalEntry(
        title="/version - Check status code",
        condition=(r.status_code == 200),
        expected="200",
        got="%d"%(r.status_code),
    ):
        return res, None

    response = r.json()
    if not res.NewConditionalEntry(
        title="/version - Check status version",
        condition=(response['version']==version),
        expected=version,
        got=response['version'],
    ):
        return res, None

    res.correct = True
    return res, r

def validate_challenge(team, res):
    base_url = team.base_url

    # create a new UUID as challenge
    challenge = str(uuid.uuid4())
    team_secret = team.get_secret()
    digest = hmac.new(
        team_secret.encode('utf-8'),
        challenge.encode('utf-8'),
        "sha256"
    ).hexdigest()

    # check if the API with the correct challenge
    try:
        r = requests.post(base_url+"/identify",
            json={'challenge': challenge},
        )
        res.NewEntry(
            title="/identify - Request API",
            correct=True,
            expected="Success",
            got="Success",
        )
    except requests.exceptions.RequestException as e:
        res.NewEntry(
            title="/identify - Request API",
            correct=False,
            expected="Success",
            got=str(repr(e))
        )
        return res

    if not res.NewConditionalEntry(
        title="/identify - Check status code",
        condition=(r.status_code == 200),
        expected="200",
        got="%d"%(r.status_code),
    ):
        return res

    response = r.json()
    if not res.NewConditionalEntry(
        title="/identify - check challenge",
        # not using compare_digest as we do not care about time attack
        condition=(response['digest']==digest),
        expected=digest,
        got=response['digest'],
    ):
        return res

    return res

def request_post(team, res, url, data, validation):
    base_url = team.base_url

    # check if the API with the correct challenge
    try:
        r = requests.post(base_url+url,
            json=data,
        )
        res.NewEntry(
            title=url+" - Request API",
            correct=True,
            expected="Success",
            got="Success",
        )
    except requests.exceptions.RequestException as e:
        res.NewEntry(
            title=url+" - Request API",
            correct=False,
            expected="Success",
            got=str(repr(e))
        )
        return res

    if not res.NewConditionalEntry(
        title=url+" - Check status code",
        condition=(r.status_code == 200),
        expected="200",
        got="%d"%(r.status_code),
    ):
        return res

    response = r.json()
    for val in validation:
        if not res.NewConditionalEntry(
            title=url+" - "+val['title'],
            condition=bool(response[val['key']]==val['value']),
            expected=str(val['value']),
            got=str(response[val['key']]),
        ):
            return res

    return res

def algo_common_class_score(team, version, url, classifier):
    res, r = check_api_version(team, version)
    if not res.correct:
        return res

    dataset = make_multilabel_classification(n_features=2, n_classes=1)
    classifier.fit(dataset[0], dataset[1])

    test_value = [[1.12, 1.69]]
    correct_class = classifier.predict(test_value)
    score = classifier.score(dataset[0], dataset[1])

    print(correct_class[0])
    print(score)

    res = request_post(
        res=res,
        team=team,
        url=url,
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
                title="Class score",
                key="score",
                value=score,
            ),
        ],
    )

    return res

def algo_common_class_precision(team, version, url, classifier):
    res, r = check_api_version(team, version)
    if not res.correct:
        return res

    dataset = make_multilabel_classification(n_features=2, n_classes=1)
    classifier.fit(dataset[0], dataset[1])

    test_value = [[1.12, 1.69]]
    correct_class = classifier.predict(test_value)
    precisions = classifier.predict_proba(test_value)

    print(correct_class[0])
    print(precisions[0][correct_class[0]])

    res = request_post(
        res=res,
        team=team,
        url=url,
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

def algo_common_reg_score(team, version, url, classifier):
    res, r = check_api_version(team, version)
    if not res.correct:
        return res

    dataset = make_multilabel_classification(n_features=2, n_classes=1)
    classifier.fit(dataset[0], dataset[1])

    test_value = [[1.12, 1.69]]
    predicted_value = classifier.predict(test_value)
    score = classifier.score(dataset[0], dataset[1])

    print(predicted_value[0])
    print(score)

    res = request_post(
        res=res,
        team=team,
        url=url,
        data=dict(
            X=dataset[0].tolist(),
            Y=dataset[1].tolist(),
            test_value=test_value,
        ),
        validation=[
            dict(
                title="Predicted value",
                key="predicted_value",
                value=predicted_value[0],
            ),
            dict(
                title="Class score",
                key="score",
                value=score,
            ),
        ],
    )

    return res

def algo_common_reg_precision(team, version, url, classifier):
    res, r = check_api_version(team, version)
    if not res.correct:
        return res

    dataset = make_multilabel_classification(n_features=2, n_classes=1)
    classifier.fit(dataset[0], dataset[1])

    test_value = [[1.12, 1.69]]
    predicted_value = classifier.predict(test_value)
    precisions = classifier.predict_proba(test_value)

    print(predicted_value[0])
    print(precisions[0][0])

    res = request_post(
        res=res,
        team=team,
        url=url,
        data=dict(
            X=dataset[0].tolist(),
            Y=dataset[1].tolist(),
            test_value=test_value,
        ),
        validation=[
            dict(
                title="Predicted value",
                key="predicted_value",
                value=predicted_value[0],
            ),
            dict(
                title="Value precision",
                key="precision",
                value=precisions[0][0],
            ),
        ],
    )

    return res
