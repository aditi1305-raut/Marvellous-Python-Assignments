import os 

def main():

    print("Enter the file name you want Check: ")
    filename = input()

    ret = os.path.exists(filename)

    if (ret==True):
        print("File is Present in current Directory")

    else:
        print("File is not present")





if __name__ == "__main__":
    main()
    


