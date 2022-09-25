# Generated by Django 4.1 on 2022-09-24 17:10

from django.db import migrations

name='Sending a package'

def challenge(apps, schema_editor):
    Challenge = apps.get_model('server', 'Challenge')
    chall = Challenge(
        name=name,
        priority=40,
        minimal_version="0.1.0",
        validator="lpb_delivery",
        description="""# Let's send some packages!

## Introduction

Well played with the introduction part!
You are now fully equiped to face a real world like challenge!

## Lore

You are a young startup company, La Poste Banquale, aiming to create an improved way to send packages across the world.
Clients are dropping off packages to you and, using a state of the start AI, you select the best provider to ship it.

As shipping is a really tense market, none of the provider explain how the price of sending a package is calculated.
Fortunately, providers expose the past price of packages in function of several parameter they choose.

## Goal

For this challenge, you will have to train an model using the algorithm of your choice to select the best provider to ship packages.
And by the best, you understand the cheapest one.
To train your model, you will have to download, prepare the raw data of every provider.

You will train your model and save the result during the container build.
At runtime, you will only load this result.
To help you a little bit, here is an example on how to save and load your model.

```
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import fetch_openml
import pickle

ml = fetch_openml(name='diabetes', version=1)
X = ml.data
Y = ml.target
test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)
# Fit the model on training set
model = LogisticRegression()
model.fit(X_train, Y_train)
# save the model to disk
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))

# some time later...

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, Y_test)
print(result)
```

With your trained model, you will expose the endpoint `/lpb/delivery`.
It will receive one thousand call with various argument, like described just after.
You will have to respond with the correct provider at least 96% of the time to validate this challenge.

### Payload example

```
{
  "length": 12, # in mm
  "width": 14, # in mm
  "depth": 16, # in mm
  "volume": 2688, # in mm3
  "color": "blue", # between blue, green, red, yellow, orange, purple
  "scotch_taped": true, # or false
  "fragile": false, # or true
  "assurance_price": 12, # in euros
  "weight": 12, # in g
  "express": false, # or true
  "signature_required": false, # or true
  "destination_type": "mailbox" # or "parcel-relay-point"
}
```

### Response example

```
{
  "selected_provider": "tnt" # between: tnt, ups, dpd, fedex, dhl, xpo
}
```

### Providers data

* [tnt](/static/provider_tnt.txt)
* [ups](/static/provider_ups.txt)
* [dpd](/static/provider_dpd.txt)
* [fedex](/static/provider_fedex.txt)
* [dhl](/static/provider_dhl.txt)
* [xpo](/static/provider_xpo.txt)

""",
    )
    chall.save()

def reverse_challenge(apps, schema_editor):
    Challenge = apps.get_model('server', 'Challenge')
    challs = Challenge.objects.filter(name=name)
    for chall in challs:
        chall.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('server', '0030_challenge_prio_30'),
    ]

    operations = [
        migrations.RunPython(challenge, reverse_challenge)
    ]