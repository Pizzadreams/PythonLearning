
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

if __name__ == "__main__":
    file_content = read_text_file(input("Enter the path to your file: "))
    print(file_content)

