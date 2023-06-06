
import pandas as pd
import json
from pandas import json_normalize

a=open("parameters.json","r")
read_json = a.read()
load_json = json.loads(read_json)

print(type(load_json))
print(load_json)

# print(data_param)
