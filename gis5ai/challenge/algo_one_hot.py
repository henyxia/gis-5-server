import challenge.common as common

def algo_one_hot(team):
    version="0.0.30"
    res, r = common.check_api_version(team, version)
    if not res.correct:
        return res

    data_in = [['Blue', 0], ['Yellow', 1], ['Green', 1], ['Red', 0]],
    test_data = [['Green', 1]]

    res = common.request_post(
        res=res,
        team=team,
        url='/preprocessing/encoder/one-hot',
        data=dict(
            X = data_in[0],
            Y = test_data,
        ),
        validation=[
            dict(
                title="Package Color Blue",
                key="package_color_Blue",
                value=0,
            ),
            dict(
                title="Package Color Yellow",
                key="package_color_Yellow",
                value=0,
            ),
            dict(
                title="Package Color Green",
                key="package_color_Green",
                value=1,
            ),
            dict(
                title="Package Color Red",
                key="package_color_Red",
                value=0,
            ),
            dict(
                title="Package Labeled",
                key="package_label_1",
                value=1,
            ),

        ],
    )

    return res
