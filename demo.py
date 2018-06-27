total_seat=108
seat_num = int(raw_input())
alias = ['WS','MS','AS','AS','MS',"WS"];
count=0
map=[]
limit=[]
for i in range(1,total_seat+1):
    temp=()
    if(count>5):
        count=0
    temp = (i,alias[count])
    map.append(temp)
    count+=1

def _find(_seat,map):
    check =_seat in [i[0] for i in map]
    for seat in map:
        # print(_seat == seat[0])
        if((_seat == seat[0])==True):
            
            print seat[0],seat[1]
            
    
                
for i in range(1,109+12,12):
    limit.append(i) 

def opposit_site(inp):
    # print "Seat Number :",inp
    map_seat = []
    for i in range(1,len(limit)):
        test = range(limit[i-1],limit[i])
        for i,j in enumerate(test):
            map_seat.append((test[i],test[len(test)-(i+1)]))

    for s in map_seat:
        if((inp == s[0])==True):
            # print "Opposite Seat :",s[1]
            _find(s[1],map)

    

opposit_site(seat_num)

