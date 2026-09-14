"""I am making a passphrase generator that uses the diceware method, created by Arnold G. Reinhold. 
I am using the EFF's large wordlist. As of now, I had to use AI to help me generate the code because I
forgot some of the Python functions. I am still learning.🫰🏾"""

import secrets

wordlist_file = "eff_large_wordlist.txt"

def generate_passphrase(num_words=6, separator=" "):
    with open(wordlist_file) as f:
        words = [line.split('\t')[1].strip() for line in f
                 if line.strip() and not line.startswith("#")]
    return separator.join(secrets.choice(words) for _ in range(num_words))

if __name__ == "__main__":
    print(generate_passphrase(6)) 