import os
import time
# importing logging
import logging
i1 = input("Input the URL: ")
url = i1 
response = os.system("ping -c 1 " + url)

#and then check the response...
if response == 0:
  print(url, 'is up!'.n)
else:
  print(url, 'is down!')
start = time.time()

qc = input("Take your time to waste time for run time ok? ")
end = time.time()
final = end - start
z = round(final, 2)
print(z, "seconds was the run time")
#using logging to select the text file for output and what the log is. 
logging.basicConfig(filename='sample.txt', format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info(url)

with open ('sample.txt', 'rt') as myfile:
    contents = myfile.read()
print(contents)