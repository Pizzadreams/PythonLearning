
def read_text_file(file_path):
    try: 
        file = open(file_path, "r") # attempt to open the file in read mode
        content = file.read() # read() called on the contents of the file as a string
        file.close() # close the file object, ensuring that system resources are released
        return content
    except FileNotFoundError: # exception is caught if file is not found
        print("File not found.")
        return "" # return empty string 

# file_path = input("Enter the path to your file: ")
# file_content = read_text_file(file_path) # holds the content of the file

# this ensures that it only runs when the script is invoked directly from the command line or executed as a standalone script.
if __name__ == "__main__": # checks if the current module is the main module being executed.
    file_content = read_text_file(input("Enter the path to your file: "))
    print(file_content)

