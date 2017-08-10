import re
import glob

textInput_instr = "def input\(\):\n\s+global state\n\s+result = ([a-zA-z0-9]+)\[state\]\n\s+state \+\= 1\n\s+return result"
textInput_outstr = "from tools import input, initArrayInputter\ninitArrayInputter("


def replace_pattern(filename ):
    def repl(m):
        arrayName = m.group(1)
        return textInput_outstr + arrayName + ")"

    with (open(filename , 'r')) as f:
        code = ''.join(f.readlines())
        replaced = re.sub(textInput_instr, repl, code)
        return replaced


for filename in glob.iglob('**/*.py', recursive=True):
    replaced_file = replace_pattern(filename)
    print(replaced_file)
    with (open(filename , 'w')) as f:
        f.write(replaced_file)
        f.close()


