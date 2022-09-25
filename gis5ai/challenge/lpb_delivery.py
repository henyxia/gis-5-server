from random import randrange, choice

import challenge.common as common
import challenge.lpb as lpb

def lpb_delivery(team):
    version="0.0.40"
    res, r = common.check_api_version(team, version)
    if not res.correct:
        return res

    total = 0
    success = 0

    best_providers = {'tnt':0, 'ups':0, 'dpd':0, 'fedex':0, 'dhl':0, 'xpo':0}

    for i in range(1, 100):
        length = randrange(100, 2000)
        width = randrange(100, 2000)
        depth = randrange(100, 2000)
        volume = length*width*depth

        attempt_values = {
            'length': length,
            'width': width,
            'depth': depth,
            'volume': volume,
            'color': choice(['blue', 'green', 'red', 'yellow', 'orange', 'purple']),
            'scotch_taped': choice([True, False]),
            'fragile': choice([True, False]),
            'assurance_price': randrange(0, 200),
            'weight': randrange(5, 100000),
            'express': choice([True, False]),
            'signature_required': choice([True, False]),
            'destination_type': choice(['mailbox', 'parcel-relay-point']),
        }

        best_provider = lpb.get_best_provider(attempt_values)
        best_providers[best_provider] += 1

        _res = common.request_post_quiet(
            res=res,
            team=team,
            url='/lpb/delivery',
            data=attempt_values,
            validation=[
                dict(
                    title="Correct Provider",
                    key="selected_provider",
                    value=best_provider,
                ),
            ],
        )

        if type(_res) != bool:
            res = _res

        total += 1
        if _res:
            success += 1

    score = int(success*100/total)
    res.NewConditionalEntry(
        title="Success rate",
        condition=bool(score>=90),
        expected="90",
        got=str(score),
    )

    print(best_providers)

    return res
