# -*- coding: utf-8 -*-

import json

d = {
    "a": "a",
    "b": 1
}

print(d)
print("")
z = json.dumps(d, sort_keys=True, indent=4, separators=(',', ': '))
z_compact = json.dumps(d, sort_keys=True, separators=(',', ': '))
print(z)
print(z_compact)
