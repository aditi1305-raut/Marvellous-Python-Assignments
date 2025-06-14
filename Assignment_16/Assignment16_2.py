import os

def main():

    print("Enter the file name: ")
    file = input()

    fobj = os.path.exists(file)

    if (fobj == True):
        print("File is present")

        data = open(file,"r")
        content = data.read()

        print("Contents of file: \n",content)

    else:
        print("File is not found")


if __name__ =="__main__":
    main()