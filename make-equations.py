import os
import sys
import re
def to_git_equation(file):
    
    # Replacement string
    equation_str = '<img src="https://render.githubusercontent.com/render/math?math='
    
    # Parse 
    with open(file, 'r') as reader:
        filelines = []
        for read in reader.readlines():
            read = re.sub(r'\$[^\$]+\$', lambda x: equation_str + x.group(0)[1:-1] + '\">', read)
            filelines.append(read)
    with open(file, 'w') as writer:
        writer.writelines(filelines)
    return 0

def main(**kwargs):
    
    # Get filename
    filepath = sys.argv[1]
    
    # Parse file
    to_git_equation(filepath)

    # Done
    print('LaTex equations transformed')

if __name__ == '__main__':
    main()
