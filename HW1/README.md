# BIS634_qz258
## Fall 2021 BIS634, NetID: qz258, Name: Olina (Qiuyu) Zhu 

This is the HW1 folder within repository for BIS634 during Fall 2021, completed by Olina (Qiuyu) Zhu, NetID: qz258. 

The file 'Execerise 1' is a Python 3 (.py) file and all other exercises are Jupyter Notebook (.jpynb) files. For Exercises 2, 3, and 4, one should run the cells in order from top to down or click 'Run All' to ensure proper execution of code logic. 

The pdf version of all code output is in HW1_console_qz258 file. 

Exercise 1: 
The code was ran with the given test code and all results matched the answer scheme. Additionally, five more tests were added to identify potential errors associated with: 
  1) Order of chicken/human tests (same parameter for two human test after inserting chicken test with the same parameter in between) 
  2) Proximity of parameter value between subsequent chicken and human tests 
  3) Proximity of parameter value between the same kinds of tests 


Exercise 2: 
  1) The columns are: name, age, weight, and eyecolor 
  2) There are 152361 rows in the data 
  3) Distribution of ages: 

    - mean         39.510528 
    - std          24.152760 
    - min          0.000748 
    - 25%          19.296458 
    - 50%          38.468955 
    - 75%          57.623245 
    - max          99.991547 

  4) Histogram generated by code. Pasting into readme file did not work. The number of bins in the histogram decides how many separate columns there will be and what the range of age represented by each column is. For example, for a dataset with x-axis range of 0-100, setting the bin number to 10 will generate 10 separate columns each representing a range of 10 years, whereas setting to 20 will generate 20 different columns each representing a range of 5 years. 20 bins were chosen for the age plot because the variation in age does not necessarily need to follow any pattern, therefore 20 bins would give a more detailed visualization of the age distribution. On the other hand, 15 bins were chosen for the weight plot, because it is highly unlikely for a large proportion of the data points to be accumulated on the ends of the plot (<10 kilos and >90 kilos), and weight tends to increase with age, therefore being able to predict a pattern in distribution encouraged the use of larger bin-widths to obtain a general idea of the main peak. 
  5) Distribution of weights: 

    - mean         60.884134 
    - std          18.411824 
    - min          3.382084 
    - 25%          58.300135 
    - 50%          68.000000 
    - 75%          71.529860 
    - max          100.435793 

  6) Histogram generated by code and cannot be pasted into readme file. The reason for choosing 15 bins was explained above in (4). 
  7) Scatterplot generated by code and cannot be pasted into readme file. From the plot one can see that weight is strongly positively correlated with age until approximately age = 20. By then the incline plateaus and stablizes near the range 60-80kgs. Note that the standard deviation increases with age until age = 20, and then significantly expands and ages 20-100 all show high spread in data. 
  8) The outlier is named Anthony Freeman. From the scatterplot, one could see the outlier was significantly below average, therefore the dataset was filtered for all whose age is above 40 years with weight below 30kgs which is characteristic of the outlier's position on the plot, and only one name appeared: Anthony Freeman. 


Exercise 3: 
The data was downloaded on September 7th from https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv, provided by The New York Times. 
  1) The function 'plot_state_to_case' takes a list of state names and plots the state's cumulative number of casese against date on an overlaid linegraph, where different colors represent different states as shown in the legend (images cannot be pasted in readme). This function was tested against four states: Alabama, Alaska, Washington, and North Carolina. The y-axis shows cumulative cases with units of 1x10^6 cases, and the x-axis shows the corresponding dates. Some examples of this function in use include the situation in which one wishes to conduct time-series analysis or other trends between two counterparts, such as comparing exoneration rates between different races or within different states in the last century, or comparing the death rates of smokers who quitted nicotine after different lengths of usage. 
  2) This figure effectively provides an overview of the trends of case growth in different states, however it has three limitations: 

    I) The x-axis tick labels are overlapping with one another, making it impossible to read without magnifying. This problem will only be exacerbated as the dataset grows and the time range expands further. This limits the scale of the database that this plot could represent. The labels were rotated 80 degrees counterclockwise, however the effects seem to be unnoticeable. 
    II) The y-axis is in units of 1x10^6 because the data spans across a large range. This unit is added at the top of the chart which makes it difficult for viewers to notice, and hence could interpret the y valyues as single digits. 
    III) The lines are all on the same graph, which is again another scale limitation because with four lines, it is easy to read, but if one were to plot all 50 states, then the graph would be a near-incomprehensive mesh of colored yarn. 
  3) The function 'highest_ase_date' takes the name of a state and returns the date of its highest number of new cases. If a state recorded the same and the overall highest number of cases across several days, then only one date would be chosen. This is tested against three states: Alabama, Alaska, and Arizona. 
  4) The function 'state_comparison' takes the names of two states and reports which one had its highest number of cases first and how many days separate that one's peak from the other one's peak. This was tested against three pairs of states: 
 
    I) (Connecticut, Colorado) --> Connecticut had its highest number of cases 2 days before Colorado 
    II) (Alabama, Colorado) --> Both Alabama and Colorado had their highest number of cases on 2021-09-05 
    III) (Alabama, North Carolina) --> North Carolina had its highest number of cases 1 days before Alabama 
  Note that the observed results are different from the given ones in the assignment. This is likely because the assignment was written in 2020 but the database has already updated until September 2021. Some examples of the function in use include comparing the growth cycle of bacteria, tracking the metabolism of certain neurotransmitters, and etc. 


Exercise 4: 
a) Function true_false_values(population_size, sample_size) shown in Exercise 4.jpynb. The three test results for true_false_values(10,2) are the following: 
	[False, False, False, True, True, False, False, False, False, False] 
	[False, True, False, False, True, False, False, False, False, False] 
	[True, True, False, False, False, False, False, False, False, False] 

b) Function sample_select(population, sample_size) shown in Exercise 4.jpynb. The test output is included in the HW1_console_qz258 file. 

c) Function predicted_drug_users(population_size, drug_users, sample_size) shown in Exercise 4.jpynb. Test result of predicted_drug_users(1000, 100, 500) is the following: 

	Observed E(yes) in population of 1000 is 308. 
	Calculated E(yes) in population of 1000 is 300. 

d) The estimated number of drug users in a population 1000, 100 of whom are drug users, and sample size is 50, the estimated number of drug users using 4(c) is 284. The graph is significantly right-skewed, and the most frequent number of drug users within population is close or at 0. 

e) The histogram is shown in HW1_console_qz258. 10000 trials were conducted, this number was chosen based on the similarity of histogram shaped generated after multiple runs. If the shape shifts significantly, then the number of trials was increased until shifts were almost unnoticeable. 

f) The histogram is shown in HW1_console_qz258. 5000 trials were conducted, this number was chosen because, although 10000 trials could generate more accurate results, it already took about two minutes to run 1000 trials. For 10000 trials, it would be difficult to generate multiple histograms and compare them. Moreover, the greater sample size could have potentially mitigated for the smaller number of trials. Despite the fact that all parameter values of the prediction function in 4(f) was simply scaled up by 100 compared to 4(e), the shape of the distributions are very different, which was not expected. The graph in 4(f) is significantly more centered (less right-skewed), and the mode occurs around the center, hence more or less a bell shaped curve. This could potentially be because of the limited number of times the simulation was ran as compared to 4(e), hence the distribution could vary each time this code cell is ran. 

g) The histogram is shown in HW1_console_qz258. 20000 trials were conducted, this number was chosen because the sample size is smaller, and hence running more tests is both more important and less time-consuming. 10000 trials generated similar graphs after running test three times. This graph is significantly more centered compared to those in 4(e), and more similar to 4(f), which is to be expected given the differences between 4(e) and 4(f). This is because the rate of drug usage increased, hence the median of the prediction also shifts to the right (greater value). 