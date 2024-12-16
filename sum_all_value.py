'''
The program takes a dictionary and prints the sum of all the items in the dictionary.
Problem Solution:
1. Declare and initialize the n number of dictionary values from the user.
2. Find the sum of all the values in the dictionary.
3. Print the total sum.
4. Exit.
Sample Input:
3
100
540
239
Sample Output :
879
'''
n=int(input())
sum_values=0
di={}
for i in range(n):
    di[i]=int(input())
for j in di.values():
    sum_values+=j
print(sum_values)
