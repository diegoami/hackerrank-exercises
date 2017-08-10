import re
import glob

textInput_instr = "def input\(\):\n\s+global state\n\s+result = ([a-zA-z0-9]+)\[state\]\n\s+state \+\= 1\n\s+return result"
textInput_outstr = "from tools import input, initArrayInputter\ninitArray.Inputter("



#fileName = '30days/binary_cont.py'


def replace_pattern(fileName):
    def repl(m):
        arrayName = m.group(1)
        return textInput_outstr + arrayName + ")"

    with (open(fileName, 'r')) as f:
        code = ''.join(f.readlines())
        replaced = re.sub(textInput_instr, repl, code)
        return replaced


for filename in glob.iglob('**/*.py', recursive=True):
    replaced_file = replace_pattern(filename)
    print(replaced_file)



