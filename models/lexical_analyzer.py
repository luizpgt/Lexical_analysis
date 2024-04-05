

from models.table_element import Table_Element

class Lexical_Analyzer:
    def __init__(self, deterministic_transition_table):
        self.det_state_transition_table = deterministic_transition_table;
        self.indet_state_transition_table = self.det_state_transition_table.state_transition_table;
        self.finite_automata = self.indet_state_transition_table.finite_automata;

        self.tape = [];
        self.symbols_table = [];


        self.initial_state = [ self.finite_automata.start_state ];
        self.error_state = [ self.det_state_transition_table .error_state ];

    def add_accept_state_to_tape(self, accept_state):
        self.tape.append(accept_state);
    
    def add_symbols_table(self, table_element):
        self.symbols_table.append(table_element);

    def str_sentence(self, sentence):
        return "".join( map(str, sentence) );

    def capture_symbol_col(self, symbol):
        return self.indet_state_transition_table.get_symbol_position(symbol);

    def capture_state_row(self, state):
        return self.det_state_transition_table.state_index(state);

    def analyze_sentences(self, sentences_info):
        inde_stt = self.det_state_transition_table;

        for sentence_info in sentences_info:
            sentence = sentence_info[0];
            file_line = sentence_info[1];

            state = self.initial_state; # create !!
            for symbol in sentence: 
                # capturar transicao por esse simbolo a partir do estado atual
                col = self.capture_symbol_col(symbol);
                if [ col ] == self.error_state:
                    state = self.error_state;
                    break;
                row = self.capture_state_row(state);
                print(row);
                state = self.det_state_transition_table.table[row][col];
                print(state);
                # capture error state 
                if state == self.error_state: # create !! 
                    break;
            # add to symbols table 
            sentence_str = self.str_sentence(sentence);
            self.add_symbols_table(Table_Element(state, file_line, sentence_str));
            self.add_accept_state_to_tape(state);

    def __str__(self):
        out = "";
        out+= "symb_table:\n";
        for table_element in self.symbols_table:
            out += table_element.__str__() + "\n";

        return out;
            
