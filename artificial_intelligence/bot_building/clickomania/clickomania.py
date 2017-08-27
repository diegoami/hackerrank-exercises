import sys

#!/bin/python
def nextMove(x, y, color, grid):
    color_map = {}
    for j in range(x):
        for i in range(y):
            if (grid[j][i] == '-'):
                continue
            color = grid[j][i]
            bordering = [(jj,ii) for jj,ii in  [(j-1,i),(j+1,i),(j,i-1),(j,i+1)] if jj >= 0 and jj < x and ii >= 0 and ii < y]
            color_map[(j,i)] = [(jj,ii) for jj,ii in bordering if grid[jj][ii] == grid[j][i]]
    col_some = {k:v for k,v in color_map.items() if len(v) > 0 }

    collist = sorted(col_some.items(), key=lambda x:x[0][0]*10+len(x[1]), reverse=True)
    print (collist, file=sys.stderr)
    return collist[0][0]

def process(input, filename=None, overwrite=True):
    x,y,k = [ int(i) for i in input().strip().split() ]
    grid = [[i for i in str(input().strip())] for _ in range(x)]
    j,i = nextMove(x, y, k, grid)
    print(j,i)


def do_test_inputs():
    from tools import input, initFileInputter
    exp_results = []
    tests_failed = 0
    for i in range(1,3,1):
        str_to_pr = 'click_'+str(i)+'.txt'
        history = 'history_'+str(i)+'.txt'
        print("======PROCESSING === {} ==========".format(str_to_pr),file=sys.stderr)
        initFileInputter(str_to_pr)
        res = process(input, history, False)
        #if (res != exp_results[i-1]):
        #    tests_failed += 1
        print("======  END PROCESSING === {} =======".format(str_to_pr), file=sys.stderr)
        print("====== TESTS FAILED  ======{} =======".format(tests_failed), file=sys.stderr)
if __name__ == "__main__":
    do_test_inputs()
    #new_maze = do_turn_maze('')
    #process(input, 'history.txt')