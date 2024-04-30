def sol(list1 ,list2):
   
    q  = [] 
    c=0
    q.append(list1)
    visited = []
    visited.append(list1)
    while(q[0]!=list2):
       print(q)
       lst=q[0]
       x=lst[0]
       y=lst[1]

       if(x<4):
            dummy = [4 , y]
            
            
            if (dummy == list2):
                print(dummy)
                return c
                
            else:
                if dummy not in visited:
                    visited.append(dummy)
                    q.append(dummy)
                    c+=1
                    print(c)


       if(y<3):
            dummy = [x ,3 ]
            
  
            if (dummy == list2):
                print(dummy)
                return c
                
            else:
                if dummy not in visited:
                    visited.append(dummy)
                    q.append(dummy)
                    c+=1
                    print(c)

       if(x>0):
            dummy = [0 , y]
            
        
            if (dummy == list2):
                print(dummy)
                return c
                
            else:
                if dummy not in visited:
                    visited.append(dummy)
                    q.append(dummy)
                    c+=1
                    print(c)
       if(y>0):
            dummy = [x , 0]
            
   
            if (dummy == list2):
                print(dummy)
                return c
                
            else:
                if dummy not in visited:
                    visited.append(dummy)
                    q.append(dummy)
                    c+=1
                    print(c)

       if(x+y>=4 and y>0):
            dummy = [4 , y-(4-x)]
            
     
            if (dummy == list2):
                print(dummy)
                return c
                
            else:
                if dummy not in visited:
                    visited.append(dummy)
                    q.append(dummy)
                    c+=1
                    print(c)

       if(x+y>=4 and x>0):
            dummy = [x - (3- y) ,3]
            
       
            if (dummy == list2):
                print(dummy)
                return c
                
            else:
                if dummy not in visited:
                    visited.append(dummy)
                    q.append(dummy)
                    c+=1
                    print(c)
       
       if(x+y>0 and x+y<=3 and x>=0):
            dummy = [0  ,x+ y]
            

            if (dummy == list2):
                print(dummy)
                return c
                
            else:
                if dummy not in visited:
                    visited.append(dummy)
                    q.append(dummy)
                    c+=1
                    print(c)

       if(x+y>0 and x+y<=4 and y>=0):
            dummy = [x + y  ,0]
            
            
            if (dummy == list2):
                print(dummy)
                return c
            else:
                if dummy not in visited:
                    visited.append(dummy)
                    q.append(dummy)
                    c+=1
                    print(c)

       q.pop(0)
       
    return c    

def main():
    initaial_state = [ 0, 0] # jug1 , jug 2
    final_state = [0 , 1]

    sol(initaial_state , final_state)

main()