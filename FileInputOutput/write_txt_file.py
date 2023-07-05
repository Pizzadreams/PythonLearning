from read_txt_file import read_text_file

def write_text_file(file_path, content):
    try:
        with open(file_path, 'w') as file: # "with" statement ensures that the file is properly closed after writing
            file.write(content)
        print("File written successfully.")
    except IOError: # if an IOError occurs, then the below is printed
        print("An error occurred while writing the file.")

if __name__ == "__main__": # code inside this suite will be executed when it is ran directly as the main module (it won't be executed if the file is imported as a module)
    file_path = input("Enter the path to your file: ")
    file_content = read_text_file(file_path)
    print("\nThe original file reads:\n" + file_content)

    new_content = input("Enter the content to write to the file: ")
    write_text_file(file_path, new_content)

    new_file_content = read_text_file(file_path)
    print("\nThe new file reads:\n" + new_file_content)