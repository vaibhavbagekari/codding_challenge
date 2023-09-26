def sort_array_0s_1s_2s(A,n):  
  i=0  
  countzero=0  
  countone=0  
  counttwo=0  
  while(i<n):  
    if (A[i]==0):  
      countzero=countzero+1  
    elif (A[i]==1):  
      countone=countone+1  
    else:  
      counttwo=counttwo+1  
    i=i+1  
  i=0  
  while(i<countzero):  
    A[i]=0  
    i=i+1  
  i=countzero  
  while(i<countzero+countone):  
    A[i]=1  
    i=i+1  
  i=countzero+countone  
  while(i<n):  
    A[i]=2  
    i=i+1  
  
print("Enter size of an array: ")  
n=int(input())  
print("Enter array elements: \n")  
i=0  
A=[]  
while(i<n):  
  ele=int(input())  
  A.append(ele)  
  i=i+1  
print("Array after sorting: \n")  
sort_array_0s_1s_2s(A,n)  
i=0  
for i in A:  
  print(i)  