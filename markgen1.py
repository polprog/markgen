from random import *
import sys

grname = ""
top = ""
grammar = {}

itermax = 10

def flatten(lista, delimeter):
    flatstr = ""
    for k in lista:
        if type(k) == str:
            flatstr = flatstr + k
            flatstr = flatstr + delimeter
        elif type(k) == list:
            flatstr = flatstr + flatten(k, delimeter)
    return flatstr

def evaluate(grammar, tok, itern, itermax):
    if(itern == itermax):
        return ""
    worktok = grammar[tok][int(random() * len(grammar[tok]))]
    tokens = worktok.split()
    for i in range(len(tokens)):
        if tokens[i][0] == "$":
            tokens[i] = evaluate(grammar, tokens[i][1:], itern + 1, itermax)
    return tokens

with open("pkp.txt") as f:
    for line in f:
        # todo: chomp line
        if line[0] == "#": # comment
            continue
        # Parse first directives
        tokens = line.split(" ")
        if len(tokens) < 1:
            continue
        if tokens[0] == "GRAMMAR":
            grname = tokens[1].strip()
        if tokens[0] == "OUTPUT":
            top = tokens[1].strip()
        
        lr = line.split("=")
        if len(lr) < 2:
            continue
        #print(lr[0], ":\t", lr[1], end="")
        tok = lr[0].strip()
        val = lr[1].strip()
        if tok not in grammar:
            grammar[tok] = []
        grammar[tok].append(val)

    #print("Grammar", grname, "top token", top)
    #print(grammar)
    #print("########\n")
    n = 1
    if(len(sys.argv) > 1):
        n = int(sys.argv[1])
    for i in range(n):
        x = evaluate(grammar, top, 0, itermax)
        print(flatten(x, " "))
