#!/usr/bin/env python3

# Modify the file which may results into larger file or smaller file than the original file size,
# then we can't write to same file while we are reading it. But, says if we only change from
# upper case to lower case, then we can modify the file using the same file descriptor. But, this
# following script is only catering for first case.

# Example on how to run:
# chmod 755 edit-file-different-filesize.py
# edit-file-different-filesize.py v100

# Sample output:
# sys.argv[0] = ./edit.py
# sys.argv[1] = v100
# foo=abcdef
#
# bar=12343-1344378
#
# moo=[v1,v2,v3,v101,v100,v1000]
#
# moo found
# [ =  5 ; ] =  29
# new_line =>  moo=[v1,v2,v3,v101,v100,v1000,v10]
#
# zoo=https://www.twitter.com

import os
import sys

keyword=""
for index, argument in enumerate(sys.argv):
    keyword=sys.argv[index]
    print("sys.argv[%d] = %s" % (index, keyword))

offset = 0
with open(file="./sample.env", mode='r') as file_input \
    , open(file="./sample-output.env", mode='w', encoding='utf-8') as file_output:

    for line in file_input:
        print(line)
        if line.startswith("moo="):
            print("moo found")
            start_indexOf = line.find("[") + 1
            end_indexOf = line.find("]")
            print("[ = ", start_indexOf, "; ] = ", end_indexOf)
            isMatched = line.find("v10,", start_indexOf, end_indexOf) >= 0 \
                or line.find("v10]", start_indexOf, end_indexOf + 1) >= 0

            new_line = ""
            if isMatched == False:
                new_line = line[0:end_indexOf] + ",v10" + line[end_indexOf] + "\n"
                print("new_line => ", new_line)

                file_output.write(new_line)
            else:
                offset = offset + len(line)
                file_output.write(line)
        else:
            offset = offset + len(line)
            file_output.write(line)


os.rename(src="./sample-output.env", dst="./sample-out.env")
