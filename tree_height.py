# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    children = {i: [] for i in range(n)}

    roots = []
    for i, parent in enumerate(parents):
        if parent == -1:
            roots.append(i)
        else:
            children[parent].append(i)
    #max_height = 0

    def FindMaxDepth(node, depth):
        if not children[node]:
            return depth
        else:
            max_depth = 0
            for child in children[node]:
                child_depth = FindMaxDepth(child, depth+1)
                max_depth = max(max_depth, child_depth)
            return max_depth
    max_height = 0
    for root in roots:
        height = FindMaxDepth(root, 0)
        max_height = max(max_height, height)
    return max_height+1


def main():
    # implement input form keyboard and from files
    letter = input()
    if 'I' in letter:
        n = int(input())
        parents = list(map(int, input().split()))
        print(compute_height(n, parents))
    elif 'F' in letter:
        file = input()
        file = ("test/" + file)
        if 'a' not in file:
            with open(file, 'r') as f:
                lines = f.readlines()
                n = int(lines[0])
                parents = list(map(int, lines[1].split()))
                print(compute_height(n, parents))
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# main()
# print(numpy.array([1,2,3]))