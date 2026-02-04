arr=[2,45,23,11,65,45]
arr.reverse()
print(arr)

def reverse_array(a):
    start=0
    end=len(a)-1
    
    while start<end:
        temp=a[start]
        a[start]=a[end]
        a[end]=temp
        start+=1
        end-=1
        
    for  i in range(len(a)):
        print(a[i],end=" ")
        
a=[20,22,24,26,28]     
reverse_array(a)
