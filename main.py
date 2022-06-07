# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv


import matplotlib.pyplot as plt



def plot():
    # Use a breakpoint in the code line below to debug your script.
    x = []
    y = []

    with open('rates.csv', 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            x.append(row[0])
            y.append(int(row[1]))

    plt.plot(x, y, color='g', linestyle='dashed',
             marker='o', label="hourly arrival rates")

    plt.xticks(rotation=25)
    plt.xlabel('Day hour')
    plt.ylabel('Hourly arrivals')
    plt.title('Hourly arrival rate Taxi Ride dataset, March 1 2011 ', fontsize=20)
    plt.grid()
    plt.legend()
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    plot()

