import copy      
# copy class agar nahi usew karega toh s mai hi avalue update hoti rahe gi

def heuristic( current,g ):
    count =0
    for i in range(len(current)):
        for j in range(len(current[0])):
            if current[i][j] != g[i][j]:
                count+=1
            else:
                count +=0
    
    return count


def compare(s,g):
    if(s==g):
        return 1
    else:
        return 0

def find_0(s):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == 0:
                return [i,j] #returns value as an array 

def up(s):
    pos_0 = find_0(s)
    i = pos_0[0]
    j = pos_0[1]
    temp = copy.deepcopy(s)
    if (i>0):
        temp[i][j] = temp[i-1][j]
        temp[i-1][j]=0
    else:
        return 0

    return temp
    

def down(s):
    pos_0 = find_0(s)
    i = pos_0[0]
    j = pos_0[1]
    temp = copy.deepcopy(s)
    if (i<2):
        temp[i][j] = temp[i+1][j]
        temp[i+1][j]=0
    else:
        return 0

    return temp

def left(s):
    pos_0 = find_0(s)
    i = pos_0[0]
    j = pos_0[1]
    temp = copy.deepcopy(s)
    if (j>0):
        temp[i][j] = temp[i][j-1]
        temp[i][j-1]=0
    else:
        return 0
    return temp

def right(s):
    pos_0 = find_0(s)
    i = pos_0[0]
    j = pos_0[1]
    temp = copy.deepcopy(s)
    if (j<2):
        temp[i][j] = temp[i][j+1]
        temp[i][j+1]=0
    else:
        return 0
    return temp

def matching(s, g):
    c=0
    q = []
    q2 =[]
    n =  heuristic(s,g)
    q2.append([n,s])
    q.append(s)
    verify =[]
    verify.append(s)
    while(q2[0][1]!=g):

        if(up(q2[0][1])):
            dummy = up(q2[0][1])
            c+=1
            print(c)
            if dummy== g:
                print(dummy)
                return c
            else:
                if dummy not in verify:
                    verify.append(dummy)
                    q2.append([heuristic(dummy,g),dummy])
                    q.append(dummy)
   

        if(down(q2[0][1])):
            dummy = down(q2[0][1])
            c+=1
            
            print(c)
            if dummy== g:
                print(dummy)
                return c
            else:
                if dummy not in verify:
                    verify.append(dummy)
                    q2.append([heuristic(dummy,g),dummy])
                    q.append(dummy)
        
        if(left(q2[0][1])):
            dummy = left(q2[0][1])
            c+=1
            print(c)
            if dummy== g:
                print(dummy)
                return c
            else:
                if dummy not in verify:
                    verify.append(dummy)
                    q2.append([heuristic(dummy,g),dummy])
                    q.append(dummy)
        
        if(right(q2[0][1])):
            dummy = right(q2[0][1])
            c+=1
            print(c)
            if dummy== g:
                print(dummy)
                return c
            else:
                if dummy not in verify:
                    verify.append(dummy)
                    q2.append([heuristic(dummy,g),dummy])
                    q.append(dummy)
        # new_inut = q2[0]
        
        q2.pop(0)
        q2.sort()
        print(q2)
        print("hi")
        
        
        
        # new_inut.append([q2[0]])
       
        for i in range(len(q2)-1):
            if i == 0:
                print(q2[0])

                continue
            else:
                q2.__delitem__(i)
        # q2.top()
        
        # q2.__delitem__(q2[1:])
        # q2.pop(1)
        print(f'deleion {q2}')


        
    

def main():
    s = [[1,2,3],
         [8,6,0],
         [7,5,4]]

    g = [[2,8,1],
         [0,4,3],
         [7,6,5]]
    print(s)
    matching(s,g)

print("hi")
main()

