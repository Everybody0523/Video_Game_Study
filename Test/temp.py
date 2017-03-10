# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import statistics
import pandas as pd
data = pd.io.parsers.read_csv("NBTC_Tata_Challenge.01.csv")
#print(data["Developer"])

d = {}
for i in range(0, 16719):
    if not(data["Developer"][i] in d):
        #First Index: Best Sale, Second Index: Worst Sale
        d[data["Developer"][i]] = [data["Global_Sales"][i]]
    else:
        d[data["Developer"][i]].append(data["Global_Sales"][i])
"""
for key in d:
    name = key
    if (len(d[key]) > 2):
        var = statistics.variance(d[key])
    output = "Global Sales Variance of "
    output = output + str(name)
    output = output + " is "
    output = output + str(var)
    print(output)
"""
d_new = {}
#dictory of each company. The first index is best-selling, second index 
#worst-selling, third index is mean, forth index is variance
for key in d:
    if len(d[key]) > 2:
        d_new[key] = [max(d[key]), min(d[key]), statistics.mean(d[key]), 
             statistics.variance(d[key])]

list = []
for key in d_new:
    if (d_new[key][0] > 8) and (d_new[key][1] > 0.533):
        a = d_new[key][3]
        b = d_new[key][2]
        c = d_new[key][1]
        d = d_new[key][0]
        list.append((key, a, b, c, d))


print(list)
#print(data)
