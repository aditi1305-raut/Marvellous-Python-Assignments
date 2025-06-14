import os

def main():
    print("Enter the file name you want to check: ")
    filename = input()

    ret = os.path.exists(filename)

    if (ret==True):
        print("File exists in current Directory")

        fobj = open(filename,"r")
        data = fobj.read()

        print("Data in the file: ",data)

        fobj.close()

    else:
        print("Such File is not present in Current Directory")


if __name__ == "__main__":
    main()