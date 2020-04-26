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

# Make a list of the comments for each talk
def listComments():
    data = readData()

    commentsList = []

    for row in data:
        comments = row['comments']
        commentsList.append(comments)
    return(commentsList)

# Convert the list of string durations into int durations
def intComments():
    intComments = []
    commentsList = listComments()

    for comments in commentsList:
        intComments.append(int(comments))
    return(intComments)


# Make a dictionary of comments & tags as key value pairs
def dictMaker():
    commentsList = intComments()
    tagsList = listTags()

    commentsTags = dict(zip(commentsList, tagsList))
    maxDiscussion = commentsTags[max(commentsList)]
    print(f"The topics which initiates the most discussion are {maxDiscussion}")

dictMaker()



