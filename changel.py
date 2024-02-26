import os
tripFile = "./net/test_trips2.txt"
hi = ['1','12','13','14','15','19','20','21','22','23','24']
low = ['2','3','4','5','6','7','8','9','10','11','16','17','18']
hifactor = .2665
lowfactor = .647
new = False
h = False
l = False
odflow = 0
#change the OD matrix for each origin
with open(tripFile,'r') as f:
#read lines containing tolled nodes
    lines = f.readlines()
    data = []

    n = 0
    for i, line in enumerate(lines):
        if line.startswith('<', 0, 1) or line.startswith('~', 0, 1):
            continue
        if line.startswith('Origin', 0, 6):
            ldata = line.split()
            # print(ldata)
            if ldata[1] in hi:
                h = True
            if ldata[1] in low:
                l = True
            # print(h, l)    
            ldata.append('\n')
            data.append(ldata)
            
        if line.startswith(' ', 0, 1) and h is True:
            ldata = line.split()
            for x in range(2, len(ldata), 3):
                ldata[x] = ldata[x][:-1]
                ldata[x] = str(float(ldata[x]) * hifactor)
                odflow += float(ldata[x])
                ldata[x] = ldata[x] + "; "
            # print(ldata)
            n += 1
            ldata.append('\n')
            data.append(ldata)
        if line.startswith(' ', 0, 1) and l is True:
            ldata = line.split()
            for x in range(2, len(ldata), 3):
                ldata[x] = ldata[x][:-1]
                ldata[x] = str(float(ldata[x]) * lowfactor)
                odflow += float(ldata[x])
                ldata[x] = ldata[x] + "; "
            # print(ldata)
            n += 1
            ldata.append('\n')
            data.append(ldata)
        if n == 5:
            h = False
            l = False
            n = 0
        # lines[i] = ' '.join(map(str,data))
    lines = list(map(' '.join, data))
    # print(data)
    # print(lines)
    # print(odflow)

    # print(lines, data, len(data))
with open(tripFile, 'w') as f:
    for line in lines:
        if line.startswith('<', 0, 1) or line.startswith('~', 0, 1):
            continue
        f.write(line)
