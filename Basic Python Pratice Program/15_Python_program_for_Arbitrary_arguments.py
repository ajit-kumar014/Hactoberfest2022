#this is an example of "Arbitary Argument in Python"
#pyhton *args allows to acceptany number of positional arguments i.e arguments which are non-keyword arguments,variable-length argument list.

def sum(*num):
    sum=0;
    for n in num:
        sum+=n;
    
    print("Sum:",sum)

#code
sum(1,2,3,4)
sum(3,24,5,6,7,8,1)

  
