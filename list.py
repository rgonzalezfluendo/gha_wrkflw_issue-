#!/usr/bin/env python3

# Dummy script as example of the issue

import json

OSs = ["windows-latest", "ubuntu-latest"]
nodes = [14, 16]

matrix = []

for os in OSs:
    for node in nodes:
        matrix.append({"os":os, "node": node})


print(json.dumps(matrix))
