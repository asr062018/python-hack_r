str = str(raw_input())

list_str = list(str)
reve_str =[]

for i in range(len(list_str)):
    reve_str.append(list_str[len(list_str)-i-1])

if list_str == reve_str:
    print 'YES'
else:
    print 'NO'
