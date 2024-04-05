class Table_Element:
    def __init__(self, state_identifier, file_line, label):
        self.state_identifier = state_identifier;
        self.file_line = file_line;
        self.label = label;

    def __str__(self):
        return f"- State: {self.state_identifier}\n  Line: {self.file_line}\n  Label: {self.label}\n";

