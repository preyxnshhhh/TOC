from automata.fa.dfa import DFA
dfa = DFA(
    states={'q0','q1','q2'},
    input_symbols={'0','1'},
    transitions={
        'q0': {'0':'q0','1':'q1'},
        'q1': {'0':'q2','1':'q0'},
        'q2': {'0':'q1','1':'q2'}
    },
    initial_state='q0',
    final_states={'q0'}
)
print("0   ->", dfa.accepts_input("0"))
print("11  ->", dfa.accepts_input("11"))
print("110 ->", dfa.accepts_input("110"))
print("100 ->", dfa.accepts_input("100"))
print("111 ->", dfa.accepts_input("111"))
