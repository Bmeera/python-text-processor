import os

def prompt_user_for_input(input_file):
    """Ask user if they want to provide new text and save it to input.txt."""
    while True:
        choice = input("Would you like to enter new text to process? (y/n): ").strip().lower()
        if choice in ['y', 'yes']:
            print("Enter your text (type END on a new line to finish):")
            lines = []
            while True:
                line = input()
                if line.strip().upper() == 'END':
                    break
                lines.append(line)
            
            new_text = "\n".join(lines)
            
            with open(input_file, 'w') as f:
                f.write(new_text)
            print(f"New text saved to {input_file}!\n")
            break  # Done — exit the loop
        elif choice in ['n', 'no']:
            print("Okay! Using the existing input.txt file.\n")
            break  # Valid answer — exit the loop
        else:
            print("Please enter a valid choice: 'y' or 'n'.")

def read_file(file_path):
    """Read text from a file."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def process_text(text):
    """Process the text (count words, convert to uppercase)."""
    if not text:
        return None
    
    # Count words
    word_count = len(text.split())
    
    # Convert to uppercase
    uppercase_text = text.upper()
    
    return {
        "original_text": text,
        "word_count": word_count,
        "uppercase_text": uppercase_text
    }

def write_results(results, output_file):
    """Write the processed results to a file."""
    if not results:
        return False
    
    try:
        with open(output_file, 'w') as file:
            file.write(f"Original Text:\n{results['original_text']}\n\n")
            file.write(f"Word Count: {results['word_count']}\n\n")
            file.write(f"Uppercase Text:\n{results['uppercase_text']}\n")
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False

def main(input_file="input.txt", output_file="output.txt"):
    """Main function to process a text file."""
    # Skip interactive prompt if running in CI
    if os.getenv("CI") != "true":
        prompt_user_for_input(input_file) #propmts the user to ask if they want to change the file

    text = read_file(input_file)
    if text:
        results = process_text(text)
        if results:
            success = write_results(results, output_file)
            if success:
                print(f"Processing complete. Results written to {output_file}")
                return True
    
    print("Processing failed.")
    return False

if __name__ == "__main__":
    main()
