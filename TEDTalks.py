import statistics
import math
import csv

def readData():
    data = []

    with open('ted_main.csv', 'r') as durationData:
        spreadsheet = csv.DictReader(durationData)
        for row in spreadsheet:
            data.append(row)
    return(data)


def listConverter():
    data = readData()

    durationList = []

    for row in data:
        sales = row['duration']
        durationList.append(sales)
    return(durationList)

def meanData():
    intDuration = []
    durationList = listConverter()

    for duration in durationList:
        intDuration.append(int(duration))
    print(intDuration)

    mean = statistics.mean(intDuration)
    meanMinutes = round(mean/60, 1)
    print(f"Optimum duration is {meanMinutes} mintues")

meanData()



