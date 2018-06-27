size=int(raw_input())
# size=5

inp_array = raw_input().split(' ') 
array = [int(num) for num in inp_array]
product=1
for i in range(0,size):
    temp = int(raw_input())
    array.append(temp)
for i in array:
    product=product*i
print product