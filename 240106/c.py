N, Q = map(int,input().split())
ryux = list(range(1, N + 1))
ryuy = [0] * N

def arr(lst):
    a = lst[0]
    result = lst[-1:] + lst[:-1]
    lst[0] = a
    return result

for i in range(Q):
    query_list = input().split()
    query_num = int(query_list[0])
    query_str = query_list[1]
    
    if query_num == 1:
        if  query_str == "R":
            ryux = arr(ryux)
            ryux[0] += 1
            
        elif  query_str == "L":
            ryux = arr(ryux)
            ryux[0] -= 1
        
        elif  query_str == "U":
            ryuy = arr(ryuy)
            ryuy[0] += 1
            
        elif  query_str == "D":
            ryuy = arr(ryuy)
            ryuy[0] -= 1
            
    else:
        q = int(query_list[1])
        print(ryux[q-1], ryuy[q-1])
#どこが間違っているのか分からない！
#仮にあってたとしても、TLEになると思う