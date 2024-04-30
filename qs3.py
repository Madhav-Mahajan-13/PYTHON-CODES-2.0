import random
import math
import copy
clauses = [
    ["n","a", "*","d"],
    ["*","c", "*","b"],
    ["n","c", "n","d"],
    ["n","d", "n","b"],
    ["n","a", "n","d"]
]

T=500
delta_T=50
# delta_E=0 #  e_current - e_previous
random_number = [0.655 ,0.254 ,0.432 ]
solution = [1,1,1,1]


# considering a maximizing prblem  good move ewhen deltaE >0
def goodmove(x):  #x= delta_E  
    if x>0:
        T=T-delta_T
        return True
    else:
        return False

def bad_move(x,i):
    p=1/(1+math.exp(-(x / T)))
    T=T-delta_T
    print(p)
    if p > random_number[i]:
        return True
    else:
        return False

def movegen(sol):
    index = random.randint(0, 3)
    if sol[index] == 0:
        sol[index] = 1 
    else:
        sol[index] = 0
    # new_sol = sol.copy()
    # return new_sol


def evaluate(sol):
        satisfied = 0
        for clause in clauses:
            if clause[0] == "n":
                s1 = not sol[ord(clause[1]-97)]
            else:
                s1 = sol[ord(clause[1]-97)]
            if clause[3] == "n":
                s2 = not sol[ord(clause[4]-97)]
            else:
                s2 = sol[ord(clause[4]-97)]

            if  s1 or s2 :
                satisfied +=1
            return satisfied
        
def main():
    e_curr = evaluate(solution)
    curr_st = solution.copy()
    for i in range(len(random_number)):

        next_st=curr_st.copy()
        movegen(next_st)
        e_next = evaluate(next_st)
        delta_E = e_next - e_curr
        if goodmove(delta_E):
            print('ACCEPTED')
            e_curr = e_next
            curr_st = next_st
            
        else:
            if bad_move(delta_E,i):
                print('ACCEPTED')
                e_curr = e_next
                curr_st = next_st
            else:
                print('rejected')

main()