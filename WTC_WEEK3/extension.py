#Let's prompt a user to input a file name
def main():
    file_name = input("Enter a File Name: ")
    print(fileExtension(file_name))

def fileExtension(extension):
    #Let's code the if stament that will check if the extension file is there
    if ".gif" in extension:
      return "image/gif"
    elif ".jpg" in extension:
      return "image/jp"
    elif ".jpeg" in extension:
      return "image/jpeg"
    elif ".png" in extension:
      return "image/png"
    elif ".pdf" in extension:
      return "application/pdf"
    elif ".txt" in extension:
      return "text/plan"
    elif ".zip" in extension:
      return "application/zip"
    else:
      return "application/octet-stream"
    
main()