def list_avg(num):
    if num==[]:
        return 0
    total=sum(num)
    count=len(num)
    average=total/count
    return average
print(list_avg([1,2,4,5,6,7]))
