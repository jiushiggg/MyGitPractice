import sys
import datetime
import re

if len(sys.argv) < 2:
    filename=raw_input("input file name:")
else:
    filename=sys.argv[1]

##with open(filename, 'r') as f, open('serial_print_hb.txt', 'w') as fw:
##    for eachline in f:
##        if (eachline[15:17] != 'F0'):
##            continue
##        eachline = ''.join((eachline[25:27], '-', eachline[27:29], '-', eachline[29:31], '-', eachline[31:33], ' ', eachline[0:14],'\n'))
##        fw.write(eachline)

id_list=[]

headers=['id', 'number']
rows=[

]

with open('id.txt', 'r') as f:
    for eachline in f:
        id_list.append(eachline)

with open('total.csv', 'rb') as totalf:
    for test_id in id_list:
        id_name = ''.join((test_id[0:2], test_id[3:5],test_id[6:8],test_id[9:11]))
    #    print id_name
        
        output_filename = ''.join((filename.replace(".txt", ""), 'output.txt'))
        with open(filename, 'r') as f, open(output_filename, 'a')as fw:
            second_list=[]
            i=0     
            for eachline in f:     
                match = re.search(id_name, eachline)
                if match is None:
                    continue
                eachline = match.string 
    #            print eachline
                
                myseconds = datetime.timedelta(hours=int(eachline[1:3]), minutes=int(eachline[4:6]), seconds=int(eachline[7:9])).total_seconds()        
                second_list.append(myseconds)
                if (1 == len(second_list)):
                    myseconds=0
                else:
                    myseconds=second_list[i]-second_list[i-1]
    #            print eachline
                eachline = ''.join((eachline[21:23], '-', eachline[23:25], '-', eachline[25:27], '-', eachline[27:29], ' ', eachline[0:10], ' ', str(myseconds),'\n'))
                fw.write(eachline)
                i += 1
    #        print second_list
            eachline = '\n'
            fw.write(eachline)

        f_csv=csv.writer(totalf)
        f_csv.writerow(headers)
        f_csv.writerows(rows)
        


    










    
