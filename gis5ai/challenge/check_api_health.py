from challenge.result import Result

import requests

def check_api_health(base_url):
    res = Result()

    # check if the API responds to the /version endpoint
    try:
        r = requests.get(base_url+"/version")
        res.NewEntry(
            title="Request API",
            correct=True,
            expected="Success",
            got="Success",
        )
    except requests.exceptions.RequestException as e:
        res.NewEntry(
            title="Request API",
            correct=False,
            expected="Success",
            got=str(repr(e))
        )
        return res

    if not res.NewConditionalEntry(
        title="Check status code",
        condition=(r.status_code == 200),
        expected="200",
        got="%d"%(r.status_code),
    ):
        return res

    response = r.json()
    if not res.NewConditionalEntry(
        title="Check status version",
        condition=(response['version']=="0.0.1"),
        expected="0.0.1",
        got=response['version'],
    ):
        return res

    res.correct = True
    return res
