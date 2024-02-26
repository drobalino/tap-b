import os
cordon = True
tripFile = "./net/test_trips.txt"
net1 = "./net/test_net.txt"
nodes = [10,11,14,15,22,23]
toll = '1'
tfvalue = '4.16'
tollf ='<TOLL FACTOR> ' + tfvalue +'\n'

with open(tripFile, 'r') as f:
#create list of lines
    lines = f.readlines()
    data = []
    found = True
    # print(lines)
    for i, line in enumerate(lines):
        ldata = line.split()
        data.append(ldata)
        if '<TOLL FACTOR>' in line:
            break
        if line.startswith('END', 1, 4):
            found = False
            lines.insert(len(data)-1, tollf)
            break
#     # print(found)
#     # print(lines)

#add toll factor parameter
if found == False:
    with open(tripFile, 'w') as f:
        for line in lines:
            f.write(line)
    f.close()

#changing toll on net file
with open(net1,'r') as f:
#read lines containing tolled nodes
    lines = f.readlines()
    data = []
    for i, line in enumerate(lines):
        if line.startswith('<', 0, 1) or line.startswith('~', 0, 1):
            continue
        else:
            data = line.split()
        # print(line, type(line), len(line))
        #CHANGES TO TOLL IN net FILE
        if len(data) > 0 and data[0] not in map(str,nodes) and data[1] in map(str,nodes):
            data = line.split()
            data[-3] = data[-3].replace(data[-3], toll)
            # print(data)
            data.append('\n')
            data.insert(0,'')
            lines[i] = ' '.join(map(str,data))
        #WEIRD TOLL CASE    
        # if len(data) > 0:
        #     if data[0] in map(str,nodes) or data[1] in map(str,nodes):     
        #         data = line.split()
        #         data[-3] = data[-3].replace(data[-3], toll)
        #         # print(data)
        #         data.append('\n')
        #         data.insert(0,'')
        #         lines[i] = ' '.join(map(str,data))
        # print(data)
        # print(line)
    # print(lines)
# modify file
with open(net1, 'w') as f:
    for line in lines:
         f.write(line)