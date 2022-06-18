# -*- coding: utf-8 -*-
"""
Created on Sat May 28 22:26:11 2022

@author: Samitha Patabendige
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


Tlen = 100 # length of the ts

# random values from normal dists
T_norm = pd.Series(np.random.normal(size=Tlen))
#print(T_norm)

# sine wave ts
# Generating time data using arange function from numpy
time = np.arange(0, (Tlen/3)*np.pi, 1)
# Finding amplitude at each time
amplitude = np.sin(time)
T_sine = pd.Series(data=amplitude, index=time)
#print(T_sine)

# discord added sine
min_pos = 70
max_pos = 80
T_sine_discorded = pd.Series(data=[T_sine[t]-np.random.uniform() if (t<max_pos) & (t>min_pos) else T_sine[t] for t in time],index=time)

fig,ax = plt.subplots()
plot_ts = T_sine_discorded
sns.lineplot(data=plot_ts,x=plot_ts.index,y=plot_ts.values)






#dist = euclidean_distances(a, a)


#trivial impl of discord
T = T_sine_discorded.copy(deep=True)
T.reset_index(drop=True,inplace=True)


def brute_force_discord_detection(T=T, n=20): 
    best_so_far_dist = 0
    best_so_far_loc = np.nan
    
    for p in range(1,len(T)-n+1):
        #print("p : ",p)
        nearest_neighbour_dist = np.Infinity
        for q in range(1,len(T)-n+1):
            if abs(p-q)>=n:
                #print("p seq : ",(T[p:(p+n-1)].values))
                dist_p_q = np.linalg.norm(T[p:(p+n-1)].values-T[q:(q+n-1)].values)#euclidean_distances(T[p:(p+n)],T[q:(q+n-1)])
                #print("dist_p_q : ",dist_p_q)
                if dist_p_q < nearest_neighbour_dist:
                    nearest_neighbour_dist = dist_p_q
                    #print('nearest_neighbour_dist : ',nearest_neighbour_dist)
                    
        if nearest_neighbour_dist > best_so_far_dist:
                best_so_far_dist = nearest_neighbour_dist
                best_so_far_loc = p
                #print("so far best discord location : ", p, "so far best discord distance : ", best_so_far_dist)
                
    return best_so_far_dist, best_so_far_loc


discord_dist, discord_loc = brute_force_discord_detection(T_sine_discorded,n=10)

print('Final discord_dist : ',discord_dist, 'Final discord_loc : ',discord_loc)




n=20

ts_def_one = T[0:discord_loc+1]
ts_disc = T[discord_loc:(discord_loc+n+2)]
ts_def_two = T[(discord_loc+n+1)::]
annotated_series = [{'ids':1, 'vals':ts_def_one,'cols':'b'},\
                    {'ids':2, 'vals':ts_disc,'cols':'r'},\
                        {'ids':3, 'vals':ts_def_two,'cols':'b'}]
    
fig,ax = plt.subplots()
plt.plot(annotated_series[0]['vals'],color=annotated_series[0]['cols'])
plt.plot(annotated_series[1]['vals'],color=annotated_series[1]['cols'])
plt.plot(annotated_series[2]['vals'],color=annotated_series[2]['cols'])

