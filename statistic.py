import matplotlib.pyplot as plot
import os

#

#plot.plot([3,2,1])
#plot.show()

def makeReport(name, date, price, instable, incoin, avg, coin):
    
    plot.plot(price, ls = "--", lw = 2, alpha = 0.3)
    plot.plot(instable, c = "g", ls = "-", lw = 1, alpha = 0.6)
    plot.plot(incoin, c = "r", ls = "-", lw = 1, alpha = 0.6)
    plot.plot(avg, c = "gold", ls = "-", lw = 1, alpha = 0.9)
    plot.grid(True)
    plot.show()
#

def normalizator(list):

    return [(x - min(list))/(max(list) - min(list)) for x in list]
#

def makeStatistic(name, log):
    
    f = open(log, "r").readlines()

    dates = []
    prices = []
    instables = []
    incoins = []
    inavgs = []
    coins = []

    for l in f:
        
        row = l.split("|")

        dates.append(row[0].split(" ")[0])
        prices.append(float(row[1]))
        instables.append(float(row[2]))
        incoins.append(float(row[4]))
        inavgs.append((instables[-1] + incoins[-1])/2)
        coins.append(float(row[3]))
    #

    makeReport(name, dates, normalizator(prices), normalizator(instables), normalizator(incoins), normalizator(inavgs), normalizator(coins))
#

path = "D:\\Project\\Seeker\\result\\balanceLT\\BNBUSDT\\"

for file in os.listdir(path):

    name = file
    target = "{}{}".format(path, file)
    
    makeStatistic(name, target)
#