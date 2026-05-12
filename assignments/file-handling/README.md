# 📘 Assignment: File Handling & Exception Management

## 🎯 Objective

Students will learn how to read from and write to files in Python, and how to write robust programs using `try/except` blocks to gracefully handle errors and unexpected input.

## 📝 Tasks

### 🛠️ Read and Write Files

#### Description

Write a Python program that reads data from a plain text file, processes each line, and writes the results to a new output file.

#### Requirements

Completed program should:

- Open and read a provided text file line by line
- Strip whitespace and skip any empty lines
- Convert each valid line to uppercase and write it to a new file called `output.txt`
- Print the total number of lines processed to the console
- Example: if `input.txt` contains:

```
hello world
  python is fun

goodbye
```

Then `output.txt` should contain:

```
HELLO WORLD
PYTHON IS FUN
GOODBYE
```

### 🛠️ Handle Errors with try/except

#### Description

Extend the program to handle common errors gracefully, so it never crashes unexpectedly regardless of the input provided.

#### Requirements

Completed program should:

- Use a `try/except` block to catch a `FileNotFoundError` if the input file does not exist, and print a friendly error message instead of crashing
- Use a `try/except` block to catch any unexpected errors during file processing and print the error details
- Add a `finally` block to ensure files are always properly closed, or use a `with` statement instead
- Demonstrate the error handling by attempting to open a file that does not exist:

```python
process_file("missing-file.txt")
# Expected output: Error: The file "missing-file.txt" was not found.
```
