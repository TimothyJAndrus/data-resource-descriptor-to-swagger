from convert_descriptor_to_swagger import convert_descriptor_to_swagger
import json
from glob import glob


descriptors = []
desc_folder = 'descriptors/'

for f_name in glob(f'{desc_folder}/*.json'):
    with open(f_name, 'r') as f:
        desc = json.load(f)
    
    descriptors.append(desc)

swagger = convert_descriptor_to_swagger(descriptors)

# print(json.dumps(swagger, indent=4))

# wipe file
open('swag.json', 'w').close()
with open('swag.json', 'w') as outfile:
    json.dump(swagger, outfile)
