from datetime import datetime
from matplotlib import pyplot as plt
import statistics

today_time = datetime.now()
file1 = open("/Users/paulinelymorgan/git/python/estudo_forex/data/DAT_MT_AUDUSD_M1_2018.csv", "r")
file2 = open("/Users/paulinelymorgan/git/python/estudo_forex/data/DAT_MT_EURUSD_M1_2018.csv", "r")
data_AUDUSD_M1_2018 = file1.read()
data_EURUSD_M1_2018 = file2.read()

class Bar(object):
    def __init__(self, arr):
        
        self.bar_date = arr[0] # date
        self.bar_hour = arr[1] # hour
        self.lixo = arr[6] # lixo

        # OHLC
        self.bar_o = float(arr[2]) # open
        self.bar_h = float(arr[3]) # high
        self.bar_l = float(arr[4]) # low
        self.bar_c = float(arr[5]) # close
        
    
    def getDate(self):
        return self.bar_date
    def getHour(self):
        return self.bar_hour
    def getOpen(self):
        return self.bar_o
    def getHigh(self):
        return self.bar_h
    def getLow(self):
        return self.bar_l
    def getClose(self):
        return self.bar_c
    def getLixo(self):
        return self.lixo

    def getId(self):
        return self.getDate()+self.getHour()

def loadBars(readFile):

    arr = []
    lines = readFile.split('\n')
    lines.pop()
   
    for line in lines:
        arr.append(Bar(line.split(',')))

    return arr

def getFormattedDate(bar):
    temp = bar.getDate().replace('.', '-')+" "+bar.getHour().split(':')[0]+":"+bar.getHour().split(':')[1]
    temp = datetime.strptime(temp, "%Y-%m-%d %H:%M")

    return temp

def getCorrelation(arr_x, arr_y):
    
    axios_y = []
    axios_x = []

    control = 0

    for arr1 in arr_x:
        # control = 0
        while(True):
            if (today_time - getFormattedDate(arr1)) > (today_time - getFormattedDate(arr_y[control])):
                break

            if arr1.getId() == arr_y[control].getId():
                axios_y.append(arr1.getClose()/arr_y[control].getClose())
                axios_x.append(arr1.getId())
                break
            control += 1

    return axios_x, axios_y

def correlationBetweenTwo(a, b):

    """
        verificacao necessária, pois há barras faltando (haverá comparação entre data e hora). 
        verifica qual par tem a primeira barra com data mais antiga. dai usa o par como laço externo.
    """
    # d1 = datetime.strptime(a[0].getDate().replace('.', '-')+" "+a[0].getHour().split(':')[0]+":"+a[0].getHour().split(':')[1], "%Y-%m-%d %H:%M")
    # d2 = datetime.strptime(b[0].getDate().replace('.', '-')+" "+b[0].getHour().split(':')[0]+":"+b[0].getHour().split(':')[1], "%Y-%m-%d %H:%M")
    diff1 = today_time - getFormattedDate(a[0])
    diff2 = today_time - getFormattedDate(b[0])

    if diff1 > diff2:
        # começa por a (diff1)
        return getCorrelation(a, b)
    else:
        # começa por b (diff2)
        # diff2 maior ou diff2 = diff1
        return getCorrelation(b, a)


bars_AUDUSD_M1_2018 = loadBars(data_AUDUSD_M1_2018)
bars_EURUSD_M1_2018 = loadBars(data_EURUSD_M1_2018)
x,y = correlationBetweenTwo(bars_AUDUSD_M1_2018, bars_EURUSD_M1_2018)

print("bars quantity: {}".format(len(y)))
print("mean: {}".format(statistics.mean(y)))
print("stdev: {}".format(statistics.stdev(y)))

plt.plot(x, y)
plt.xlabel("Bars: {}".format(len(y)))
plt.ylabel("Correlation")
plt.title("Mean: {}".format(statistics.mean(y)))
plt.show()


