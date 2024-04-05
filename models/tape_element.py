class Tape_Element:
    def __init__(self, state, file_line, label):
        # e.g :: str(2,9) -> originally [2, 9] on det. state transition table
        self.state_symbol = self.str_state_symbol(state); 

        self.file_line = file_line;
        self.label = label; # accepted label


    def str_state_symbol(self, state):
        return ",".join( map( str, state) );


    def __str__(self):
        return f"- Est: {self.state_symbol}\n  Line: {self.file_line}\n  Label: {self.label}\n";
