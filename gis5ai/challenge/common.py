from challenge.result import Result

import hashlib
import hmac
import uuid
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

def validate_challenge(team, res):
    base_url = team.base_url

    # create a new UUID as challenge
    challenge = str(uuid.uuid4())
    team_id = "team_"+str(team.id)
    team_secret = hashlib.sha256(team_id.encode('utf-8')).hexdigest()
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
