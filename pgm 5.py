from automata.fa.dfa import DFA
dfa = DFA(
    states={'q0','q1','q2','q3','q4','q5'},
    input_symbols={'0','1'},
    transitions={
        'q0': {'0':'q0','1':'q1'},
        'q1': {'0':'q2','1':'q3'},
        'q2': {'0':'q4','1':'q5'},
        'q3': {'0':'q0','1':'q1'},
        'q4': {'0':'q2','1':'q3'},
        'q5': {'0':'q4','1':'q5'}
    },
    initial_state='q0',
    final_states={'q0'}
)
print("0     ->", dfa.accepts_input("0"))
print("110   ->", dfa.accepts_input("110"))     
print("10010 ->", dfa.accepts_input("10010"))   
print("111   ->", dfa.accepts_input("111"))     
print("1010  ->", dfa.accepts_input("1010"))    
