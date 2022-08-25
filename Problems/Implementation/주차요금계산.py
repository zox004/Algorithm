from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    park_info = defaultdict(int)
    for record in records:
        time, number, inout = record.split()
        hour, minute = time.split(":")
        time = int(hour)*60 + int(minute)
        if inout=="IN":
            park_info[number] -= time
        else:
            park_info[number] += time
    park_info = sorted(park_info.items())

    for number, time in park_info:
        fee = fees[1]
        if time<=0:
            time += 23*60 + 59
        if time > fees[0]:
            tmp = math.ceil((time-fees[0])/fees[2])
            fee += tmp*fees[3]
        answer.append(fee)
        
    return answer
