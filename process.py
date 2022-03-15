import sys
import os

current_sentence = 0


def process_folder(folder):
    for filename in os.listdir(folder): 
        process_file(folder + '\\' + filename)


def process_file(filename):
    i = 1
    processing_mode = False
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            if (not processing_mode and is_end_of_header(line)):
                processing_mode = True
            elif (processing_mode and is_start_of_footer(line)):
                processing_mode = False
            elif (processing_mode): 
                process_line(filename, i, line)

            i += 1


def is_end_of_header(line):
    return line.strip().endswith("lugu")


def is_start_of_footer(line):
    return line.startswith("KALEVIPOEG")


def process_line(filename, linenumber, line):
    global current_sentence
    token = ""
    token_index = 0
    token_start_position = 0
    i = 0
    for c in line: 
        i += 1
        if c.isalnum() or c == "'" or c == "′": 
             token += c
        else: 
            if len(token) > 0:
                 process_token(filename, linenumber, token_start_position, token_index, token)
                 token_index += 1

            if is_sentence_final(c):
                current_sentence += 1

            token = ""
            token_start_position = i


def is_sentence_final(character):
    return character in ['!', '.', '?']


def process_token(filename, linenumber, offset, idx, token):
    global current_sentence
    print(filename, current_sentence, linenumber, offset, idx, token, token.lower(), sep = '\t')


sys.stdout.reconfigure(encoding='utf-8')
process_folder(sys.argv[1])
