import sys

def process_tokens(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            tokens = line.split(sep = '\t')
            token_position = tokens[4]
            normal_token = tokens[5]
            if (token_position != '0') and normal_token[0].isupper():
                print(normal_token)

sys.stdout.reconfigure(encoding='utf-8')
process_tokens(sys.argv[1])
