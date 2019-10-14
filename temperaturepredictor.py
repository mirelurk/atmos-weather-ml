import LinearRegression as linreg

import csv              #used in data importing
import datetime         #used in data cleaning
import string           #used in data cleaning

import matplotlib                   #used in graphing
import matplotlib.pyplot as plt     #used in graphing

import numpy as np

#DATA RETRIEVE

training_set = []

with open('HoustonTemp.csv', newline='\n') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')
    for row in datareader:
        newset = [row[1], row[2]]
        training_set.append(newset)

csvfile.close()


#DATA CLEANING

def pullOutNumbers(s):
    #Pull the numbers from a list and return joined string
    num = []
    for j in s:
        try:
            j = int(j)
            num.append(j)
        except ValueError:
            break
    try:
        num = ''.join(num)
    except TypeError:
        for i in range(len(num)):
            num[i] = str(i)
        num = ''.join(num)
    return(num)

def dataCleaning():
    #Working with the training_set[]

    #Remove Titles
    training_set.pop(0)

    #Change all T's and gaps in i[1] to floats
    correctedCount = 0
    for i in training_set:
        if i[1]=='T' or i[1]=='':
            i[1] = float(0)
            correctedCount+=1
        else:
            num = pullOutNumbers(i[1])
            i[1] = float(num)
    print(correctedCount)
    

    #Change datetime to a value of 1-365 based on what day of the year data
    #was collected on.
    for i in training_set:
        datalist = list(i[0])
        datalist[10] = ' '
        date = ''.join(datalist[:10])
        
        #WHOLE DATE START
        dateformat = datetime.datetime.strptime(date, '%Y-%m-%d')
        newdate = datetime.date(dateformat.year, dateformat.month,
                                dateformat.day)
        testdate = datetime.date(dateformat.year, 1, 1)
        calcdate = str(newdate - testdate)
        calcdate = list(calcdate)
        numdays = pullOutNumbers(calcdate)
        
        try:
            days = float(''.join(numdays))
        except ValueError:
            days = 1.0
        
        #HOUR DECIMAL START
        timehour = datalist[11:13]
        timehour = int(''.join(timehour))
        hours = round(timehour/24, 2) #final decimal value
        total = days + hours
        i[0] = float(total)
          
dataCleaning()

#TRAINING

defaultInst = linreg.RegressionAlg() #an instance kept with default values
instance = linreg.RegressionAlg()
instance.train(training_set)

def printValues():
    print('{} sin({}x - {}) + {}'.format(instance.a, instance.b, instance.c,
                                         instance.d))

#GRAPHING

def overlayScatter():
    #Scatter plot of training data
    x = []
    y = []
    for i in training_set:
        x.append(i[0])
        y.append(i[1])

    #Pull inputs from training instance
    t = np.arange(1, 365)
    s = instance.a*np.sin(instance.b*t-instance.c)+instance.d
    
    #Graphing
    fig, sct = plt.subplots()
    sct.scatter(x, y, marker="|")
    sct.plot(t, s)

    plt.show()

def zoomScatter():
    #Scatter plot of training data
    x = []
    y = []
    for i in training_set:
        x.append(i[0])
        y.append(i[1])

    #Pull inputs from training instance
    t = np.arange(1, 365)
    s = instance.a*np.sin(instance.b*t-instance.c)+instance.d
    
    #Graphing
    fig, sct = plt.subplots()
    sct.scatter(x, y, marker="|")
    sct.plot(t, s)
    sct.set_xlim([0,100])
    sct.set_ylim([-50, 100])

    plt.show()

printValues()
overlayScatter()
zoomScatter()

