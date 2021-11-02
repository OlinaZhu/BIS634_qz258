

##Question 4: 
Parallelization: 
To parallelize the merge sort algorithm using 2 processes, I would find the tasks in merge sort that could be independently, i.e., one task does not rely on or feed into another. 
The two processes could be each assigned to half (N/2) items in the N-item array at the very first recursion. Each process could then spawn threads that further break down each half of the list into halves, i.e., N/4, N/8, ..., 1.
Note that subsequent bisections of the two N/2-item arrays could occur independently of each other because no shared memory or reliance on each other's output is present. 
Once a process has reached the point of producing arrays of 1 item from the initial N/2-item list, it begins to merge them back together in a sorted manner regardless of whether the other process has completed dividing its own N/2 items into single-item arrays. The first item of left array is compared with that of right array, and inserted into output array accordingly, and such comparison in order between the left and right arrays occur until all items have been added to the output array. Note that elements from the same subarray are never compared with each other, and elements in each of the two processes are not compared until the final step. 
In the final step, parallelization ends and only one process is needed to merge the two sorted N/2-item arrays together. 

Validation of Results: 
I would validate the results by running the same array in a traditional (non-parallel) version of merge sort and a parallel version of merge sort. If the two results are identical, then we know that the parallelization produces valid results, but we do not yet know whether it produces a speed-up from this test. I would run multiple arrays of different properties (length, repeating numbers, odd/even items, etc.) to eliminate errors in edge cases. 

Validation of Speed-up:
I would utilize the time package in python to track the runtime of my program. Again, I would run both a traditional (non-parallel) version and a parallel version of merge sort, but each implementation has a start_time = time.time() call in the very beginning of the code and a time.time() - start_time at the end of execution such that the duration of execution is returned. Moreover, I would run the two versions of merge sorts repeatedly on varying sizes of arrays, and plot each version's performance on a size-of-array v.s. runtime line graph. An average could be taken for 5 runs of each array-size, such that an overview of the standard error of runtime could also be visualized along with the trend. From the graph we will be able to: 
	1. Determine whether there is a speed up using parallelization on merge sort; 
	2. Determine the trend of increase/speed-up relative to traditional version: is the increase linearly increasing, constant, or exponentially increasing, or shrinking as the size of array increases; and 
	3. Calculate Big O of parallelized version and compare it to that of traditional version. 

## Question 5: 
Some of the initial exploration is shown in the previous homework assignment. The relevant output from said assignment will also be included in this console_qz258 pdf document in this homework along with new graphs and analysis. 

Figure I: 

Figure II: 

Figure III: 


Missing Data Code: 

Quantification of Missing Data: 

MCAR/MAR/MNAR? 

Data-cleaning Necessary? 


_____________________________________________________________________________________________

#Resources: 
https://docs.python-requests.org/en/latest/user/quickstart/ 
https://www.ncbi.nlm.nih.gov/books/NBK3837/ 
https://www.geeksforgeeks.org/get-post-requests-using-python/ 
https://www.w3schools.com/python/ref_requests_post.asp 
>>>>>>> 3cb9b98500c14042b3df6908ca2e88bcac39b6d8
