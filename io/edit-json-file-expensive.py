#!/usr/bin/env python3

# Modify JSON file that has a list property.

# Example on how to run:
# chmod 755 io/edit-json-different-filesize.py
# edit-json-different-filesize.py moo

# Sample output:
# sys.argv[0] = ./io/edit-json-file-expensive.py
# sys.argv[1] = moo
# keyword found:
# $['v1', 'v2', 'v3', 'v101', 'v100', 'v1000']
# append v10:
# $['v1', 'v2', 'v3', 'v101', 'v100', 'v1000', 'v10']
#

import json
import os
import sys


keyword=""
for index, argument in enumerate(sys.argv):
    keyword=sys.argv[index]
    print("sys.argv[%d] = %s" % (index, keyword))

offset = 0
with open(file="./sample-input-files/sample.json", mode='r') as file_input \
    , open(file="./sample-input-files/sample.json.out", mode='w', encoding='utf-8') as file_output:

    parsed_json = json.load(file_input)
    if keyword in parsed_json:
        print(f"keyword found:\n${parsed_json[keyword]}")

        if "v10" not in parsed_json[keyword]:
            parsed_json[keyword].append("v10")
            print(f"append v10:\n${parsed_json[keyword]}")

            serialized_json = json.dump(parsed_json, file_output)
            os.rename(src="./sample-input-files/sample.json.out", dst="./sample-input-files/sample.json")
