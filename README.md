# Pilox

A simple programming language implementation for understanding interpreters and compilers

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: In Development](https://img.shields.io/badge/Status-In_Development-blue)](https://github.com/yourusername/Pilox)

## Overview

Pilox is an interpreted programming language built from scratch as a learning project. It's inspired by the Crafting Interpreters approach but with some unique additions. This project aims to demystify how programming languages work under the hood.

> [!NOTE]  
> This project is currently under active development. Many features are incomplete or may change.

## Features

- C-like syntax with modern language features
- Support for variables, functions, and control structures
- First-class functions
- Object-oriented programming capabilities
- Dynamic typing
- Interactive REPL mode for quick testing
- File execution mode for running scripts

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/jilox.git
cd jilox

# No installation required - pure Python implementation
```

## Usage
```bash
python language/main.py
```

### REPL Mode

For interactive use, simply run:

```bash
pilox
```

This will start the Pilox REPL where you can write and execute code line by line.

```bash
pilox> var greeting = "Hello, world!";
pilox> print greeting;
Hello, world!
pilox> exit
```

### Running Scripts

To execute a Pilox script file:

```bash
pilox ./path/to/script.plx
```

## Examples

### Hello World
```pilox
print "Hello, World!";
```

### Variables
`*Coming soon*`
will look like:
```c
var name = "Pilox";
var version = 0.1;
print "Running " + name + " version " + version;
```

### Control Flow
`*Coming soon*`
will look like:
```c
var max = 10;
var i = 0;

while (i < max) {
  print i;
  i = i + 1;
}
```

### Functions
`*Coming soon*`
will look like:
```c
fun factorial(n) {
  if (n <= 1) return 1;
  return n * factorial(n - 1);
}

print factorial(5); // Outputs: 120
```
## Project Structure
```python
pilox/
├── language/
│   ├── main.py          # Entry point for the interpreter
│   ├── scanner.py       # Lexical analyzer
│   └── TokenType.py     # Token definitions
├── examples/            # Example pilox programs
└── README.md
```

## Implementation Details

Pilox is built following a classic compiler pipeline:

1. **Scanning/Lexing** (Implemented): Converting source text into tokens
2. **Parsing** (In progress): Building an abstract syntax tree
3. **Static Analysis** (Planned): Scope resolution and type checking
4. **Interpretation/Compilation** (Planned): Executing or translating the code

## Contributing

Contributions are welcome! If you'd like to help develop Pilox:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- [Crafting Interpreters](https://craftinginterpreters.com/) by Robert Nystrom
- The Python programming language

## Roadmap

- [x] Lexical analysis (Scanner)
- [ ] Parser implementation
- [ ] AST interpreter
- [ ] Variable declarations and scopes
- [ ] Control flow statements
- [ ] Functions and closures
- [ ] Classes and instances
- [ ] Standard library
