#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math 

# Nested for loop printing triangles
def nestFors(height):
    nestFors = "Nested for loops"
    printStr(nestFors)

    #PsuedoCODE
    #for( int i = 1, i <= height, i++){
    #   for (int j = i, i < j, j++){
    #       print(*)
    #   }
    #   print("\n")
    #}

    for i in range(1, height + 1):
            print("*" * i)

# List version of printing triangle
def listLoop(height):
    listStr = "Using List"
    printStr(listStr)

    triList = []
    for i in range(1, height + 1):
        triList.append("*" * i)
    print("\n".join(triList))

# Looped print 180 reverse triangle
def revStr(height):
    revStr = "180 Reverse triangle"
    printStr(revStr)

    for i in range(height - 1, -1, -1):
        print("{}{}".format(" " * i , "*" * (height - i)))

# Recursive triangle print
def recTri(height):
    if height > 0:
        recTri(height - 1)
        print("*" * height)

# Recursive upside down triangle print
def recUpTri(height): 
    print("*" * height)
    if height > 0:
        recUpTri(height - 1)

# Recursive 180 reverse triangle print
def recRevTri(height, i):
    print("{}{}".format(" " * height, "*" * i ))
    if height > 0:
        recRevTri(height-1,i + 1)

# Looped pyramid printing
def pyraPrint(height):
    j = 1
    for i in range(height -1, -1, -1):
        print("{}{}".format(" " * i, "*" * j))
        j += 2 

# Recursive pyramid print inc by 1
def recPyraPrint(height,i):
    print("{}{}".format(" " * height ,"*" * i))
    if height > 0:
        recPyraPrint(height - 1, i + 2)

# Looped pyramid inc by 2
# 1 = [ , , , ,*, , , , ]
# 2 = [ , ,*,*,*,*,*, , ]
# 3 = [*,*,*,*,*,*,*,*,*]
def pyraPrint2(height):
    k = (height - 2) + height 
    for i in range(1, height+1):
        print("{}{}".format(" " * k ,"*" * (4 * i - 3)))
        k -= 2 

# Recursive pyramid print inc by 2
# 1 = [ , , , ,*, , , , ]
# 2 = [ , ,*,*,*,*,*, , ]
# 3 = [*,*,*,*,*,*,*,*,*]
def recPyraPrint2(k, i):
    print("{}{}".format(" " * k ,"*" * i))
    if k > 0:
        recPyraPrint2(k - 2, i + 4)

# triangle print with inc by 2
def triPrint2(height): 
    j = 1;
    for i in range(1, height + 1):
        print("*" * j)
        j += 2;

# Simple print for name
def printStr(name):
    strLen = len(name)
    print("=" * strLen)
    print(name)
    print("=" * strLen)

height = input("Please enter the depth of triangle \t")
# nestFors(height)
# listLoop(height)
# revStr(height)
# recTri(height)
# recUpTri(height)
# recRevTri(height, 1)
# pyraPrint(height)
# recPyraPrint(height, 1)
recPyraPrint2(((height - 2) + height), 1) 
# pyraPrint2(height)
# triPrint2(height)
