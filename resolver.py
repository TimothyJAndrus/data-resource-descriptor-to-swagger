from prance import ResolvingParser
import json


parser = ResolvingParser('swag.json')
swag = parser.specification  # contains fully resolved specs as a dict

open('resolved.json', 'w').close()
with open('resolved.json', 'w') as outfile:
    json.dump(swag, outfile, indent=4)
