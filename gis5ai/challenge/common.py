from challenge.result import Result

import requests

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
