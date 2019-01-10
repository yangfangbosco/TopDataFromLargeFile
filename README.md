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

### Verify Your Downloading
If you download all the code and data correctly, run the python code.py with default setting. You should see the following result:
[('158.com', 2745), ('425.com', 2721), ('239.com', 2712), ('830.com', 2706), ('296.com', 2700), ('55.com', 2700), ('170.com', 2697), ('524.com', 2697), ('377.com', 2694), ('248.com', 2688), ('353.com', 2685), ('735.com', 2679), ('544.com', 2676), ('306.com', 2673), ('642.com', 2670), ('897.com', 2667), ('347.com', 2667), ('494.com', 2667), ('737.com', 2661), ('120.com', 2661), ('733.com', 2658), ('608.com', 2658), ('918.com', 2658), ('119.com', 2658), ('252.com', 2658), ('753.com', 2652), ('470.com', 2652), ('311.com', 2649), ('769.com', 2646), ('844.com', 2643), ('684.com', 2643), ('358.com', 2643), ('691.com', 2640), ('825.com', 2640), ('498.com', 2634), ('971.com', 2634), ('226.com', 2631), ('337.com', 2631), ('973.com', 2628), ('71.com', 2628), ('442.com', 2628), ('338.com', 2625), ('670.com', 2625), ('423.com', 2622), ('448.com', 2619), ('587.com', 2619), ('289.com', 2616), ('233.com', 2616), ('145.com', 2616), ('114.com', 2613), ('571.com', 2610), ('398.com', 2610), ('113.com', 2610), ('387.com', 2607), ('110.com', 2607), ('886.com', 2607), ('401.com', 2607), ('185.com', 2607), ('243.com', 2604), ('181.com', 2604), ('667.com', 2604), ('913.com', 2604), ('414.com', 2604), ('319.com', 2604), ('331.com', 2604), ('389.com', 2601), ('644.com', 2601), ('520.com', 2598), ('591.com', 2598), ('722.com', 2598), ('527.com', 2598), ('990.com', 2598), ('435.com', 2598), ('117.com', 2595), ('240.com', 2595), ('209.com', 2595), ('75.com', 2592), ('997.com', 2592), ('200.com', 2592), ('937.com', 2589), ('803.com', 2589), ('488.com', 2589), ('427.com', 2589), ('935.com', 2586), ('687.com', 2586), ('466.com', 2586), ('109.com', 2586), ('716.com', 2586), ('461.com', 2586), ('171.com', 2583), ('194.com', 2583), ('551.com', 2583), ('561.com', 2583), ('880.com', 2583), ('447.com', 2583), ('283.com', 2583), ('142.com', 2583), ('453.com', 2583), ('567.com', 2583), ('269.com', 2583)]
test done, take 10.562938928604126

