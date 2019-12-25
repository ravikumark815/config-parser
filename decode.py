#!/usr/bin/python

import sys
import base64

if len(sys.argv)!=3:
    print("\nUsage:\n\tpython decode.py <exp file path> <result file path>\n")

else:
    with open(sys.argv[1], 'r') as f:
        rawData = f.readline()
    f.close()

    finalData = base64.b64decode(rawData)
    finalData =  finalData.split("&")

    with open(sys.argv[2], 'w+') as f:
        for i in finalData:
            f.writelines(str(i) + "\n")
    print("\nEXP Decoded Successfully\n")
    f.close()