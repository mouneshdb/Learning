# filehandling in python
import sys
count = 0
rep = 0
with open("sample1.txt", "r") as file:
    for line in file.readlines():
        each_rep = line.count(sys.argv[1])
        rep += each_rep
        while(rep > 9):
            count += 1
            rep -= 9

print(count)
