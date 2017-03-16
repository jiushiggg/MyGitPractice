#!/C:\Python27

import sys
import re


lst=[]

if  len(sys.argv) < 2:
    filename=raw_input("input file name:")
else:
    filename=sys.argv[1]


def id_to_8id(data):
    data = re.findall('\d{18}', data)
    for lst_element in data:
        s = format(int(lst_element[8:]) , 'x')
        s=''.join((s[0:2],'-',s[2:4],'-',s[4:6],'-', s[6:8],'\n')).upper()        
        yield s

    
with open(filename, 'r') as f, open('4id.txt', 'w') as fw:
    for eachline in f:
        for lst_element in id_to_8id(eachline):
            if lst_element not in lst: 
                fw.write(lst_element)
                lst.append(lst_element)





