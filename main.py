import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("./110/data.csv")
data = df["temp"].tolist()
fig = ff.create_distplot([data], ["temp"], show_hist=False)
fig.show()
print("population mean:- ",statistics.mean(data))
print("population stddev:- ",statistics.stdev(data))


def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    print("sampling mean:- ", statistics.mean(mean_list))
    print("sampling stdev:- ", statistics.stdev(mean_list))
setup()
