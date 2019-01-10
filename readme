# Find the top 100 URL from a 100G file with 1G RAM

### Problem Statement

There is a data file with 100G URL, each URL take one single line. Write a computer program to process this data file with only 1G Ram

### Files

There are 3 important files in this repository:
code.py is the main code file where all the code is located.
sampledata20m is a 20m data file with randomly generated URLs. The URL generator is coded in code.py
sampledata is a 100m data file with randomly generated URLs as well.

### Runing

To run the code, simply clone this repository to your local file system. Run the code.py with python code.py. You can adjust the parameters the change the running time and space.

### Function Explanation
There is two most important function in the code.py that I would like to explain here.
split_data:
  This function split the URLs data to different files based on his hash number. For example, if a hash of a URL is 212221, and we decided to use 200 files to save all the data,
  it will be stored in file number 21 (212221 % 200 )

process_datafile
  Once the split finished, we will read which file individually and count their occurrence using python dictionary. Then, we merge all the dictionary and find the most popular 100.

### Potential Problem and Improvement

Potential Problem: I didn't add the mechanism to handle the following situation: there is a large number of unique URLs, in the worst case, all URLs are different.
In this case, the dictionary we created in the processing procedure might get larger than the limited memory because there are too many keys in it.

Improvement 1: I need to come up with a mechanism that is able to limit the size of a dictionary. For example, limit the size of the split file and use additional files to store remaining URLs with the same hash. Then run K-way merge.
However, it might cause another problem that one URL are stored in different files and when we save them to different dictionaries, the count is also split. We need another process to combine 
the count from the different dictionary while the memory is limited.

Improvement 2: Another way to solve the problem above was store data URL count into files instead of using a dictionary only. In the current implementation, I loaded all the URLs into the dictionary which might use more than limited memory. However, if I set a threshold for the size of the dictionary, and once the size reaches the threshold, all data and their count in the dictionary can be stored in a file. THen I can empty the dictionary and load more data. Later on, when I move the data to the file again, I can read the file line by line to see if the newly added data already have some count in the file. If yes, then update the count by adding a new count.
Else, then add the new data to the file. With this implementation, we will not need to worry about the dictionary size.

Improvement 3: When combining the dictionaries, I loaded all dictionaries from all split file. Then sort and find the top 10. In fact, a min heap can help with it so I don't have to load all data into the memory together. 
I haven't implemented this part due the limited time.

