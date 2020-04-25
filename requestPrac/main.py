import requests
import html
import csv
from contextlib import closing
import matplotlib.pyplot as plt


def derivative(x,y,start,end):
    y_prime = []
    prevX = start
    prevY = end
    for i in range(0,len(x)):
        delta_x = x[i] - prevX
        delta_y = y[i] - prevY
        if (delta_x == 0):
            delta_x = 1
        y_prime.append(delta_y/delta_x)
        prevX = x[i]
        prevY = y[i]
    return y_prime

def getCountryData(country):
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

    with closing(requests.get(url, stream=True)) as r:
        f = (line.decode('utf-8') for line in r.iter_lines())
        reader = csv.reader(f, delimiter=',', quotechar='"')
        data = []
        first = True
        for row in reader:
            if first == True:
                data.append(row)
                first = False
            if row[0] == country:
                data.append(row)
        return data

def plotData(Data):
    plt.plot([day for day in range(0,Data["days"])], Data["data"])  
    plt.title(Data["title"])  
    # naming the x axis 
    plt.xlabel(Data["xlabel"]) 
    # naming the y axis 
    plt.ylabel(Data["ylabel"])    


    # function to show the plot 
    plt.show() 
  

def main():
    USA = getCountryData("USA")
    my_total_cases = 0
    total = 0
    NC_indx = None
    TC_indx = None
    TC_data = []
    NC_data = []
    days = -1
    for row in USA:
        days += 1
        if row == USA[0]:
            for col in row:
                if col == "new_cases":
                    NC_indx = row.index(col)
                if col == "total_cases":
                    TC_indx = row.index(col)
        else:
            TC_data.append(int(row[TC_indx]))
            NC_data.append(int(row[NC_indx]))
            my_total_cases += int(row[NC_indx])
    TC_dict = {
                "days": days,
                "data": TC_data,
                "title": 'Number of total cases',
                "xlabel": 'days since Dec 31, 2019',
                "ylabel": 'Total cases'}
    plotData(TC_dict)
    NC_dict = {
                "days": days,
                "data": NC_data,
                "title": 'New Cases Each Day',
                "xlabel": 'days since Dec 31, 2019',
                "ylabel": 'New cases'}

    plotData(NC_dict)
    Deriv_dict = {
                "days": days,
                "data": derivative([day for day in range(0,days)],TC_data,0,0),
                "title": 'Derivative of total cases',
                "xlabel": 'days since Dec 31, 2019',
                "ylabel": 'Derivative'}

    plotData(Deriv_dict)

    Sec_Deriv_dict = {
                "days": days,
                "data": derivative([day for day in range(0,days)],Deriv_dict["data"],0,0),
                "title": '2nd Derivative of total cases',
                "xlabel": 'days since Dec 31, 2019',
                "ylabel": '2nd Derivative'}

    plotData(Sec_Deriv_dict)

  


if __name__ == "__main__":
    main()