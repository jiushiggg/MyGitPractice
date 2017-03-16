#!/C:\Python27

import os


voltage = {0:'26',1:'27',2:'28',3:'29',4:'30',5:'31',6:'32',7:'33'}

output = os.popen('grep "500B63EE" hb.txt | grep  "F0[0-9A-F]\{30\}"').read().split('\n')

for eachline in output:
    if len(eachline) > 6:
        eachline = ' '.join((eachline,voltage[int(eachline[-5], 16)&0x07]))
        print eachline



