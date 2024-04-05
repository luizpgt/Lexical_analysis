class Tape:
    def __init__(self, deterministic_state_transition_table):
        self.tape = [];
        self.deterministic_state_transition_table = deterministic_state_transition_table;
        self.state_error = str(0); 


    def add_to_tape(self, tape_element):
        self.tape.append(tape_element);


    def read_sentences(self, sentences):
        pass;


    def __str__(self):
        out = "";
        for it in self.tape:
            out += it.__str__() ;
        return out;
