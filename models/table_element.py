class Table_Element:
    def __init__(self, state_identifier, state_accept_value, file_line, label):
        self.state_identifier = state_identifier;
        self.state_accept_value = state_accept_value;
        self.file_line = file_line;
        self.label = label;

    def __str__(self):
        return f"- State: {self.state_identifier} ({self.state_accept_value})\n  Line: {self.file_line}\n  Label: {self.label}\n";

