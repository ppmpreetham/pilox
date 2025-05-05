import sys

def runfile(filename):
    ...
    
def runprompt():
    ...

def main():
    if len(sys.argv) > 1:
        print("Usage: jilox <script>")
        sys.exit(64) # EX_USAGE
    elif len(sys.argv) == 1:
        runfile(sys.argv[0])
    else:
        runprompt()
        

if __name__ == "__main__":
    main()