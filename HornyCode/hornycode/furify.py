import builtins
import re
import random

def uwuify(text: str) -> str:
    text = re.sub(r'[rl]', 'w', text)
    text = re.sub(r'[RL]', 'W', text)
    text = re.sub(r'n([aeiou])', r'ny\\1', text)
    text = re.sub(r'N([aeiouAEIOU])', r'Ny\\1', text)
    words = text.split()
    for i in range(len(words)):
        if len(words[i]) > 2 and random.random() < 0.3:
            words[i] = words[i][0] + '-' + words[i]
    return ' '.join(words) + " ~nya"

def horny_print(*args, **kwargs):
    furry_args = [uwuify(str(arg)) for arg in args]
    builtins.original_print(*furry_args, **kwargs)

def enable_furry_output():
    if not hasattr(builtins, "original_print"):
        builtins.original_print = builtins.print
        builtins.print = horny_print

