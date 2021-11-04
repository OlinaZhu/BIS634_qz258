Note that readme is not complete, I will be submitting a pdf version of readme instead such that a single document could encapsulate the code, output, and analysis. Currently it is still two separate documents of: ReadMe.md and Console_qz258.pdf. 


## Question 1: 
Although no written response is required for this question, I still want to mention that I recieved a tremendous amount of help from our TF Wenxin Xu and Professor McDougal. 

Note that I was able to query the data but was unsuccessful at finding out which tags corresponded to 'query' and 'MeSH' because I was not able to generate an overview of the xml's tags. Therefore, all enties for query' and 'mesh' in the resulting jason and dataframes in Q2 are 'N/A'. This prohibited analysis of mesh values, so all code written in Q2 are to work 'hypothetically' but cannot generate any real values using data generated from Q1. 



## Question 2: 
As explained above, no results can be generated for Q2 due to faulty code in Q1. All code in Q2 are complete for reference. 



# Question 3: 
Not yet completed. Encountered trouble in installing pytorch (commandline shows requirements satisfied when I tried to install twice, but running code still shows no pytorch found). 



## Question 4: 
Parallelization: 
To parallelize the merge sort algorithm using 2 processes, I would find the tasks in merge sort that could be independently, i.e., one task does not rely on or feed into another. 

The two processes could be each assigned to half (N/2) items in the N-item array at the very first recursion. Each process could then spawn threads that further break down each half of the list into halves, i.e., N/4, N/8, ..., 1.

Note that subsequent bisections of the two N/2-item arrays could occur independently of each other because no shared memory or reliance on each other's output is present. 

Once a process has reached the point of producing arrays of 1 item from the initial N/2-item list, it begins to merge them back together in a sorted manner regardless of whether the other process has completed dividing its own N/2 items into single-item arrays. The first item of left array is compared with that of right array, and inserted into output array accordingly, and such comparison in order between the left and right arrays occur until all items have been added to the output array. Note that elements from the same subarray are never compared with each other, and elements in each of the two processes are not compared until the final step. 

In the final step, parallelization ends and only one process is needed to merge the two sorted N/2-item arrays together. 

Validation of Results: 
I would validate the results by running the same array in a traditional (non-parallel) version of merge sort and a parallel version of merge sort. If the two results are identical, then we know that the parallelization produces valid results, but we do not yet know whether it produces a speed-up from this test. I would run multiple arrays of different properties (length, repeating numbers, odd/even items, etc.) to eliminate errors in edge cases. 


Validation of Speed-up:
I would utilize the time package in python to track the runtime of my program. Again, I would run both a traditional (non-parallel) version and a parallel version of merge sort, but each implementation has a start_time = time.time() call in the very beginning of the code and a time.time() - start_time at the end of execution such that the duration of execution is returned. 

Moreover, I would run the two versions of merge sorts repeatedly on varying sizes of arrays, and plot each version's performance on a size-of-array v.s. runtime line graph. An average could be taken for 5 runs of each array-size, such that an overview of the standard error of runtime could also be visualized along with the trend. From the graph we will be able to: 

1. Determine whether there is a speed up using parallelization on merge sort; 
2. Determine the trend of increase/speed-up relative to traditional version: is the increase linearly increasing, constant, or exponentially increasing, or shrinking as the size of array increases; and 
3. Calculate Big O of parallelized version and compare it to that of traditional version. 


## Question 5: 
Some of the initial exploration is shown in the previous homework assignment. The code is reproduced in Q5.jpynb with additional analysis. Note that original code for HW2 is modified such that the "Date" column is now of type "datetime". The first four figures (2 tables, 2 graphs) are not included in the below, and Figure I below refers to the 5th figure in the console_qz258 file, which is the first graph newly generated for HW3. The output for Quantification of Missing Data is included in the console_qz258 file and is not reproduced here. 

Figure I: Lineplot showing the number of deaths over time from 2012 to 2021. The units shown on the x-axis is years, but the data points themselves are specific to days, hence a very messy graph showing an overall increase throughout the years. I tried to use barplot, histplot, and displot instead to generate columns, but it seems that the datetime format does not work very well with the axes of those graph formats. 

Figures II, III: Figure II shows a cleaned version of the type of drug columns (18 in total), where all NaN values in these columns are to be interpreted as 'N' for No and not missing if there exists at least 1 non-NaN value in the row, hence NaN is only kept if all entries in row for type of drug columns is NaN. Figure III shows the integration of this cleaned dataset for type of drug into the whole dataset. This helps to remove confounding of missing value analysis, as prior to such cleaning the crude number and proportion of missing values in these type of drug columns are incredibly high, whereas persumeably the intention of the publishers is to use the columns as tick-charts and simply left False values as blank. 

Figure IV: A dictionary showing the counts of missing values for each column, in the format: "column name": [crude number of missing values in column, proprtion of missing values in column]. Note that proportions are rounded to 3 decimal places, so 0.001 indicates a number rounded to 0.1%. 

Figure V: A dataframe constructed to show the information in Figure IV in a more organized, plottable way. 

Figure VI: A plot of missing values by crude number.The graph was made horizontal such that the labels could show clearly. Moreover, note that the column for 'Other Significant Conditions' is extremely high, and this applies to figure VII as well, but this is very amibugous data - it is difficult to say whether missing values here indicates none observed or confirmed no other conditions. Therefore, for further analysis, this variable was removed, as it contains so many missing values its analysis is likely to lack statistical power anyways. 

Figure VII: A graph similar to figure VI but showing proportion of column values missing rather than crude number. 

Figure VIII: A graph showing the information in figure VII but removing 'Other Significant Conditions' to obtain a more detailed view of the lower-valued columns. It seems that most columns have relatively small proportions of values missing except 'Description of Injury'and 'Injury Place'. 


### Missing and Cleaning Data Code 
#### (also found in console_qz258, only reproduced here as requested by homework manual): 
_________

1. Cleaning data by replacing type of drug NaN values with N appropriately: 
_________
	type_of_drug = data[["Heroin", "Cocaine", "Fentanyl", "Fentanyl Analogue", "Oxycodone", "Oxymorphone", "Ethanol", "Hydrocodone",	"Benzodiazepine", "Methadone", "Amphet", "Tramad", "Morphine (Not Heroin)", "Hydromorphone", "Xylazine", "Other", "Opiate NOS",	"Any Opioid"]]
	row = 0
	col_num = len(type_of_drug.columns)

	while row < len(type_of_drug):
	    num_nan = type_of_drug.iloc[row].isna().sum()
	    if num_nan != col_num: type_of_drug.iloc[row].fillna("N", inplace=True)
	    row += 1

	data[["Heroin", "Cocaine", "Fentanyl", "Fentanyl Analogue", "Oxycodone", "Oxymorphone", "Ethanol", "Hydrocodone",	"Benzodiazepine", "Methadone", "Amphet", "Tramad", "Morphine (Not Heroin)", "Hydromorphone", "Xylazine", "Other", "Opiate NOS",	"Any Opioid"]] = type_of_drug
_________

2. Count missing values and the proportion of each column that is missing to store in dictionary, and create dataframe 
_________
	nan_dict = {}
	cols = data.columns
	for col in cols:
	    nan_dict[col] = [data[col].isna().sum(), round(data[col].isna().sum()/len(data[col]), 3)]

	nan_df = pd.DataFrame.from_dict(nan_dict, orient='index', columns=['# Missing', 'Proportion of Column Data Missing']).reset_index() 
_________

3. 
_________ 
	// plot missing values graph by crude number

	missing_crude_plt = sns.barplot(data=nan_df, x='# Missing', y='index')


	// plot missing values graph by proportion of total column entries

	missing_prop_plt = sns.barplot(data=nan_df, x='Proportion of Column Data Missing', y='index')


	// obtain more detailed view on previous graph by removing the other significant conditions column

	missing_prop_mag_plt = sns.barplot(data=nan_df.drop([9]), x='Proportion of Column Data Missing', y='index')


	// examining potential associations between description of injury and other variables

	injury_assoc = data[data['Description of Injury'].isna()]

	IA_age_gb = injury_assoc.groupby('Age')['ID'].count()
	IA_age_gb.head(100)

	IA_sex_gb = injury_assoc.groupby('Sex')['ID'].count()
	IA_sex_gb

	IA_race_gb = injury_assoc.groupby('Race')['ID'].count()
	IA_race_gb

	IA_date_gb = injury_assoc.groupby('Date')['ID'].count()
	IA_date_gb = IA_date_gb.sort_values(ascending=False)


	// the follow 3 calls is to obtain an overview of the general pattern between dates and missing value counts in Description of Injury. 

	IA_date_gb.head(50)
	IA_date_gb.head(100)
	IA_date_gb.head(500)
_________ 


MCAR/MAR/MNAR: Analysis was done on the relationship between the missing values in 'Description of Injury' (DOI) and 4 other variables: 'Age', 'Sex', 'Race', and 'Date'. 

Age: It seems that most of the missing values for DOI is aggregated between ages 20-60, and relatively few data are missing for other age groups. This could potentially be because more cases within the age range 20-60 occured, hence a higher likelihood of having an increased crude number of missing data being associated with this age range. 

Sex: Men are more than two times as likely to have missing data in terms of crude numbers, but if we look at the age_gender_plt plot (orange-blue line plot at the top), then we see that more male cases are recorded than female cases, hence a crude number comparison may not be fair in concluding that men are more likely to experience missing values in this dataset. 

Race: White people cases contain significantly more missing DOI data than other races, and Hispanic White people and Black people came in second and third respectively, but are both much less than the data for White people. This could be due to the same fallacy of base numbers as described above. 

Date: Most of the missing data from this category came from 2015, and the density for missing data in 2015 is significantly higher than other years, as shown by the 3 calls to view the pattern of dates appearing in the dataset sorted in descending order for number of occurrences. The top 50 missing DOI date-values are in 2015, and this trend continued into the visible parts of the top 100 entries, and it is only in the top 500 entries that we begin to see appearance of other years, but with significantly lower occurrence. 

Due to the above analysis, I would say that DOI data is MAR because although it could be predicted by date to some extent, we can only say that if a DOI value is missing, it is more likely to be in the year 2015, but cannot be predicted by any other value, and even this prediction is not reliable because we did not calculate the percentage of data that are missing in 2015, which could be the next step to validate an association (or lack thereof) between missing DOI and Date. 

_____________________________________________________________________________________________

# Resources: 

https://docs.python-requests.org/en/latest/user/quickstart/ 

https://www.ncbi.nlm.nih.gov/books/NBK3837/ 

https://www.geeksforgeeks.org/get-post-requests-using-python/ 

https://www.w3schools.com/python/ref_requests_post.asp 
