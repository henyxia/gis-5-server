import challenge.common

def check_api_health(team):
    #FIXME
    res,r = challenge.common.check_api_version(team, "0.0.1")
    return res
