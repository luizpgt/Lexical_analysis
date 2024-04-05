




# TODO: permitir multiplas gramáticas como input para automato finito
# TODO: gerar fita 
# TODO: adicionar suporte à entrada de tokens SEPARADORES como + e ou -

from Deterministic_finite_automaton.main import generate_deterministic_state_transition_table, markdown_print

from models.tape_element import Tape_Element
from models.tape import Tape

from input_.lexical_scanner import read_valid_sentences


# generate deterministic_state_transition_table 
token_n_grammars_file = "finite_automata_input.txt";
deterministic_state_transition_table = generate_deterministic_state_transition_table(token_n_grammars_file);
print("\nDeterministic State Transition Table ::: \n");
markdown_print(deterministic_state_transition_table); # pretty print table 


# generate tape
input_file = "example_program_file.txt";
