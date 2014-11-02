import bisect
case= list(map(int,input().split())) # create a list of Integer from a list of String
N=case[0] #5
M=case[1] #3
k=case[2] #2 k value
numbers=list(map(int,input().split()))
'''Consider the given numbers 6 5 3 4 2
   When M is 3, circularly arranged numbers of above integers will look like 6 5 3 4 2 6 5
   note that 6 and 5 have been appended to the end of the original list'''
'''So we are doing exactly the same thing here. We append first M-1 numbers to its' own tail'''

'''numbers[:M-1] will generate a list with elements from 0 to M-1 th index from original list.
   When we want to join two lists, we use 'extend()' method '''
numbers.extend(numbers[:M-1]) # now we have a circular array

'''When length of subsequence(M) is 3 and 'K' value is 2,
   What we are going to do is
   1.Take the first subsequence 6 5 3.
   2.Then sort it in ascending order ->  3 5 6
   3.Get the '2nd' smallest number (5) from it and store in a list
   4.Then take the second subsequence 5 3 4 and repeat the process
   5.Finally find the smallest value in that list

   This could be a headache when M goes bigger. Because every large subsequence has to be sorted.

   if you carefully examined both susequences you may notice a connection between them
    6 5 3
      5 3 4
    Second subsequence can be generated by removing the first element of first subsequnce and adding 4 to it
    So you need to see that we don't have to generate each and every subsequence from the scratch.
    Instead you can use the previously created subsequence and edit it.

    Now you may have question,
    When we sort the subsequence how can we remove the first element? (which is 6)
    It may be in some where else.
    how do we add an element to a sorted list?

    1.Store the first element in a variable before sorting
    2.Sort the subsequence and find the k th smallest number and store it in a array
    3.Find the saved value in the sorted subsequence and remove it
    4.Then insert the value to be added (which is 4) in to the correct position

    1. a=subseq[0]
    2. subseq.sort()
    3. subseq.remove(a)
    4. subseq.insert(correct_index,4)

    Then we can find the 2nd smallest value in the edited subseqence
    In the next iteration we will remove 5 from the sorted array and add 2

    Still this is not good enough, because we have to iterate through elements in order to remove
    the first element of the subsequence and to insert the new value.
    In the worst case you may have to compare it against 2(n-1) elements.
    One for removing and one for inserting.

    Then how ca we optimize this?
    Well you need see that we have a sorted array.
    So we can perform a Binary search in order to find the index of the element we want to remove or index,
    which has a runtime of O(log n)
    Then we can delete that index from the sorted list at a glance'''



subsequence=numbers[0:M] # First we create an sebseqense of length M from beginning
subsequence.sort()
kVals=[]
kVals.append(subsequence[k-1]) # Then we append the k th smallest value to a list

for i in range(N-1):
    element_to_be_removed=numbers[i]
    element_to_be_added=numbers[i+M]

    '''Find the index of the element to be removed in sorted array.
         "Bisect" means to divide into two equal parts'''
    index_to_be_removed=bisect.bisect(subsequence,element_to_be_removed)-1
    del subsequence[index_to_be_removed] # delete index in sorted array
    '''We use the insort() method in bisect library which performs binary insertion to a sorted array'''
    bisect.insort_left( subsequence, element_to_be_added) # insert New value to the sorted list
    kVals.append(subsequence[k-1]) # append the k th smallest value in subsequence, to the list
    
kVals.sort()
print(kVals[0])