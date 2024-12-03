import sys

# write a program that takes two command line arguments, which should be the 
# same length. It then reads its input one line at a time, replaces any characters
# found in the first argument with the corresponding character from 
# the second argument, and prints the result.

if len(sys.argv) == 3:
    arg_1 = sys.argv[1]
    arg_2 = sys.argv[2]
    
    if len(arg_1) == len(arg_2):
        for line in sys.stdin:
            line_copy = ''
            for i in line:
                if i in arg_1:
                    line_copy += arg_2[arg_1.rfind(i)]
                else:
                    line_copy+= i
            print(line_copy, end='')
    else:
        print("ERROR: Arguments must be the same length.", end='\n')
else:
    print("USAGE: welcome.py characters replacements", end='\n')
