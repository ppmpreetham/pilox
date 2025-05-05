import sys
import os
import tokenize
from io import StringIO

def runfile(filename):
    """Run the file with the given filename.
    This function reads the file, and executes it.

    Args:
        filename (str): Path to the file to be executed
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        run(content)
    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'")
        sys.exit(66)  # EX_NOINPUT
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(74)  # EX_IOERR

def run(source):
    """Run the source code.
    Gokenizes the source code and prints the tokens.

    Args:
        source (str): Line of code to be executed
    """
    try:
        tokens = []
        source_io = StringIO(source)
        for token in tokenize.generate_tokens(source_io.readline):
            tokens.append(token)
            
        for token in tokens:
            print(token)
            
    except tokenize.TokenError as e:
        print(f"Error tokenizing input: {e}")
    except Exception as e:
        print(f"Error: {e}")
    
def runprompt():
    while True:
        try:
            line = input("jilox> ")
            if line.strip() == "exit":
                break
            run(line)
        except EOFError:
            break
        except KeyboardInterrupt:
            print("\nExiting... :)")
            break
        except Exception as e:
            print(f"Error: {e}")

def main():
    if len(sys.argv) > 2:
        print("Usage: jilox <script>")
        sys.exit(64) # 64 for command line usage errors
        
    elif len(sys.argv) == 2:
        runfile(sys.argv[1]) # file mode
        
    else: 
        runprompt() # REPL mode
        
if __name__ == "__main__":
    main()