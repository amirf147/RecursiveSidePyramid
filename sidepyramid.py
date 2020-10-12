##Question 12 (Bonus): Implement a recursive method to print the
##following output. Assume your method takes as input the length of the
##longest row (in this case 5), and another integer that will represent
##the progress toward the base case. It is allowed to code several
##functions, all of which does not have to be recursive.
##0
##0 1
##0 1 2
##0 1 2 3
##0 1 2 3 4
##0 1 2 3
##0 1 2
##0 1
##0

progress = 1 # value that determines the length of the row to be printed

def sequence(width):

    string = ''

    if width > 0:
    
        for i in range(width):
        
            string += str(i)
    
        print(string)

def side_pyramid(width, progress):

    """progress must always be 1 or you can just pass the predefined
variable progress which is set to 1. width defines how far out pyramid grows"""

    if width == 0:
        
        if width == 0 and progress == 0:
            return
        
        progress -= 1
        sequence(progress - 1)
        return side_pyramid(width, progress) 

    elif width > 0:
        
        sequence(progress)
        progress += 1
        return side_pyramid(width - 1, progress)

    else:
        print("width must be positive integer")
