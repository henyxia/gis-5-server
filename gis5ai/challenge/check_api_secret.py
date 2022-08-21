from challenge.result import Result
from challenge.common import check_api_version

def check_api_secret(team):
    res, r = check_api_version(team, "0.0.2")
    if not res.correct:
        return res

    res.correct = False
    return res
