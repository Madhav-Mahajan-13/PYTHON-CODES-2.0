import copy      
# copy class agar nahi usew karega toh s mai hi avalue update hoti rahe gi
def dist(s,g):
     c=0
     for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] != g[i][j] :
                c=c+1
     return c 

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
    q.append([dist(s,g),s])
    verify =[]
    verify.append(s)
    while(q[0][1]!=g):

        if(up(q[0][1])):
            dummy = up(q[0][1])
            c+=1
            print(f'{c} --up ')
            if dummy== g:
                print(dummy)
                return c
            else:
                if dummy not in verify:
                    verify.append(dummy)
                    q.append([dist(dummy,g),dummy])
   

        if(down(q[0][1])):
            dummy = down(q[0][1])
            c+=1
            
            print(f'{c} --down ')
            if dummy== g:
                print(dummy)
                return c
            else:
                if dummy not in verify:
                    verify.append(dummy)
                    q.append([dist(dummy,g),dummy])
        
        if(left(q[0][1])):
            dummy = left(q[0][1])
            c+=1
            print(f'{c} --left ')
            if dummy== g:
                print(dummy)
                return c
            else:
                if dummy not in verify:
                    verify.append(dummy)
                    q.append([dist(dummy,g),dummy])
        
        if(right(q[0][1])):
            dummy = right(q[0][1])
            c+=1
            print(f'{c} --right ')
            if dummy== g:
                print(dummy)
                return c
            else:
                if dummy not in verify:
                    verify.append(dummy)
                    q.append([dist(dummy,g),dummy])
        
        q.pop(0)
        q.sort()
        print(q)
    

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

