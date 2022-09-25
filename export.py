from random import randrange, choice

import gis5ai.challenge.lpb as lpb

def export_all():
    for provider in ['tnt', 'ups', 'dpd', 'fedex', 'dhl', 'xpo']:
        f = open("gis5ai/server/static/provider_"+provider+".txt", 'w')

        f.write(getattr(lpb, provider+'_fields')())
        f.write("\n")
        for i in range(1000):
            export_data(f, provider)

        f.close()

def export_data(f, provider):
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

    f.write(getattr(lpb, provider+'_to_csv')(attempt_values))
    f.write("\n")

if __name__ == '__main__':
    export_all()
