# Lexical Analysis

Author: Luiz Paulo Grafetti Terres

CC: Construção de Compiladores

Professor: Braulio Adriano De Mello

# Usage Example:

`finite_automata_input.txt`: serves as input for the Deterministic State Transition Table submodule.

```
¨ This is a comment !
¨ This files contains regular grammars and tokens.
¨ It is meant to guaranteed work with at most: 
¨	1 Regular grammar, with N rules
¨	N Tokens of any reasonable length

se
entao
senao

<S> ::= a<A> | e<A> | i<A> | o<A> | u<A>
<A> ::= a<A> | e<A> | i<A> | o<A> | u<A> | ε
```

# Output expected from the Deterministic State Transition Table 

## Deterministic State Transition Table:

Note: ERROR state is actually `[0]`, but its output is represented by `-` for better understanding of the table;

 | Accept State | - |s |e |n |t |a |o |i |u |
|-|-|-|-|-|-|-|-|-|-|
 |  | [1] |[2, 9] |[4, 14] |- |- |[14] |[14] |[14] |[14] |
 |  | [2, 9] |- |[3, 10] |- |- |- |- |- |- |
 | _variable_A | [4, 14] |- |[14] |[5] |- |[14] |[14] |[14] |[14] |
 | _variable_A | [14] |- |[14] |- |- |[14] |[14] |[14] |[14] |
 | se | [3, 10] |- |- |[11] |- |- |- |- |- |
 |  | [5] |- |- |- |[6] |- |- |- |- |
 |  | [11] |- |- |- |- |[12] |- |- |- |
 |  | [6] |- |- |- |- |[7] |- |- |- |
 |  | [12] |- |- |- |- |- |[13] |- |- |
 |  | [7] |- |- |- |- |- |[8] |- |- |
 | senao | [13] |- |- |- |- |- |- |- |- |
 | entao | [8] |- |- |- |- |- |- |- |- |

--- 

`example_program_file.txt`: serves as input the lexical analysis.

```
se
entao
ent
senao
aaaeiou
```

# Outputs expected for the Lexical Analysis

Tape: [[3, 10], [8], [0], [13], [14], ['$']]

Symbol Table:

- State: [3, 10] (se)
  - Line: 1
  - Label: se

- State: [8] (entao)
  - Line: 2
  - Label: entao

- State: [0] (ERROR)
  - Line: 3
  - Label: ent

- State: [13] (senao)
  - Line: 4
  - Label: senao

- State: [14] (1_var_A)
  - Line: 5
  - Label: aaaeiou
