#!C:\Python27\python.exe
# encoding: utf-8
import time
import re
import sys
import os 
import xmlrpclib
import random

server = xmlrpclib.ServerProxy("http://127.0.0.1:9000")




def follow(thefile):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

#def update(n, esl_list, multi_packet=True):
def update(n, esl_list, multi_packet=False):
    price = random.randint(1, 1000)
    print '----------update times:%d' % n
    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),
    
    if multi_packet ==False:      
        test_template = "MPD_eslid"
        print 'update price:%d '% (price),
    else:
        if n%2 == 0:            
            test_template = 'ManymanyNumber_E31_250122213-BLACK-WHITE'            
        else:
            test_template = 'MPD_eslid'
            print 'update price:%d '% (price),
    print test_template            
            
    for line in esl_list:
        server.send_cmd("ESL_UPDATE", [{
            "eslid": line.strip(), 
            "template": test_template,
            "sid":"2345",
            "itemName": "小苹果",
            "Price": price,
            "discount": "-20",
            "hotline": "投诉电话:12358",
            "skuCode": "1234567890",
            "productDate": "1488527366954",
            "productTime": "1488527366954",
            "producer": "北京",
            }])	
			
			
update_num = 0
m_total_num = 0.0
m_success_num = 0.0
m_failed_num = 0
file_name = '.\log\eslworking.log'
esl_id_file = '100.txt'

update_num = 0
for index, line in enumerate(open(esl_id_file,'r')):
    update_num += 1
print	update_num


if __name__ == '__main__':
    if  len(sys.argv) < 2:
        filename = esl_id_file
        file_object = open(filename)
    else:
        file_object=sys.argv[1].split(',')

        
    with open(file_name, 'r') as logfile, open('update_time.txt', 'a') as fw:
        loglines = follow(logfile)         
               
        for i in xrange(1000):
            file_object = open(esl_id_file)
            update(i, file_object)

            for eachLine in loglines:
                m_finish = re.search("(esl_update_finished).+(offline|online)", eachLine)                
                if m_finish is not None:
                    m_total_num += 1
                    if m_finish.group(2) == "online":
                        m_success_num += 1
                    elif m_finish.group(2) == "offline":
                        m=re.search('[0-9A-F]{2}-[0-9A-F]{2}-[0-9A-F]{2}-[0-9A-F]{2}', eachLine)
                        print m.group()
                        m_failed_num += 1
                                        
                    continue
                
#                m_time = re.search("heatp_data | detail=", eachLine)
#                if m_time is not None:
#                    fw.write(eachLine)
						
                if update_num == m_total_num:
                    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) ,  \
                        'update finish total:%d, success:%d, failed:%d, success rate:%.4f' %  \
                        (m_total_num, m_success_num, m_failed_num, m_success_num/m_total_num)
                    m_total_num = 0.0
                    m_success_num = 0.0
                    m_failed_num = 0                    
                    break
                    
            file_object.close()
#            time.sleep(180)

