from automata.fa.dfa import DFA
dfa = DFA(
    states={'q0','q1','q2','q3','q4'},
    input_symbols={'0','1'},
    transitions={
        'q0': {'0':'q0','1':'q1'},
        'q1': {'0':'q2','1':'q3'},
        'q2': {'0':'q4','1':'q0'},
        'q3': {'0':'q1','1':'q2'},
        'q4': {'0':'q3','1':'q4'}
    },
    initial_state='q0',
    final_states={'q0'}
)
print("0     ->", dfa.accepts_input("0"))
print("101   ->", dfa.accepts_input("101"))
print("1010  ->", dfa.accepts_input("1010"))
print("1111  ->", dfa.accepts_input("1111"))
print("10100 ->", dfa.accepts_input("10100"))
