# BIS634_qz258
## Fall 2021 BIS634, NetID: qz258, Name: Olina (Qiuyu) Zhu 

This is the HW2 folder within repository for BIS634 during Fall 2021, completed by Olina (Qiuyu) Zhu, NetID: qz258. 

Jupyter Notebook file cells should be ran in order from top to down or click 'Run All' to ensure proper execution of code logic. 

The pdf version of all code output is in HW2_console_qz258 file. 

Note that the data file for Q2 is too large to be uploaded, hence should anyone try to run the code in Q2, please do so locally with a downloaded file. 

References:
https://medium.com/@robertopreste/from-xml-to-pandas-dataframes-9292980b1c1c 
https://docs.python.org/3/library/xml.etree.elementtree.html 

# Q1:
The histogram is shown in the console_HW2_qz258 pdf file in the folder. 

No patient share the exact same age (i.e., non-rounded ages). This is shown by using the .duplicated() method on the column "full_age", and finding whether any value of true was returned. If not, then there are no duplicated exact ages. 

Bonus: Should any two patients share the exact same age, then the sorting problem would be affected. For example, if there were many duplicated ages, then the algorithm identifying n-th oldest person would take a redundantly long time to run. Also, bisection method used to locate values would be incorrect and would need extra steps to correct. Specifically, in a dataset where the high_age value is found but is duplicated at adjacent lower indices, then it is possible that those with high_age values would also be counted to the result when they shouldn't be, as the algorithm simply does an index-subtraction of 1 from the index of high_age found to signify the right end of the list of ages in range, but in this case the value at high_index - 1 is still equal to high_age and should not be included in the count. An example erronous call with duplicate ages would be: num_patients_in_age_range[0, 0, 2, 3, 4, 5, 5, 5, 5], 2, 5). This problem could be resolved by adding a step like: while list[high_index-1] == list[high_index]: high_index -= 1. 

Provider encoded gender as female, male, and unknown. This was seen was the data was grouped by the "gender" variable and the three corresponding rows showed all the categories used to encode gender. 

The oldest patient is 84.99855742449432 years old with name Monica Caponera. 

The function is implemented and shown in the console_HW2_qz258 file. The code is reproduced below: 

```
def find_second_oldest(list):
    oldest = 0
    second_oldest = 0
    for i in list:
       if i > oldest: oldest = i
       elif i > second_oldest: second_oldest = i
    return second_oldest
    
print("Second oldest is", find_second_oldest(df['full_age']))
```

Output: Second oldest is 84.9982928781625 


This method trades off between time and space efficiency, where any n-th oldest person in list for n < length of list, a new variable called n-th_oldest is created to store that information and itself and any m-th_oldest variable for m < n is updated when necessary. 

This is advantageous to use when one is looking for extreme values, i.e. searching for people in the 95% percentile in sorted ages, because a reasonable number of variables would be created and maintained. However, when one were to look for more centered values, such as the median age, then this method is very inefficient and it would be better to just use the regular sorting algorithm that runs in O(nlogn) time. 

James Robertson is 41.5 years old. 

There are 150677 people who are at least 41.5 years old in the dataset. 

O(logn) function that returns number of patients who's age is within range (low_age, high_age) and relevant tests are shown in the Q2.jypn file as well as the console_HW2_qz258 file. 

The modified funcion that returns number of patients in age range and the number of males in range and relevant tests are shown in the Q2.jypn file as well as the console_HW2_qz258 file. Note that an issue encountered here is in the base case, when the condition len(lst) == 0 or condition lst[len(lst) - 1] < low_age is reached. The program seemed to continue executing following code even after calling exit(0), exit(1), or quit(). Therefore, the sys.exit() function was called to force the program to end and produce results. 


# Q2: 
Data URL: https://www.dropbox.com/s/0nj725q0avgimd4/GCA_000001405.28_GRCh38.p13_genomic.fna?dl=0 

There are 240548031 15-mers that have less than two 'N's on chromosome 2 in the dataset. 

There are 144698064 unique 15-mers on chromosome 2, as estimated using hashes. The simple tests and relevant datasets are in console_HW2_qz258 file slight edits in pdf file that are not in oringal console but does not affect output) reproduced below: 

data_1 = "abcdefghijklmnopqabcdefghijklmno"

data_2 = "ctagctagctagctagctagcccccccccccc"

data_3 = "acacacacacacacacacacacacacacacac"


test 1: Correct answer should be 17

Observed answer is 17 

test 2: Correct answer should be 15

Observed answer is 15 


test 3: Correct answer should be 2

Observed answer is 2 


test 4: trying algorithm on chromosome 2

144698064

*Note: For this problem, I understand that the approximate counting code is probably wrong. I did not quite understand the materials in slides on the topic, and simply used scale = 30 as 1 billion seubsequences is approximately 2^30. But this does not sound right because the probability of clashes is simply too high at about 50%. Could we please go over the implementation of this problem in class? The explanation on the slides is understandable by logic (incrementing exponent increase) but difficult to implement into actual problems for me. Thank you! 


# Q3: 
Problem with friend's solution: After going through some online research, I found that there could be several issues with the friend's running of the program. 
	I. MemoryError typically means running out of RAM, and though her data is 4GB but the RAM is 8GB, it could still run out. This is because some overhead or background activity on her computer maybe taking up RAM, or she should use a 64-bit computer instead of a 32-bit one which allows more memory as not all memory provided by RAMs are usable memory. 
	II. Repeated access to RAM could cause overload, as the continuous access of RAM could occur at at rate that exceeds the DRAM refresh rate. 
	III. When expanding a list and not pre-allocating memory, the system needs to make a copy of the current list, which takes up additional memory that may not be apparent to the user as this process occurs implicitly. 
	IV. The issue may not be due to running out of RAM space, but due to limited CPU capacity. A process running on a single core may not be able to handle so much input, hence even if there are free RAM space, the operating system throws a MemoryError. 

Sources: 
https://support.microsoft.com/en-us/topic/the-usable-memory-may-be-less-than-the-installed-memory-on-windows-7-based-computers-3d194dc3-39b9-fae7-74d8-59931b53d2c2
https://www.mathworks.com/matlabcentral/answers/406845-out-of-memory-error 
https://www.pythonpool.com/python-memory-error/ 
https://www.memtest86.com/troubleshooting.htm 

Suggested storage method: The friend could try to run all the data through a hash function and simple store a hash table, therefore duplicate values are not going to take up additional space and would be stored in a standardized format that has a reasonable trade-off between accuracy and space. Alternatively, she could try to pre-allocate a large chunk of memory for this calculation which would avoid failures in memory allocation.  

Suggested calculation strategy: Instead of sotring all the data, the friend could have two variables, sum and count, the former stores the running total of weights and the latter stores how many weights there are, which then could allow her to do a simple sum/count calculation to compute the average weight. This only requires space to be reserved for some overhead, the weight read on every "for line in f" which is updated hence does not need storing throughout the entire for-loop, a float for sum, and an integer for count. 


# Q4: 
The dataset is called "Accidental_Drug_Related_Deaths_2012-2020", published by data.ct.gov, and could be found at https://catalog.data.gov/dataset/accidental-drug-related-deaths-2012-2018. No license information was available, but Data.gov specified that the data source was public and that "This dataset is intended for public access and use". There were no restrictions on use found, and no applications were needed to access data, however on several other related datasets that I visited, it was noted that users should only use data for statistical analyses purposes and not try to identify individual responders. 

The variables are explicitly specified and no additional readings (e.g., codebooks) were needed to undertsand the dataset. No variable was derivable from another variable, but statistical predictions could be made after some data wrangling. For example, I plotted the number of deaths due to accidental drug usage by age and gender, and it was clear that males had significantly higher counts than females from ages 20 to 70. The overall age trend of accidental drug-related deaths also followed more closely to that of the males than the females. Therefore, it seems that simply by looking at the age of an individual, one could predict that the individual is likely a male rather than a female if they are within the age range. Moreover, one could substitute age for drug type to predict the gender of an individual who died from a certain drug. Similarly, gender could be subsituted by race for an analysis between race and drug type/age. 

Some analyses that one cannot do with this dataset is whether underlying health conditions contributed to the deaths, as this column was left mostly blank and minimal meaningful analyses could be done. Also, the dataset only showed age at death but not drug use duration, frequency, or intensity, which does now allow a more detailed analysis on the effects of these variables on likelihood of accidental death due to drug usage. 

The data was downloaded as a CSV file and loaded into a Pandas Dataframe. There are 7679 rows in the dataset and 28 variables (originally 42, but some redunant variables were removed). Some basic descriptions are provided in the Q4 and console_HW2_qz258 files. 

I believe this dataset is interesting because of the legalization of marijuana use in NYC this year, and in many other states previously. Although marijuana is said to be not able to cause OD, it is a gateway drug and could lead to use of harder drugs. Therefore, I was interested in examining date on deaths related to accidental drug use, which is more likely related to leisure drug use rather than prescription drugs as the latter tend to have stricter regulations on access and presribed dosage. 

