# 217.-Contains-Duplicate

## Method 1 - Sort then compare
Sorting by the sorted() function included with Python3 (which is an adaptive and powerful sorting algorithm) then comparing every adjacent value, we can detect any duplicates. 
Time: O(nlog(n))
Space: O(1)

## Method 2 - Using Hashsets
Using hashsets are more efficient in time compared to Sorting and comparing. Hashsets provide faster inserting and checking if a value already exists. For every element, we check if the set includes the current element. If does, we return True. If not for all elements, we return False.
Time: O(n)
Space: O(n)