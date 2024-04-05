separator_chars = [' ', '\n'];
appearing_separator_chars = ['+'];

separator_chars += appearing_separator_chars;


def read_valid_sentences(filename):
    file = open(filename, "r");
    chars = [];

    schars = [];
    while 1: 
        char = file.read(1);
        # eof
        if not char: 
            break;
        # separator
        if char in separator_chars: 

            if char in appearing_separator_chars :
                chars.append([char]);

            chars.append(schars);
            schars = [];
            continue;
        schars.append(char);

    file.close();
    return chars;
