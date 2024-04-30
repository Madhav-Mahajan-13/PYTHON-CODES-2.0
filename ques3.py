from sys import maxsize  

def main():
    graph = [ [0 ,10, 15, 20] , 
              [10, 0, 35, 25] ,
              [15, 35, 0, 30] ,
              [20, 25, 30, 0] ]
    
    city_1=int(input("enter the starting node : "))
    city_1 -=1
    min = maxsize
    current = 0
    v= 4
    list = []
    
    for i in range(v):
        if i != city_1:
            city_2= i
            for j in range(v):
                if (j != city_1 and j!=city_2):
                    city_3 =j
                    for k in range(v):
                        if (k != city_1 and k!=city_2) and k != city_3: 
                            city_4 = k
                            current  = graph[city_1][city_1] + graph[city_2][city_3] + graph[city_1][city_2]+ graph[city_3][city_4]

                            if(current <= min):
                                min = current
                                list.append(city_1+1)
                                list.append(city_2+1)
                                list.append(city_3+1)
                                list.append(city_4+1)
    print(min)
    print(list)
    return min
main()
