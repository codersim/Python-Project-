import statistics
import math
import csv

# Read the data from csv file
def readData():
    data = []

    with open('ted_main.csv', 'r') as durationData:
        spreadsheet = csv.DictReader(durationData)
        for row in spreadsheet:
            data.append(row)
    return(data)

# Make a list of the durations for each talk
def listConverter():
    data = readData()

    durationList = []

    for row in data:
        duration = row['duration']
        durationList.append(duration)
    return(durationList)

# Convert the list of string durations into int durations
def intData():
    intDuration = []
    durationList = listConverter()

    for duration in durationList:
        intDuration.append(int(duration))
    return(intDuration)


# Calculate the mean duration
def meanData():

    intDuration = intData()

    mean = statistics.mean(intDuration)
    meanMinutes = round(mean/60, 1)
    print(f"Optimum duration is {meanMinutes} mintues")

#################################       MAIN METHOD     #################################
meanData()

# Make a list of the tags for each talk
def listTags():
    data = readData()

    tagsList = []

    for row in data:
        tags = row['tags']
        tagsList.append(tags)
    return(tagsList)

# Make a dictionary of comments & tags as key value pairs
def dictMaker():
    intDuration = intData()
    tagsList = listTags()

    commentsTags = dict(zip(intDuration, tagsList))
    print(commentsTags[1286])

dictMaker()



