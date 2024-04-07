

from models.table_element import Table_Element

class Lexical_Analyzer:
    def __init__(self, deterministic_transition_table):
        self.det_state_transition_table = deterministic_transition_table;
        self.indet_state_transition_table = self.det_state_transition_table.state_transition_table;
        self.finite_automata = self.indet_state_transition_table.finite_automata;

        self.tape = [];
        self.symbols_table = [];
        self.final_sentence_symbol = '$';

        self.initial_state = [ self.finite_automata.start_state ];
        self.error_state = [ self.det_state_transition_table .error_state ];

    def add_accept_state_to_tape(self, accept_state):
        self.tape.append(accept_state);
    
    def add_symbols_table(self, table_element):
        self.symbols_table.append(table_element);

    def list_to_str_sentence(self, sentence):
        return "".join( map(str, sentence) );

    def capture_symbol_col(self, symbol):
        return self.indet_state_transition_table.get_symbol_position(symbol);

    def capture_state_row(self, state):
        return self.det_state_transition_table.state_index(state);

    def get_accept_state_value(self, state):
        # accept_state ::: ( list(state) , str(value) )
        for accept_state in self.det_state_transition_table.accept_states:
            if state == accept_state[0]:
                return accept_state[1];
        return ""

    def analyze_sentences(self, sentences_info):
        inde_stt = self.det_state_transition_table;

        for sentence_info in sentences_info:
            sentence = sentence_info[0];
            file_line = sentence_info[1];

            state = self.initial_state;
            for symbol in sentence: 
                # capturar transicao por esse simbolo a partir do estado atual
                col = self.capture_symbol_col(symbol);
                if [ col ] == self.error_state:
                    # filters 1 char long error
                    state = self.error_state;
                    break;
                row = self.capture_state_row(state);
                state = self.det_state_transition_table.table[row][col];
                # capture error state 
                if state == self.error_state:  
                    break;

            # add to symbols table 
            sentence_str = self.list_to_str_sentence(sentence);

            # verify if stopped at valid accept state
            state_accept_value = self.get_accept_state_value(state);
            if not state_accept_value:
                state = self.error_state;
                state_accept_value = self.get_accept_state_value(state);

            self.add_symbols_table(Table_Element(state, state_accept_value, file_line, sentence_str));
            self.add_accept_state_to_tape(state);

        # add final sentence symbol
        self.add_accept_state_to_tape( [self.final_sentence_symbol] );

    def __str__(self):
        out = "";
        out+= "Tape: ";
        out += str(self.tape) + "\n\n";
        out+= "Symbol Table:\n\n";
        for table_element in self.symbols_table:
            out += table_element.__str__() + "\n";
        return out;
            
