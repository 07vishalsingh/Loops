'''
You are given a list of file names. Write a Python function to find and return the file extensions of all the file names in the list. The file extension of a file name is the part after the last "." character. Return the file extensions as a set to avoid duplicates.
'''
def extract_file_extensions(files):
    extensions = set()
    for file_name in files:
        # Split the file name at the "." character
        parts = file_name.split(".")
        if len(parts) > 1:
            # Add the file extension to the set
            extensions.add(parts[-1])
    return extensions

# Example usage
file_list = [
    "document1.txt",
    "image.png",
    "presentation.pptx",
    "script.py",
    "data.csv"
]
print("File Extensions:", extract_file_extensions(file_list))  # Output: {'csv', 'pptx', 'txt', 'png', 'py'}
