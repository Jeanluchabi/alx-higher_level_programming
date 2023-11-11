#!/usr/bin/python3
if __name__ == "__main__":
    import sys, math
    
    result = 0

    for n in sys.argv[1:]:
        result += int(n)
        
    print(result)


