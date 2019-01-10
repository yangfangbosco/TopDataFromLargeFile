import hashlib
import os
import random
#from memory_profiler import profile
import resource
import operator
import json
import sys
import time

# this function suppose to set limit for this python process, but not able to work
def memory_limit():
  resource.setrlimit(resource.RLIMIT_STACK, (10240, 10240))
  print(resource.getrlimit(resource.RLIMIT_STACK))


# check the size of given file
def check_file_size(filename):
  statinfo = os.stat(filename)
  current_size = statinfo.st_size
  return current_size

# create_sample_data creates a data file with given file name and desired size in bytes. The data file contains random urls.
def create_sample_data(size, filename):
  current_size = 0
  while(current_size < size):
    address = str(random.randint(0, 1000)) + '.com\n'
    datafile = open(filename,"a")
    datafile.write(address)
    datafile.close()
    current_size = check_file_size(filename)
    print(current_size)

# calculate hash value for each url, then take the remain when divided by number of file I want 
def calculate_hash(url, number_of_file):
  hashvalue = int(hashlib.sha1(url.encode('utf-8')).hexdigest(), 16) % (10 ** 8)
  remain = hashvalue % (number_of_file)
  return remain

#@profile
# split_data splits a given file to multiple files based on the given size.
def split_data(size, filename,outputfilename, number_of_file):
# open buffering is set to be the size
  inputfile = open(filename,"r")
  newline = inputfile.readline()
  list_all = [[] for x in range(number_of_file)]
  # total_size is the buffer to read the urls and write one time to files
  total_size = 0
  round = 0
  while(newline != ""):
    url = newline
    newline = inputfile.readline()
    outputfileindex = calculate_hash(url, number_of_file)
    list_all[outputfileindex].append(url)
    # add the total size to ensure the buffer size is limited to 2MB(this is the testing value, please increase this value if you have more memory.)
    total_size += len(url)
    if(total_size > size):
      total_size = 0
      round = round + 1
      print('full - round ' + str(round))
      for i in range(0,number_of_file):
        outputfile = open(outputfilename+str(i), 'a')
        #print('writing ' + str(i))
        for item in list_all[i]:
          outputfile.write(item)
      list_all = [[] for x in range(number_of_file)]
  # add the remaining
  for i in range(0,number_of_file):
        outputfile = open(outputfilename+str(i), 'a')
        #print('writing ' + str(i))
        for item in list_all[i]:
          outputfile.write(item)
  list_all = [[] for x in range(number_of_file)]    
  print("split data done\n")

# process_all_datafile take number of files, create dictonaries for them, and merge dictionary. Finally return the top 100.
def process_all_datafile(outputfilename, number_of_file):
  sum_dict = {}
  for i in range(0, number_of_file):
    filename = outputfilename + str(i)
    single_dict = process_datafile(filename)
    sum_dict = { k: sum_dict.get(k, 0) + single_dict.get(k, 0) for k in set(sum_dict) | set(single_dict)}
  
  sorted_d = sorted(sum_dict.items(), key=operator.itemgetter(1), reverse = True)[:100]
  print(sorted_d)

# process_datafile will read the given file, count the number of time that each url appears, and save them into a file.
def process_datafile(filename):
  print("processing " + filename + "\n")
  data_dict = dict()
  inputfile = open(filename, 'r')
  newline = inputfile.readline().strip()
  while(newline != ""):
    url = newline
    newline = inputfile.readline().strip()
    if(url in data_dict.keys()):
      data_dict[url] += 1
    else:
      data_dict[url] = 1
  return data_dict

def clean_all_temp_file(outputfilename, number_of_file):
  for i in range(0, number_of_file):
    os.remove("outputfile" + str(i))



def find_top100_from_large_file(write_buffer, inputfilename, temp_outputfilename, number_of_file):
  start = time.time()
  split_data(write_buffer, inputfilename, temp_outputfilename, number_of_file)
  process_all_datafile(temp_outputfilename, number_of_file)
  clean_all_temp_file(temp_outputfilename, number_of_file)
  end = time.time()
  print('test done, take '+ str(end-start))

def test_with_20Mdata_1Mbuffer(write_buffer, inputfilename, outputfilename, number_of_file):
  find_top100_from_large_file(write_buffer, inputfilename, outputfilename, number_of_file)

def main():
  test_with_20Mdata_1Mbuffer(2*1024*1024, 'sampledata20m', 'outputfile', 20)
  
  
if __name__== "__main__":
  main()