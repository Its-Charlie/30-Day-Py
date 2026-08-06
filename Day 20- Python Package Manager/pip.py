# using numpy after installing it with pip

'''before running this code, make sure to install numpy using pip:
pip insrtall numpy"'''

import numpy as np
arr = np.array([1,2,3])

print(arr)
print(arr+2)
print(arr*5)

#requst API using requests module after installing it with pip

'''pip install requests'''
import requests

url = "https://api.github.com"

response = requests.get(url)

print(response.status_code)
print(response.text)
print(response.json())