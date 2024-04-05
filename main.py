




# TODO: permitir multiplas gramáticas como input para automato finito
# DONE: gerar fita 
# TODO: adicionar suporte à entrada de tokens SEPARADORES como + e ou -
# TODO: melhorar captura dos valores do arquivo de entrada "programa input"

from Deterministic_finite_automaton.main import generate_deterministic_state_transition_table, markdown_print
from models.lexical_analyzer import Lexical_Analyzer
from input_.lexical_scanner import read_input_sentences

# generate deterministic_state_transition_table 
token_n_grammars_file = "finite_automata_input.txt";
deterministic_state_transition_table = generate_deterministic_state_transition_table(token_n_grammars_file);
print("\nDeterministic State Transition Table ::: \n");
markdown_print(deterministic_state_transition_table); # pretty print table 

lexical_analyzer = Lexical_Analyzer(deterministic_state_transition_table);

programs_file = "example_program_file.txt";
list_of_all_sentences = read_input_sentences(programs_file);

lexical_analyzer.analyze_sentences(list_of_all_sentences);

print("LEXIC ANALYSIS");
print("--------------");
print("tape: ", lexical_analyzer.tape);
print();
print(lexical_analyzer);
