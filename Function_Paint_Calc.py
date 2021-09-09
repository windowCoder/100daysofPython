
def paint_calc(h, w):
    return(h * w / 5)


#TODO-1: Create a calculator for these instructions:
# 1 can of paint per 5 square meters of wall. Given any
# height and width of wall, calculate how many cans of paint needed.
# Number of cans = ( wall height x wall width) / coverage per can.
# [Height = 2, Width = 4, Coverage = 5] => (2x4)/5 = 1.6

h = int(input("height of wall? "))
w = int(input("width of wall? "))
print(paint_calc(h, w))