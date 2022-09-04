from challenge.result import Result
import challenge.common as common

def check_api_secret(team):
    res, r = common.check_api_version(team, "0.0.2")
    if not res.correct:
        return res

    res = common.validate_challenge(team, res)

    return res
