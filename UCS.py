#102203123
q = []
s = [['S','A',1],['S','B',5],['S','C',15],['A','G',10],['B','G',5],['C','G',5]]
visited = []
def compare(s,g):
    return g[0]==s[0]

def generate_children(st):
    global q
    global visited
    global s
    for x in s:
        if st[0]==x[0]:
            q.append([x[1],x[2]+st[1]])

def search(g):
    global q
    global visited
    while len(q):
        cur = q[0]
        del q[0]
        if compare(cur,g):
            if cur[1] < g[1]:
                g[1] = cur[1]
        else:
            generate_children(cur)
            visited.append(cur)        

def main():
    global q
    g = ['G',9999]
    q = [['S',0]]
    search(g)
    print(g)

main()