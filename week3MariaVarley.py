import socket
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
mysock.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    #print data;


    #dataDict = {}    

data = data.split("\n")
for line in data:
    print line;
#if(re.findall('Content-Type: ([a-z/sa-z]+)', line)):
#		dataDict["Content-Type"] = content;
#		print content
#length =  re.findall('Content-Length: ([0-9]+)', line);
#if length: 
#		dataDict["Content-Length"] = length; 
#ereg = re.findall('ETag: "([0-9a-z-0-9a-z]+)', line);
#if ereg:
#		dataDict["EReg"] = ereg;
    #content.extend(re.findall('Content-Type: ([a-z/sa-z]+)', line));
    #content.extend(re.findall('Content-Length: ([0-9]+)', line));
    #content.extend(re.findall('ETag: "([0-9a-z-0-9a-z]+)', line));
    #print content
#print dataDict    	
mysock.close()