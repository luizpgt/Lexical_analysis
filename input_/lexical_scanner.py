separator_chars = [' ', '\n'];
appearing_separator_chars = ['+', '-', '*', '/'];

separator_chars += appearing_separator_chars;

def read_input_sentences(filename):
    file = open(filename, "r");
    sentences = [];

    sentence = [];
    line = 1;
    while 1: 
        char = file.read(1);

        # eof
        if not char: 
            break;

        # separator
        if char in separator_chars: 
            # se o char for separador, guarda a palavra obtida até antes dele
            if len(sentence):
                sentences.append((sentence, line));
                sentence = []; 

            if char in appearing_separator_chars:
                # se o char atual for um separador reconhecido, 
                # adicionar ele também como sentenca de 1 char
                sentences.append(([char], line));

            if char == "\n": line += 1;
            continue;

        # adiciona char à sentenca atual
        sentence.append(char);

    file.close();
    return sentences;
