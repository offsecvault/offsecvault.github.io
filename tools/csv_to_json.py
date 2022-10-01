#!/bin/python3

import pandas as pd
import csv,json

data = pd.read_csv("path/to/file")
print(data)
print("Converted JSON File: ")
print(json.dumps(list(csv.reader(open('path/to/file'))))
