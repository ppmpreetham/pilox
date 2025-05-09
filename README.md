# Pilox

A simple programming language implementation for understanding interpreters and compilers

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: In Development](https://img.shields.io/badge/Status-In_Development-blue)](https://github.com/yourusername/Pilox)

## Overview

Pilox is an interpreted programming language built from scratch as a learning project. It's inspired by the Crafting Interpreters approach but with some unique additions. This project aims to demystify how programming languages work under the hood.

> ⚠️ **Note**: This project is currently under active development. Many features are incomplete or may change.

## Features

- C-like syntax with modern language features
- Support for variables, functions, and control structures
- First-class functions
- Object-oriented programming capabilities
- Dynamic typing
- Interactive REPL mode for quick testing
- File execution mode for running scripts

## Installation

*Coming soon*

## Usage

### REPL Mode

For interactive use, simply run:

```bash
pilox
```

This will start the Pilox REPL where you can write and execute code line by line.

### Running Scripts

To execute a Pilox script file:

```bash
pilox path/to/script.jlx
```

## Examples

### Hello World
```pilox
print "Hello, World!";
```

### Variables
*Coming soon*

### Control Flow
*Coming soon*

### Functions
*Coming soon*

## Project Structure
*Coming soon*

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
