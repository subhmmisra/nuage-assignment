from concurrent.futures.thread import ThreadPoolExecutor

import typer

app = typer.Typer()

lookup_table = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
                'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
                'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
                'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
                'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B',
                'Z': 'A',
                'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v',
                'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q',
                'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l',
                'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
                'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b',
                'z': 'a'
                }


@app.command()
def hello(file: str):
    print(f'Reading....., {file}')

    with open(file, "r", encoding='utf-8-sig') as f:
        f_contents = f.read()
        cipher = ''
        for letter in f_contents:
            # checks for space
            if letter != ' ':
                # adds the corresponding letter from the lookup_table
                if not letter.isalpha():
                    cipher += letter
                else:
                    cipher += lookup_table[letter]
            else:
                # adds space
                cipher += ' '

        with open("encrypted_output.txt", "w") as wf:
            for i in cipher:
                wf.write(i)


@app.command()
def speed(file_name: str):
    file = [file_name]
    # # use as many threads as possible, default: min(32, os.cpu_count()+4)
    with ThreadPoolExecutor() as executor:
        executor.map(hello, file)


if __name__ == '__main__':
    app()