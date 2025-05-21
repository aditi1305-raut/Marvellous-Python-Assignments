i =1 

def pattern(Num):
    global i
    if(i<=Num):
        print("* "*i)
        i = i +1
        pattern(Num)

''' for i in range(1,Num+1):
        print("* "*i)'''
    
def main():
    ret = pattern(4)
    print(ret)
    
if __name__ == "__main__":
    main()