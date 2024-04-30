import copy
def compare(s,g):
    s.sort()
    g.sort()
    return s == g

q = []
visited = []
def generate_child(s):
    global q
    global visited
    for i in range(len(s)):
        temp = copy.deepcopy(s)
        if s[i] != []:
            top = temp[i][-1]
            del temp[i][-1]

            for j in range(len(s)):
                if i != j:
                    new_state = copy.deepcopy(temp)
                    new_state[j] = new_state[j] + [top]
                    if new_state not in q and new_state not in visited:
                        q.append(new_state)

def search(g):
    global q
    global visited
    c = 0
    while len(q):
        curr = q[0]
        del q[0]
        c += 1
        if curr == g:
            print(f"Found in {c} steps")
            exit()
        generate_child(curr)
        visited.append(curr[0])
    print("Cannot find solution")
    exit()

def main():
    s = [['A'], ['B','C'], []]
    g = [[], [], ['C','B','A']]
    generate_child(s)
    search(g)
main()    