from Deterministic_finite_automaton.main import generate_deterministic_state_transition_table, markdown_print
from models.lexical_analyzer import Lexical_Analyzer
from input_.lexical_scanner import read_input_sentences

def generate_lexical_analyzer(deterministic_state_transition_table, program_filename):
    lexical_analyzer = Lexical_Analyzer(deterministic_state_transition_table);

    list_of_all_sentences = read_input_sentences(program_filename);

    lexical_analyzer.analyze_sentences(list_of_all_sentences);
    
    return lexical_analyzer;

def print_stable_to_file(lexical_analyzer, stape_filename):
    tape = "";
    translation_table = "";
    stable = "";
    lines = [];
    # generate stable and translation table:
    for table_el in lexical_analyzer.symbols_table:
        if not (table_el.state_accept_value in tape):
            # for translation table:
            translation_table += '¨ ' + table_el.state_accept_value + "\n";
            # lines.append('¨ ' + table_el.state_accept_value + "\n");
        # generate table lines
        # table += str(table_el.state_identifier);
        stable += str(table_el.state_accept_value );
        stable += " " + str(table_el.file_line);
        stable += " " + str(table_el.label);
        stable += "\n";
        tape += (" " + table_el.state_accept_value);
    
    # append (EOF)
    translation_table += '¨ $ (EOF)\n'
    stable += '$\n'

    # lines.append(tape);
    lines.append(translation_table);
    lines.append(stable);
    with open (stape_filename, "w") as file:
        file.writelines(lines);

if __name__ == "__main__":
    finite_automata_input_filename = "finite_automata_input.txt";
    program_filename = "example_program_file.txt";

    print("DETERMINISTIC STATE TRANSITION TABLE");
    print("------------------------------------");
    deterministic_state_transition_table = generate_deterministic_state_transition_table(finite_automata_input_filename);
    markdown_print(deterministic_state_transition_table);

    print("LEXIC ANALYSIS");
    print("--------------");
    lexical_analyzer = generate_lexical_analyzer(deterministic_state_transition_table, program_filename);
    print(lexical_analyzer);

    stape_filename = "output_stable.txt";
    print_stable_to_file(lexical_analyzer, stape_filename);