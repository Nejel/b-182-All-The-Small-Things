#!/bin/python

import sys
import os



# Complete the function below.

def jobOffers(scores, lowerLimits, upperLimits):
    if len(lowerLimits) != len(upperLimits):
        raise Exception("invalid input")

    resultSize = len(lowerLimits)
    result = [0] * resultSize

    for i in range(resultSize):
        for score in scores:
            if lowerLimits[i] <= score <= upperLimits[i]:
                result[i] += 1

    return result

def readArray():
    size = int(raw_input())
    arr = []
    for i in range(size):
        arr.append(int(raw_input()))
    return arr

print jobOffers(readArray(), readArray(), readArray())

if __name__ == "__main__":
    f = open(os.environ['OUTPUT_PATH'], 'w')
    scores_cnt = 0
    scores_cnt = int(raw_input())
    scores_i = 0
    scores = []
    while scores_i < scores_cnt:
        scores_item = int(raw_input());
        scores.append(scores_item)
        scores_i += 1


    lowerLimits_cnt = 0
    lowerLimits_cnt = int(raw_input())
    lowerLimits_i = 0
    lowerLimits = []
    while lowerLimits_i < lowerLimits_cnt:
        lowerLimits_item = int(raw_input());
        lowerLimits.append(lowerLimits_item)
        lowerLimits_i += 1


    upperLimits_cnt = 0
    upperLimits_cnt = int(raw_input())
    upperLimits_i = 0
    upperLimits = []
    while upperLimits_i < upperLimits_cnt:
        upperLimits_item = int(raw_input());
        upperLimits.append(upperLimits_item)
        upperLimits_i += 1


    res = jobOffers(scores, lowerLimits, upperLimits);
    for res_cur in res:
        f.write( str(res_cur) + "\n" )

    f.close()
