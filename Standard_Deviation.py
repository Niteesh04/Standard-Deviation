import math
import csv
with open('data.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)
data=file_data[0]
n=len(data)
total=0
for x in data:
    total += int(x)
mean=total/n
Square_List=[]
for number in data:
    a=int(number)-mean
    a=a**2
    Square_List.append(a)
sum=0
for i in Square_List:
    sum=sum+i
result = sum/(len(data)-1)
std_deviation=math.sqrt(result)
print(std_deviation)