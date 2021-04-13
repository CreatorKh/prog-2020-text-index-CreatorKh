
def read_file(filename, dir='data'):
    with open(f"../{dir}/{filename}.txt", 'r', encoding='utf-8') as f:
        text = f.read()
    return text


def save_file(filename, text, dir='data'):
    with open(f"../{dir}/{filename}.txt", 'w', encoding='utf-8') as f:
        f.write(text)
    return 1
