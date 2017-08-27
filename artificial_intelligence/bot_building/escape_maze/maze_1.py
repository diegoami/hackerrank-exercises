import sys
import os

rules_exc = [

    {
        "lines":
            [
                "#--",
                "#--",
                "#--",
                "UP",
                "#--",
                "#--",
                "#--"
            ],
        "answer" : "RIGHT"
    },

    {
        "lines":
            [
                "#--",
                "#--",
                "###"
            ],
        "answer": "RIGHT",

    }
,

 {
        "lines":
            [
                "###",
                "#--",
                "#--"
            ],
        "answer": "DOWN",

    }
,
    {
        "lines":
            [
                "###",
                "--#",
                "--#"
            ],
        "answer": "LEFT",

    }
,

    {
        "lines":
            [
                "--#",
                "--#",
                "--#"
            ],
        "answer": "LEFT",

    }
,
    {
        "lines":
            [
                "--#",
                "--#",
                "--#",
                "LEFT",
                "###",
                "---",
                "---",

            ],
        "answer": "LEFT",

    }
,
    {
        "lines":
            [
                "---",
                "---",
                "###",
                "UP",
                "###",
                "---",
                "---",

            ],
        "answer": "LEFT"

    },
    {
        "lines": [

                "###",
                "---",
                "---",
                "RIGHT",
                "#--",
                "#--",
                "#--"
            ],
        "answer" : "RIGHT"
    }



]

rules = [ 


    {
        "lines":
    [

    "#--",
    "#--",
    "#--",
    "UP",
    "#--",
    "#--",
    "#--",
    "UP",
    "#--",
    "#--",
    "#--"
    ],
        "answer": "RIGHT"
    },
    { "lines" :
       [

        "---",
        "--#",
        "--#",
        "UP",
        "---",
        "---",
        "--#",
    ],
    "answer" : "RIGHT"
    },
    {
        "lines":
        [

            "-##",
            "---",
            "---",
            "LEFT",
            "---",
            "---",
            "--#"
        ],
        "answer": "RIGHT"
    },

    {
        "lines":
            [

                "###",
                "---",
                "---",
                "RIGHT",
                "#--",
                "#--",
                "#--",
                "UP",
                "#--",
                "#--",
                "#--"
            ]
      ,
    "answer" : "RIGHT"
    }

,
    {
        "lines":
            [
                "#--",
                "#--",
                "#--",
                "RIGHT",
                "-##",
                "---",
                "---"

            ],
        "answer": "LEFT"
    },
]



def check_rules(lines):
    if (len(lines) >= 20):
        return None

    for i, rule_ex in enumerate(rules_exc):
        rev_lines = [l.strip() for l in lines]
        if (rev_lines == rule_ex["lines"]):
            print("Hit Rule Exc {}".format(i), file=sys.stderr)
            return rule_ex["answer"]

    for i, rule in enumerate(rules):
        if (len(rule["lines"]) > len(lines)):
            continue
        rev_lines = [l.strip() for l in lines]
        if (rev_lines[len(lines) - len(rule["lines"]):] == rule["lines"]):
            print("Hit Rule {}".format(i), file=sys.stderr)
            return rule["answer"]
    return None


def find_exit(maze):
    for j in range(len(maze)):
        if 'e' in maze[j]:
            return (j,maze[j].index('e'))
    return None

dirs_r = ['UP','RIGHT','LEFT', 'DOWN']
dirs_l = ['UP','LEFT','RIGHT', 'DOWN']








def get_best_move(maze, lines, prev_dir = "UP", prev_norm_dir= "UP"):

    def walk_possible(maze, dir):
        if dir == 'DOWN' and maze[2][1] in ['-','e']:
            return True
        elif dir == 'RIGHT' and maze[1][2] in ['-','e']:
            return True
        elif dir == 'UP' and maze[0][1] in ['-','e']:
            return True
        elif dir == 'LEFT' and maze[1][0] in ['-','e']:
            return True

    dir_from_rule = check_rules(lines)
    if (dir_from_rule):
        return dir_from_rule
    else:
        exit = find_exit(maze)
        if (exit):
            if exit[0] == 0 and walk_possible(maze,'UP'):
                return 'UP'
            elif exit[1] == 2 and walk_possible(maze,'RIGHT')  :
                return 'RIGHT'
            elif exit[1] == 0 and walk_possible(maze,'LEFT') :
                return 'LEFT'
            else:
                return 'DOWN'

        else:
            dir = prev_dir

            while True:
                if walk_possible(maze,dir):
                    return dir
                dir_index = dirs_r.index(dir)
                dir_index = dir_index + 1 if dir_index < 4 else 0
                dir = dirs_r[dir_index]

def read_history(filename):
    if (os.path.isfile(filename)):
        with open( filename, "r") as f:
            lines = f.readlines()
            return [l for l in lines if len(l.strip()) > 0]
    else:
        return []


def write_history(filename,lines):
    with open(filename, "w") as f:
        f.writelines([l for l in lines if len(l.strip()) > 0] )

def maze_dump(maze):
    maze_lines = []
    for j in range(3):
        maze_lines.append("".join(maze[j])+"\n")
    return maze_lines


def process(input, filename, overwrite=True):
    player = int(input())
    maze = []
    for j in range(3):
        maze.append([])
    for j in range(3):

        mazej = input()
        for i in range(3):
            maze[j].append(mazej[i])

    lines = read_history(filename)

    print("===== HISTORY === ", file=sys.stderr)
    lines = lines + maze_dump(maze)
    for line in lines:
        print(line.strip(),file=sys.stderr)

    new_dir = get_best_move(maze,lines)
    print("====== DIR === {} ==== ".format(new_dir), file=sys.stderr)
    lines.append(new_dir+"\n")
    if (overwrite):
        write_history(filename, lines)
    print(new_dir)
    return new_dir

def do_test_inputs():
    from tools import input, initFileInputter
    exp_results = ["DOWN","UP","RIGHT","RIGHT","UP","RIGHT","UP", "RIGHT", "LEFT", "RIGHT", "RIGHT", "RIGHT", "LEFT", "DOWN"]
    tests_failed = 0
    for i in range(1,15,1):
        str_to_pr = 'maze_'+str(i)+'.txt'
        history = 'history_'+str(i)+'.txt'
        print("======PROCESSING === {} ==========".format(str_to_pr),file=sys.stderr)
        initFileInputter(str_to_pr)
        res = process(input, history, False)
        if (res != exp_results[i-1]):
            tests_failed += 1
        print("======  END PROCESSING === {} =======".format(str_to_pr), file=sys.stderr)
        print("====== TESTS FAILED  ======{} =======".format(tests_failed), file=sys.stderr)
if __name__ == "__main__":
    do_test_inputs()
    #new_maze = do_turn_maze('')
    #process(input, 'history.txt')
    #test_mazes()