from itertools import zip_longest
import time
import shlex
import subprocess
import shutil
import os
import linecache
from subprocess import call


class Networks:
    def __init__(self, netFile, tripFile):
        self.netFile = netFile
        self.tripFile = tripFile
cgap = '1e-6'
maxiter = '100'
maxrtime = '60'
batches = '1'
trips = ['No_TransferSiouxFalls_trips.txt']
netFile = 'No_TransferSiouxFalls_net.txt'
termcrit = 1

# print('Braess network is default, is this ok?', '\n', 'y or n')
# newFile = input()
# if newFile == 'n':
#     cgap = input('Provide convergence gap: ')
#     maxiter = input('Provide maximum number of iterations: ')
#     maxrtime = input('Provide maximum run time: ')
#     batches = input('Provide number of batches: ')
#     print('Select termination criteria:','\n', '1 = Convergence Gap','\n', '2 = Maximum Number of Iterations','\n', '3 = Maximum Runtime')
#     trips = []
#     termcrit = int(input())
#     if int(batches) > 1:
#         while len(trips) < int(batches):
#             file = input('Provide trip file: ')
#             trips.append(file)
#     else:
#         file = input('Provide trip file: ')
#         trips.append(file)

#     netFile = input('Provide network file: ')


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
st = time.time()
subprocess.call('./bin/tap net/params.txt', shell = True)
tstt = 0

with open('./flows.txt', 'r') as f:
    i = 0
#for i in range(2):
    for line in f:
        #print(line.strip(), type(line))  
        list = line.split()
        tstt += float(list[1]) * float(list[2])
        # print(list[0][1])
        # print(type(list[0]), list)
        # if i <= 2:
        #     print(tstt)
        # i += 1

            # print(list)
            # i += 1
            # if i == 2:
        #     break
et = time.time()
elapsed = et - st
print('TSTT is:', tstt, 'Elapsed time is:', elapsed)



        
        

