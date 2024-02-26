from itertools import zip_longest
import time
import shlex
import subprocess
import shutil
import os
import linecache
from subprocess import *
from change import *

# class Networks:
#     def __init__(self, netFile, tripFile):
#         self.netFile = netFile
#         self.tripFile = tripFile
cgap = '1e-6'
maxiter = '100'
maxrtime = '60'
batches = '2'
trips = ['SiouxFalls_class1.txt', 'SiouxFalls_class2.txt']
netFile = 'SiouxFalls_net.txt'
termcrit = 1

print(netFile)


def tapb_write(cgap, maxiter, maxrtime, batches, trips, netFile):
    '''write tui file to be read by tap-b'''
    path = './net'
    name = 'params.txt'
    full = os.path.join(path, name)
    with open(full, 'w') as f:
        f.write('<NETWORK FILE> ')
        f.write(netFile)
        f.write('\n')
        if isinstance(trips, str) is False:
            for item in trips:
                f.write('<TRIPS FILE> ')
                f.write(item)
                f.write('\n')
        else:
            f.write('<TRIPS FILE> ')
            f.write(trips)
            f.write('\n')
        f.write('\n')              
        f.write('<NUMBER OF BATCHES> ')
        f.write(batches)
        f.write('\n')
        if termcrit == 1:
            f.write('<CONVERGENCE GAP> ')
            f.write(cgap)
            f.write('\n')
            f.write('~<MAX ITERATIONS> ')
            f.write(maxiter)
            f.write('\n')
            f.write('~<MAX RUN TIME> ')
            f.write(maxrtime)
            f.write('\n')
        elif termcrit == 2:
            f.write('~<CONVERGENCE GAP> ')
            f.write(cgap)
            f.write('\n')
            f.write('<MAX ITERATIONS> ')
            f.write(maxiter)
            f.write('\n')
            f.write('~<MAX RUN TIME> ')
            f.write(maxrtime)
            f.write('\n')
        else:
            f.write('~<CONVERGENCE GAP> ')
            f.write(cgap)
            f.write('\n')
            f.write('~<MAX ITERATIONS> ')
            f.write(maxiter)
            f.write('\n')
            f.write('<MAX RUN TIME> ')
            f.write(maxrtime)
            f.write('\n')

tapb_write(cgap, maxiter, maxrtime, batches, trips, netFile)

#filepath = './bin/tap net/params.txt'
# foundDelta = False

# while foundDelta == False:
st = time.time()
subprocess.call('./bin/tap net/params.txt', shell = True)
tstt = 0
totalCost = 0   
linkCost = 0
tolled = False


with open('./flows.txt', 'r') as f:
    # i = 0
    tolledLinks = 0
    for line in f:
        link = ''
        #print(line.strip(), type(line))  
        data = line.split()
        tstt += float(data[1]) * float(data[2])
        for n in range(1, len(data[0]) - 1):
            link = link + data[0][n]
        link = link.split(',')
        link = list(map(int, link))
        common = set(link) & set(nodes)
        if link[1] in nodes and link[0] not in nodes:
            tolled = True
        # tolled = all(val in nodes for val in link)
        # print(link,tolled, link[1])
        if tolled:
            linkCost = float(data[1]) * (float(data[2]) + float(tfvalue) * float(toll))
            totalCost += float(data[1]) * (float(data[2]) + float(tfvalue) * float(toll))
            tolledLinks += 1
            # print(linkCost)
        else:
            linkCost = float(data[1]) * float(data[2])
            totalCost += float(data[1]) * float(data[2])
            # print(linkCost)
        tolled = False
        # print(data[0][1], data[0], len(data[0]))
        # print(type(data[0]))
        # print(type(data[0]), data)
        # i += 1
        # if i == 32:
        #     break
et = time.time()
tollCost = totalCost - tstt
elapsed = et - st
print(tolledLinks)
print('Elapsed time is:', elapsed)
print('TSTT (time):', tstt)
# print('TSTT (cost):', totalCost)
# print('Cost due to tolls is:', tollCost)

#resetting net file
shutil.copyfile('/workspaces/tap-b/net/SiouxFalls_net.txt', '/workspaces/tap-b/net/test_net.txt')
