import sys
from math import ceil

def get_best_provider(values):
    prices = {
        "tnt": tnt(values),
        "ups": ups(values),
        "dpd": dpd(values),
        "fedex": fedex(values),
        "dhl": dhl(values),
        "xpo": xpo(values),
    }

    lowest_price = None
    best_provider = None
    for provider, price in prices.items():
        sys.stdout.write("%s %-20d " % (provider, price))
        if lowest_price == None or price < lowest_price:
            lowest_price = price
            best_provider = provider

    sys.stdout.write("\n")

    return best_provider

def tnt(v):
    price = (v['length']*v['width']*v['depth'])/1000000
    price += v['assurance_price']
    if v['scotch_taped']:
        price *= 0.1
    return price

def tnt_fields():
    return 'length,width,depth,volume,color,scotch_taped,fragile,assurance_price,weight,express,signature_required,destination_type,price'

def tnt_to_csv(v):
    csv = str(v['length'])
    csv += ','
    csv += str(v['width'])
    csv += ','
    csv += str(v['depth'])
    csv += ','
    csv += str(v['volume'])
    csv += ','
    csv += str(v['color'])
    csv += ','
    csv += str(v['scotch_taped'])
    csv += ','
    csv += str(v['fragile'])
    csv += ','
    csv += str(v['assurance_price'])
    csv += ','
    csv += str(v['weight'])
    csv += ','
    csv += str(v['express'])
    csv += ','
    csv += str(v['signature_required'])
    csv += ','
    csv += str(v['destination_type'])
    csv += ','
    csv += str(int(tnt(v)))
    return csv

def ups(v):
    price = v['weight'] / 1000
    if v['destination_type'] == 'mailbox':
        price *= 10

    return price

def ups_fields():
    return 'length,width,depth,color,scotch_taped,fragile,assurance_price,weight,express,signature_required,destination_type,price'

def ups_to_csv(v):
    csv = str(v['length'])
    csv += ','
    csv += str(v['width'])
    csv += ','
    csv += str(v['depth'])
    csv += ','
    csv += str(v['color'])
    csv += ','
    csv += str(v['scotch_taped'])
    csv += ','
    csv += str(v['fragile'])
    csv += ','
    csv += str(v['assurance_price'])
    csv += ','
    csv += str(v['weight'])
    csv += ','
    csv += str(v['express'])
    csv += ','
    csv += str(v['signature_required'])
    csv += ','
    csv += str(v['destination_type'])
    csv += ','
    csv += str(int(ups(v)))
    return csv

def dpd(v):
    if v['color'] == 'purple':
        return 12

    price = v['length']*v['width']*v['depth']*v['weight']/1000000000000
    if v['assurance_price']:
        price *= v['assurance_price']

    return min(1200, price)

def dpd_fields():
    return 'length,width,depth,volume,color,scotch_taped,fragile,assurance_price,weight,express,signature_required,destination_type,price'

def dpd_to_csv(v):
    csv = str(v['length'])
    csv += ','
    csv += str(v['width'])
    csv += ','
    csv += str(v['depth'])
    csv += ','
    csv += str(v['volume'])
    csv += ','
    if v['color'] == 'purple':
        csv += 'PURPLE'
    else:
        csv += str(v['color'])
    csv += ','
    csv += str(v['scotch_taped'])
    csv += ','
    csv += str(v['fragile'])
    csv += ','
    csv += str(v['assurance_price'])
    csv += ','
    csv += str(v['weight'])
    csv += ','
    csv += str(v['express'])
    csv += ','
    csv += str(v['signature_required'])
    csv += ','
    csv += str(v['destination_type'])
    csv += ','
    csv += str(int(dpd(v)))
    return csv

def fedex(v):
    price = v['volume'] / 100000000
    price += 20
    if v['express']:
        price *= 10

    if v['signature_required']:
        price *= 2

    if v['destination_type'] == 'parcel-relay-point':
        price /= 2

    if v['fragile']:
        price *= 2

    return price

def fedex_fields():
    return 'length,width,depth,volume,color,scotch_taped,fragile,assurance_price,weight,express,signature_required,destination_type,price'

def fedex_to_csv(v):
    csv = str(v['length'])
    csv += ','
    csv += str(v['width'])
    csv += ','
    csv += str(v['depth'])
    csv += ','
    csv += str(v['volume'])
    csv += ','
    csv += v['color'].title()
    csv += ','
    csv += str(v['scotch_taped'])
    csv += ','
    csv += str(v['fragile'])
    csv += ','
    csv += str(v['assurance_price'])
    csv += ','
    csv += str(v['weight'])
    csv += ','
    csv += str(v['express'])
    csv += ','
    csv += str(v['signature_required'])
    csv += ','
    csv += v['destination_type'].title()
    csv += ','
    csv += str(int(fedex(v)))
    return csv

def dhl(v):
    price = 10
    if v['length'] > 300:
        price += v['length']*0.1

    if v['express']:
        price += 10

    return price

def dhl_fields():
    return 'length,width,depth,volume,color,scotch_taped,fragile,assurance_price,weight,express,signature_required,destination_type,price'

def dhl_to_csv(v):
    csv = str(v['length'])
    csv += ','
    csv += str(v['width'])
    csv += ','
    csv += str(v['depth'])
    csv += ','
    csv += str(v['volume'])
    csv += ','
    csv += str(v['color'])
    csv += ','
    csv += str(v['scotch_taped'])
    csv += ','
    csv += str(v['fragile'])
    csv += ','
    csv += str(v['assurance_price'])
    csv += ','
    csv += str(v['weight'])
    csv += ','
    csv += str(v['express'])
    csv += ','
    csv += str(v['signature_required'])
    csv += ','
    csv += str(v['destination_type'])
    csv += ','
    csv += str(int(dhl(v)))
    return csv

def xpo(v):
    return (
        ceil(v['length']/1000)*
        ceil(v['width']/1000)*
        ceil(v['depth']/1000)*
        max(1, int(v['fragile']*2))*
        60
    )

def xpo_fields():
    return 'length,width,depth,volume,color,scotch_taped,fragile,assurance_price,weight,express,signature_required,destination_type,standart_size,price'

def xpo_to_csv(v):
    csv = str(v['length'])
    csv += ','
    csv += str(v['width'])
    csv += ','
    csv += str(v['depth'])
    csv += ','
    csv += str(v['volume'])
    csv += ','
    csv += str(v['color'])
    csv += ','
    csv += str(v['scotch_taped'])
    csv += ','
    csv += str(v['fragile'])
    csv += ','
    csv += str(v['assurance_price'])
    csv += ','
    csv += str(v['weight'])
    csv += ','
    csv += str(v['express'])
    csv += ','
    csv += str(v['signature_required'])
    csv += ','
    csv += str(v['destination_type'])
    csv += ','
    csv += str(
        ceil(v['length']/1000)*
        ceil(v['width']/1000)*
        ceil(v['depth']/1000)
    )
    csv += ','
    csv += str(int(xpo(v)))
    return csv
