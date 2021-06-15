import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("./110/110data.csv")
data = df["temp"].tolist()
mean = sum(data) / len(data)

fig = ff.create_distplot([data], ["whole data -temp"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean],y=[0,1], mode="lines", name="MEAN"))
fig.show()

print("Mean of the whole data:- ",statistics.mean(data))
print("Std-deviation of the whole data:- ",statistics.stdev(data))
#________________________________________________________________

#Taking 10 random samples from the whole data(ex:counter=10)
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
        #dataset is the list containing 10 random samples from the whole data
    mean_10_samples = statistics.mean(dataset)
    std_deviation_10_samples=statistics.stdev(dataset)

    fig = ff.create_distplot([dataset], ["mean_10_samples- temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean_10_samples, mean_10_samples],y=[0,1], mode="lines", name="MEAN"))
    fig.show()
    #print("Mean of 10 random Sample :- ",mean_10_samples)
    #print("std_deviation of 10 random sample:- ",std_deviation_10_samples)
    
    return mean_10_samples
#------------------------------------------------------------------
def show_fig(mean_list_1000):
    df = mean_list_1000
    sampling_mean = sum(mean_list_1000) / len(mean_list_1000)
    fig = ff.create_distplot([df], ["Sampling mean -temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[sampling_mean, sampling_mean],y=[0,1], mode="lines", name="MEAN"))
    fig.show()

def setup():
    mean_list_1000 = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(10)
        mean_list_1000.append(set_of_means)
    show_fig(mean_list_1000)
    print("sampling mean :- ", statistics.mean(mean_list_1000))
    print("sampling std_deviation:- ", statistics.stdev(mean_list_1000))
setup()
