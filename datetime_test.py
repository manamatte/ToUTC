# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import unittest        #for tests run
#from datetime import datetime        #for datetime manage
import datetime
import os              #for file extension
from pytz import timezone
#import pytz
# Here's our "unit".
def IsOdd(n):
    return n % 2 == 1

class timeline:
    def __init__(self,string):
        #self.string = string 
        self.datetime = datetime.datetime.strptime('13Sep0002', '%d%b%Y')
        self.strings = string

    def split(self,separator):
        self.strings = self.string.split(separator)
        
def StringToUTCToString(string_in,timeformat,in_timezone,out_timezone='UTC'):
        a_datetime = datetime.datetime.strptime(string_in , timeformat)
        in_tz = timezone(in_timezone)
        out_tz = timezone(out_timezone)
        loc_dt = in_tz.localize(a_datetime)
        return out_tz.normalize(loc_dt.astimezone(out_tz)).strftime(timeformat)
        
def ParseDatesToUTC(filepath,column,separator,timeformat,in_timezone,out_timezone='UTC'):
       #self.failIf(IsOdd(4))
        #a = datetime.datetime.strptime('13Sep0002', '%d%b%Y')#,in_timezone)
        #a.tzinfo = 
        print("loading file:", filepath)
        #write line by line
        #array = []
        filename, file_extension = os.path.splitext(filepath)
        out_filepath = filename + '_ToUTC'+ file_extension
        
        out_file = open(out_filepath,"w")
        out_file.write('!! ToUTC run: ' + in_timezone + '->' + out_timezone + '!! ToUTC !!'+'\r\n')
        
        with open(filepath, "r") as ins:
           
           n_lines_try_fails = 0
           column = column-1 # from column number to index
           
           for line in ins:
              tl = line.split(separator)
              n = len(tl)
              
              if n == 1: #header single column
                  out_line = line
                  
              else:
    
                  out_line = ''
                  if n < column:
                      #header less column then datetime one or missing datetime column                  
                      out_line = line
                  else:
                    if column == 0:
                      #out_line = out_line + tl[0] #god for testing but not lately when ifn ==0 etc..
                      try:
                          #isoformat remind d.isoformat()  '2002-03-11'
                          a_datetime_st = StringToUTCToString(tl[column],timeformat,in_timezone,out_timezone)
                          out_line =  out_line + a_datetime_st
                      except ValueError:
                          out_line = out_line + tl[column] 
                          print("Line not modified to UTC: //", line,"//",ValueError.args)
                          n_lines_try_fails = n_lines_try_fails +1;
                      
                      for i in range(column+1,n):
                          out_line = out_line + separator + tl[i]
                        
                    else:
                
                      out_line = out_line + tl[0] 
                      for i in range(1,column): #if n ==0?
                          out_line = out_line + separator + tl[i] 
                      #parse datetime    tl[column]
                      try:
                          #isoformat remind d.isoformat()  '2002-03-11'
                          a_datetime_st = StringToUTCToString(tl[column],timeformat,in_timezone,out_timezone)
                          out_line = out_line + separator +  a_datetime_st
                      except ValueError:
                          out_line = out_line + separator + tl[column] 
                          print("Line not modified to UTC: //", line,"//",ValueError.args)
                          n_lines_try_fails = n_lines_try_fails +1;
                      
                      for i in range(column+1,n):
                          out_line = out_line + separator + tl[i] 
                      
              #end if       
              out_file.write(out_line)
              #splitted = []
              #splitted.append(array(array.count).split(separator))
              
           #for timelineg in array:
              #print(line[1:3])
              #print(timelineg.strings(1))
        #write in the file
        
        
        
        out_file.close()
        ##
        print("written file:", out_filepath)
        #read and write all
        #in_file = open("test.txt","r")
       # text = in_file.read()
       # in_file.close()

        #print(text)
        ##
        
        
           
        
        #print(a)
        #print("nonno",separator,"nonna")
        #print(a)
        return True
        quit
        
def ParseDatesToUTC2(filepath,column,separator,timeformat,in_timezone,out_timezone='UTC'):
       #self.failIf(IsOdd(4))
        #a = datetime.datetime.strptime('13Sep0002', '%d%b%Y')#,in_timezone)
        #a.tzinfo = 
        print("loading file:", filepath)
        #write line by line
        #array = []
        filename, file_extension = os.path.splitext(filepath)
        out_filepath = filename + '_ToUTC'+ file_extension
        
        out_file = open(out_filepath,"w")
        
        
        with open(filepath, "r") as ins:
           
           n_lines_try_fails = 0
           column = column-1 # from column number to index
           
           for line in ins:
              tl = line.split(separator)
              n = len(tl)
              
              if n == 1: #header single column
                  out_line = line
                  
              else:
    
                  out_line = ''
                  if n < column:
                      #header less column then datetime one or missing datetime column                  
                      out_line = line
                  else:
                    if column == 0:
                      #out_line = out_line + tl[0] #god for testing but not lately when ifn ==0 etc..
                      try:
                          #isoformat remind d.isoformat()  '2002-03-11'
                      
                          in_str = tl[column] + separator + tl[column+1]
                          a_datetime_st = StringToUTCToString(in_str,timeformat,in_timezone,out_timezone)
                          out_line =  out_line + a_datetime_st
                      except ValueError:
                          out_line = out_line + tl[column] + separator + tl[column+1]
                          print("Line not modified to UTC: //", line,"//",ValueError.args)
                          n_lines_try_fails = n_lines_try_fails +1;
                      
                      for i in range(column+2,n):
                          out_line = out_line + separator + tl[i]
                        
                    else:
                
                      out_line = out_line + tl[0] 
                      for i in range(1,column): #if n ==0?
                          out_line = out_line + separator + tl[i] 
                      #parse datetime    tl[column]
                      try:
                          #isoformat remind d.isoformat()  '2002-03-11'
                          in_str = tl[column] + separator + tl[column+1]
                          a_datetime_st = StringToUTCToString(in_str,timeformat,in_timezone,out_timezone)
                          out_line = out_line + separator +  a_datetime_st
                      except ValueError:
                          out_line = out_line + separator + tl[column] + separator + tl[column+1]
                          print("Line not modified to UTC: //", line,"//",ValueError.args)
                          n_lines_try_fails = n_lines_try_fails +1;
                      
                      for i in range(column+2,n):
                          out_line = out_line + separator + tl[i] 
                      
              #end if       
              out_file.write(out_line)
              #splitted = []
              #splitted.append(array(array.count).split(separator))
              
           #for timelineg in array:
              #print(line[1:3])
              #print(timelineg.strings(1))
        #write in the file
        
        
        
        out_file.close()
        ##
        
        #read and write all
        #in_file = open("test.txt","r")
       # text = in_file.read()
       # in_file.close()

        #print(text)
        ##
        
        
           
        
        #print(a)
        #print("nonno",separator,"nonna")
        #print(a)
        return True
        quit
# Here's our "unit tests".
class IsOddTests(unittest.TestCase):
    #todo get list of time zones and format description
    def testOne2(self):
        #define variables
        #timeformat = '%d-%b-%Y'
        timeformat = "%d/%m/%Y,%H:%M"
        in_timezone = 'CET' # CET
        filepath = r"C:\...csv"
        column = 3
        separator = ','
        
        bol = ParseDatesToUTC2(filepath,column, separator,timeformat,in_timezone)
        
        self.assertTrue(bol)
    
    
    def testOne(self):
        #define variables
        #timeformat = '%d-%b-%Y'
        timeformat = "%d/%m/%Y %H:%M"
        in_timezone = 'CET' # CET
        filepath = r"C:\..._k.csv"
        column = 3
        separator = ','
        
        bol = ParseDatesToUTC(filepath,column, separator,timeformat,in_timezone)
        
        self.assertTrue(bol)
    
    def testTwo(self):
        #define variables
        #timeformat = '%d-%b-%Y'
        timeformat = "%Y-%m-%d %H:%M"
        in_timezone = 'CET' # CET
        filepath = r"C:\...txt"
        column = 1
        separator = '\t'
        
        bol = ParseDatesToUTC(filepath,column, separator,timeformat,in_timezone)
        
        self.assertTrue(bol)
        
    def testdata(self):
        a = datetime.datetime.strptime('16Sep2012', '%d%b%Y')
        
        print(a)
        
        self.assertFalse(IsOdd(4))
        
        
def main():
    unittest.main()

if __name__ == '__main__':
    main()