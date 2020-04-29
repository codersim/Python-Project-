# 1. Read the data from the spreadsheet
import csv

def readData():
    data = []

    with open('sales.csv', 'r') as salesData:
        spreadsheet = csv.DictReader(salesData)
        for row in spreadsheet:
            data.append(row)
    return(data)


# 2. Collect all of the sales from each month into a single list
def listConverter():
    data = readData()

    salesList = []

    for row in data:
        sales = row['sales']
        salesList.append(sales)
    return(salesList)

# 3. Output the total sales across all months
def totalCount():
    salesList = listConverter()
    count = 0

    for salesAmount in salesList:
        count = count + int(salesAmount)
    print(count)

#################################       MAIN METHOD     #################################
totalCount()

THIS IS A TEST

