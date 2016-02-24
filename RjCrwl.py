
import zlib
# from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup

__author__ = 'rajasyedabuthahir.j'
import sys
# sys.stdout = open('iamarks.txt', 'w')
import httplib, urllib
reg_no_start=711312104053
reg_no_end=711312104103
while(reg_no_start<=reg_no_end):

       params = urllib.urlencode({'regno': reg_no_start})
       headers = {"Host": "coe1.annauniv.edu",
       "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0",
       "Accept": "text/plain, */*; q=0.01",
       "Accept-Language": "en-US,en;q=0.5",
       "Accept-Encoding": "gzip, deflate",
       "Content-Type": "application/x-www-form-urlencoded",
       "Authorization": "Basic ZW1zYXU6IUJlc3RHdW5AIzIwMTMh",
       "Referer": "http://sdpdr.nic.in/annauniv/result",
       "Content-Length": "18",
       "Origin": "http://sdpdr.nic.in",
       "Connection": "keep-alive"
       }
       conn = httplib.HTTPConnection("coe1.annauniv.edu")
       conn.request("POST", "/app/app_action/annauniv_iamark.php", params, headers)
       response = conn.getresponse()
       print response.length


       decompressed_data=zlib.decompress(response.read(), 16+zlib.MAX_WBITS)

       soup = BeautifulSoup(decompressed_data,"html.parser")
       if not soup.nexttonextresponse is None:
           print ("--------------------------------------------------------------"+"\n"
                  "NOV/DEC 2015 EXAMS REGISTER_NUMBER-" +str(reg_no_start) +"\n"+
                  soup.nexttonextresponse.findAll('response')[0]['value1'] + "\t"+
                  soup.nexttonextresponse.findAll('response')[0]['value2']+ "\t"+
                     soup.nexttonextresponse.findAll('response')[0]['value3']+ "\n"+
                  soup.nexttonextresponse.findAll('response')[1]['value1']+ "\t"+
                  soup.nexttonextresponse.findAll('response')[1]['value2']+ "\t"+
                  soup.nexttonextresponse.findAll('response')[0]['value3']+ "\n"+
                  soup.nexttonextresponse.findAll('response')[2]['value1']+ "\t"+
                  soup.nexttonextresponse.findAll('response')[2]['value2']+ "\t"+
                  soup.nexttonextresponse.findAll('response')[0]['value3']+ "\n"+
                  soup.nexttonextresponse.findAll('response')[3]['value1']+ "\t"+
                  soup.nexttonextresponse.findAll('response')[3]['value2']+ "\t"+
                  soup.nexttonextresponse.findAll('response')[0]['value3']+ "\n"+
                  soup.nexttonextresponse.findAll('response')[4]['value1']+ "\t"+
                  soup.nexttonextresponse.findAll('response')[4]['value2']+ "\t"+
                  soup.nexttonextresponse.findAll('response')[0]['value3']+ "\n"+
                  soup.nexttonextresponse.findAll('response')[5]['value1']+ "\t"+
                  soup.nexttonextresponse.findAll('response')[5]['value2']+ "\t"+
                  soup.nexttonextresponse.findAll('response')[0]['value3']+ "\n"+
                  soup.nexttonextresponse.findAll('response')[6]['value1']+ "\t"+
                  soup.nexttonextresponse.findAll('response')[6]['value2']+ "\t"+
                  soup.nexttonextresponse.findAll('response')[0]['value3']+ "\n"+
                  soup.nexttonextresponse.findAll('response')[7]['value1']+ "\t"+
                  soup.nexttonextresponse.findAll('response')[7]['value2']+ "\t"+
                  soup.nexttonextresponse.findAll('response')[0]['value3']+ "\n"+
                  "--------------------------------------------------------------"
                  )
       # conn.close()

       reg_no_start+=1
