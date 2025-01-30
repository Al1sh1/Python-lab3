from itertools import permutations

def printpermutations(s):
    perms = [''.join(p) for p in permutations(s)]
    for perm in perms:
        print(perm)

printpermutations("abc")