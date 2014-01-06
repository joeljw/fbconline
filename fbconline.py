#!/usr/bin/python

#Import the email modules we'll need
from email.parser import Parser

import os
import sys

rootdir = sys.argv[1]
print "Date,Name,Phone,Email"
with open('fboutput.csv','w') as fo:
 for rootdir, subFolders, files in os.walk(rootdir):
    for file in files:
        filePath = rootdir + '/' + file
        f = open( filePath, 'r')
        headers = Parser().parse(f)
        body = headers.as_string()
        lines = body.split("\n")
        for index, line in enumerate(lines):
#            if "Online:" in line:
#               print lines[index+1]
#               fo.write(lines[index+1]+",")
#               continue
            if "----------------" in line:
               print lines[index+2]
               fo.write(lines[index+2]+",")
               continue
            if "Name:" in line:
               print line
               fo.write(line+",")
               continue
            elif "Email:" in line:
               print line
               fo.write(line+",")
               continue
            elif "Phone:" in line:
               print line
               fo.write(line+"\n")
               break
 f.close()
fo.close()