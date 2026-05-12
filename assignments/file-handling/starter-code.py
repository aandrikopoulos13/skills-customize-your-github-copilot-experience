# starter-code.py
# Assignment: File Handling & Exception Management
# Use this file as your starting point. Fill in the TODO sections to complete the assignment.

# TODO: Implement the process_file() function below.
#       It should read an input file, process each line, and write results to output.txt.
#       It must also handle errors gracefully using try/except.

def process_file(input_filename):
    """
    Reads lines from input_filename, converts them to uppercase,
    and writes the results to 'output.txt'.

    Handles FileNotFoundError and any unexpected exceptions.
    Prints the total number of lines processed.
    """
    # TODO: Use a try/except block to catch FileNotFoundError
    # TODO: Use a with statement (or finally block) to ensure files are closed properly
    # TODO: Skip empty lines after stripping whitespace
    # TODO: Write each valid line in uppercase to output.txt
    # TODO: Print the total number of lines processed
    pass


# ── Entry point ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Test 1: Process a valid file
    # Create a sample input.txt before running, or use your own file
    process_file("input.txt")

    # Test 2: Attempt to process a file that does not exist
    # Expected output: Error: The file "missing-file.txt" was not found.
    process_file("missing-file.txt")
