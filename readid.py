#!/C:\Python27

                                            
    
import sys
import re

#1056400800272
class CaluteId(object):
    def __init__(self):				     	
        self.carton =  None
        self.__str_data = []

    def id_to_8id(self, data):      
        s = format(int(data[8:]) , 'x')
        s=''.join((s[0:2],'-',s[2:4],'-',s[4:6],'-', s[6:8],'\n')).upper()        
        return s
	    
    def read_web_data(self, carton):
        
        import urllib
        import json
        self.carton = carton
        url = ''.join(('http://42.159.27.52:7900/hs.him.v2/PdaService_2_0/QueryEslInfoByCartonNo.action?CartonNo=C',carton))
        u = urllib.urlopen(url)
        self.__str_data = u.read()
        u.close()
        self.__str_data = json.loads(self.__str_data)
	    
    def carton_id(self):                    
        return (eslid["EslCode"] for eslid in self.__str_data["executionData"])
            
    def block_id(self,iterator):
        for data in iterator:
            for lst in re.findall('\d{18}', data):
                yield lst
        
	
    def read_file(self, filename):
        with open(filename, 'r') as f:
            for eachline in f.readlines():
                yield eachline

    def write_id_file(self, iterator, wfilename):
        lst = []
        with open(wfilename, 'w') as fw:
            for lst_element in iterator:
                #print lst_element,
                if lst_element not in lst: 
                    fw.write(lst_element)
                    lst.append(lst_element)													           


idtext = CaluteId()
##idtext.read_web_data('1056400800272')
##cid = (idtext.id_to_8id(data) for data in idtext.carton_id())
##filename = ''.join(("8id",idtext.__carton,".txt"))
##idtext.write_id_file(cid, filename)

if len(sys.argv) == 1:
    filename=raw_input("Input carton No.:")
    
    idtext.read_web_data(filename)
    cid = (idtext.id_to_8id(data) for data in idtext.carton_id())
    filename = ''.join(("8id",filename,".txt"))
    idtext.write_id_file(cid, filename)
   
elif len(sys.argv) == 2:
    if sys.argv[1] is '--help':
        print('ha')
    else:
        print('haha')
elif len(sys.argv) == 3:
    if (sys.argv[1].upper() == '-C'):        
        idtext.read_web_data(sys.argv[2])
        cid = (idtext.id_to_8id(data) for data in idtext.carton_id())
        filename = ''.join(("8id",idtext.carton,".txt"))
        idtext.write_id_file(cid, filename)
    elif sys.argv[1].upper() == '-BT':
        bid = (idtext.id_to_8id(x) for x in idtext.block_id(idtext.read_file(sys.argv[2])))
        idtext.write_id_file(bid, '8id.txt')
    elif ((sys.argv[1].upper() == '-CT') or (sys.argv[1].upper() == '-TC')):
        for catronnumber in idtext.read_file(sys.argv[2]):
            idtext.read_web_data(catronnumber)
            cid = (idtext.id_to_8id(data) for data in idtext.carton_id())
            filename = ''.join(("8id",catronnumber.strip('\n'),".txt"))
            idtext.write_id_file(cid, filename)         	      
else:
    print('try %s --help for more information' % sys.argv[0].split('\\')[-1])	
