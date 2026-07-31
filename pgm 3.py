from automata.fa.dfa import DFA
dfa = DFA(
    states={'q0','q1','q2'},
    input_symbols={'0','1'},
    transitions={
        'q0': {'0':'q0','1':'q1'},
        'q1': {'0':'q2','1':'q1'},
        'q2': {'0':'q0','1':'q1'}
    },
    initial_state='q0',
    final_states={'q0'}
)
print("0    ->", dfa.accepts_input("0"))
print("100  ->", dfa.accepts_input("100"))
print("1100 ->", dfa.accepts_input("1100"))
print("10   ->", dfa.accepts_input("10"))
print("101  ->", dfa.accepts_input("101"))
