import sys
import os

def runfile(filename):
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
    ...
    
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