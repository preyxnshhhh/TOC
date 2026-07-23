from automata.fa.dfa import DFA
dfa= DFA(
    states={'q0','q1'},
    input_symbols={'0','1','2','3','4','5','6','7','8','9'},
    transitions={
        'q0':
        {'0':'q1','1':'q0','2':'q1','3':'q0','4':'q1','5':'q0','6':'q1','7':'q0','8':'q1','9':'q0'},
        'q1':
        {'0':'q1','1':'q0','2':'q1','3':'q0','4':'q1','5':'q0','6':'q1','7':'q0','8':'q1','9':'q0'}
        },
    initial_state='q0',
    final_states={'q1'}
)
print("124 ->", dfa.accepts_input("124"))   
print("135 ->", dfa.accepts_input("135"))   
print("80  ->", dfa.accepts_input("80"))    
print("7   ->", dfa.accepts_input("7"))     
print("246 ->", dfa.accepts_input("246"))   
