my_dict = {}

def load_prompts():
    with open('PROMPTS.txt', 'r') as f:
        for line in f:
            key, value = line.split(':')
            my_dict[key] = value

    return my_dict


def parse_bullets(bullets):
    # Given a string in the following format:
    # 1. "string 1"
    # 2. "string 2"
    # and so forth
    # Extract the strings and return them in a list
    
    strings = []
    for line in bullets.split('\n'):
        print(line)
        if line.strip():
            string = line.split('. ')[1]
            strings.append(string)

    return(strings)

# s = "1. Climate change Republican policy absurd\n"
# print(parse_bullets(s))
    
