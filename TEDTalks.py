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

#################################       MAIN METHOD     #################################
# Find which topics are the most popular
from collections import Counter     #Collections is a module which contains the 'counter' tool used to provide tallied of items
tagsList = listTags()
most_common_topics = [word for word, word_count in Counter(tagsList).most_common(3)]
print(f"The most popular themes are {most_common_topics}")


# Make list of speakers
def list_of_speakers():
    data = readData()

    speakerList = []

    for row in data:
        speaker = row['main_speaker']
        speakerList.append(speaker)
    return(speakerList)

# Make list of URLs
def list_of_URLs():
    data = readData()

    urlList = []

    for row in data:
        url = row['url']
        urlList.append(url)
    return(urlList)

#################################       MAIN METHOD     #################################
# Make a dictionary of speakers & urls as key value pairs
def choose_your_talk():
    speakerList = list_of_speakers()
    urlList = list_of_URLs()
    chosen_speaker = input("Which speaker do you want to listen to?")

    speakerURL = dict(zip(speakerList, urlList))
    print(speakerURL[chosen_speaker])

choose_your_talk()


# Make list of view numbers
def list_of_views():
    data = readData()

    viewsList = []

    for row in data:
        views = row['views']
        viewsList.append(views)
    return(viewsList)


# Make a dictionary of number of views & urls as key value pairs - note could have got index of comment and used this to find URL
def most_viewed_talks():
    viewsList = list_of_views()
    urlList = list_of_URLs()
    viewsURL = dict(zip(viewsList, urlList))

    chosen_rank = input("Which video do you want to see from the top three rankings? Please enter first, second or third")

    if chosen_rank == 'first':
        high = max(viewsList)
        print(viewsURL[high])
    elif chosen_rank == 'second':
        high = max(viewsList)
        viewsList.remove(high)
        second = max(viewsList)
        print(viewsURL[second])
    elif chosen_rank == 'third':
        high = max(viewsList)
        viewsList.remove(high)
        second = max(viewsList)
        viewsList.remove(second)
        third = max(viewsList)
        print(viewsURL[third])
    else:
        print("Error. Was expecting first, second or third")

most_viewed_talks()

# View ted talk durations over 2000 seconds

duration = input('enter ted talks duration')
longtime = float(duration) >= 2000

print('This is a long talk: {}'.format(longtime))

