import time
import shlex
import subprocess
import shutil

class Networks:
    def __init__(self, netFile, tripFile):
        self.netFile = netFile
        self.tripFile = tripFile

cgap = float(input('Provide convergence gap: '))
maxiter = int(input('Provide maximum number of iterations: '))
maxrtime = int(input('Provide maximum run time: '))
batches = int(input('Provide number of batches: '))
tripFile = []

if batches > 1:
    while len(tripFile) < batches:
        file = input('Provide trip file: ') + '.txt'
        tripFile.append(file)
else:
    file = input('Provide trip file: ') + '.txt'
    tripFile.append(file)

netFile = input('Provide network file: ') + '.txt'


def tapb_write(cgap, maxiter, maxrtime, batches, tripFile, netFile):
    '''write tui file to be read by tap-b'''
    with open('params_txt', 'w') as f:
        f.write('<NETWORK FILE> ')
        f.write(netFile)
        f.write('/n')
        if type(tripFile) == list:
            for item in tripFile:
                f.write('<TRIPS FILE> ')
                f.write(item)
                f.write('/n')
                f.write('<NUMBER OF BATCHES> ')
                f.write('batches')
                f.write('/n')
        else:
            f.write('<TRIPS FILE> ')
            f.write('trips.txt')
            f.write('/n')
        f.write('<CONVERGENCE GAP> ')
        f.write('cgap')
        f.write('/n')
        f.write('<MAX ITERATIONS> ')
        f.write('maxiter')
        f.write('/n')
        f.write('<MAX RUN TIME> ')
        f.write('maxrtime')
        f.write('/n')

def uesolver():
    location = 'tap-b/bin/tap net/'
    start = time.time()
    tapb_write(cgap, maxiter, maxrtime, batches, tripFile, netFile)
    args = shlex.split(location + 'params.txt')
    elapsed = time.time() - start

    return elapsed

print(uesolver(), )


        
        

