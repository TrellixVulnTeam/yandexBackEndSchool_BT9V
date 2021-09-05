import json
import copy
from typing import Dict, Any
from datetime import datetime

dataFormat = "%Y-%m-%d %H:%M:%S"
errorList = []
errorExist = 0
with open("input.txt") as inputData:
    t, e = map(int, inputData.readline().split())
    for line in inputData:
        statusLine = line[22:]
        status = statusLine[0:statusLine.index(" ")]
        if status == "ERROR":
            errorList.append(line)
            if len(errorList) == e:
                if e == 1:
                    errorExist = 1
                    break
                lastErrorDate = datetime.timestamp(datetime.strptime(errorList[e-1][1:20], dataFormat))
                for i in range(0, len(errorList)):
                    currentErrorDate = datetime.timestamp(datetime.strptime(errorList[i][1:20], dataFormat))
                    if lastErrorDate - currentErrorDate <= t - 1:
                        break
                errorList = errorList[i:e]
            if len(errorList) == e:
                errorExist = 1
                break

with open("output.txt", "w") as o:
    if errorExist == 1:
        o.write(errorList[e-1][1:20])
    else:
        o.write("-1")