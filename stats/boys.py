import random
N=1000

def true_if_boy():
    return True if random.randrange(1,3) == 1 else False

one_boy, two_boys, first_one, second_one = 0, 0, 0, 0
for i in range(N):
    children = [true_if_boy(),true_if_boy()]
    one_boy += any(children)
    two_boys += all(children)
    first_one += children[0]
    second_one += children[1]

print(one_boy, two_boys, two_boys/one_boy)
print(first_one, second_one)