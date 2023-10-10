import time
import shlex
import subprocess
import shutil
import os
from subprocess import call


class Networks:
    def __init__(self, netFile, tripFile):
        self.netFile = netFile
        self.tripFile = tripFile

cgap = input('Provide convergence gap: ')
maxiter = input('Provide maximum number of iterations: ')
maxrtime = input('Provide maximum run time: ')
batches = input('Provide number of batches: ')
trips = []

if int(batches) > 1:
    while len(trips) < int(batches):
        file = input('Provide trip file: ')
        trips.append(file)
else:
    file = input('Provide trip file: ')
    trips.append(file)

netFile = input('Provide network file: ')


def tapb_write(cgap, maxiter, maxrtime, batches, tripFile, netFile):
    '''write tui file to be read by tap-b'''
    path = './bin/tap net'
    name = 'params.txt'
    full = os.path.join(path, name)
    with open(full, 'w') as f:
        f.write('<NETWORK FILE> ')
        f.write(netFile)
        f.write('\n')
        for item in trips:
            f.write('<TRIPS FILE> ')
            f.write(item)
            f.write('\n')
        f.write('\n')              
        f.write('<NUMBER OF BATCHES> ')
        f.write(batches)
        f.write('\n')
        f.write('<CONVERGENCE GAP> ')
        f.write(cgap)
        f.write('\n')
        f.write('~<MAX ITERATIONS> ')
        f.write(maxiter)
        f.write('\n')
        f.write('~<MAX RUN TIME> ')
        f.write(maxrtime)
        f.write('\n')

tapb_write(cgap, maxiter, maxrtime, batches, trips, netFile)

# with open('params_txt', 'w') as f:
#     call('./bin/tap/params_txt')
# def uesolver():
#     location = 'tap-b/bin/tap net/'
#     start = time.time()
#     tapb_write(cgap, maxiter, maxrtime, batches, tripFile, netFile)
#     #args = shlex.split(location + 'params.txt')

#     elapsed = time.time() - start

#     return elapsed

# print(uesolver(), tapb_write )


        
        

