import sys

if len(sys.argv) < 2:
    filename=raw_input("input file name:")
else:
    filename=sys.argv[1]

with open(filename, 'r') as f, open('10id.txt', 'w') as fw:
    for eachline in f:
        eachline = eachline.replace("-", "")
#        print eachline
        digit_10 = int(eachline, 16)
#        print digit_10
        mystr = ''.join((str(digit_10), "\n"))
#        print mystr
        fw.write(mystr)
