
def day1_1(file_name):
    sum=0
    L=0
    R=0
    f=open(file_name,"r")
    lines=f.readlines()
    for line in lines:
        for char in line:
            if char.isnumeric():
                L=int(char)
                break
        reversed_line=line [::-1]
        for char in reversed_line:
            if char.isnumeric():
                R=int(char)
                break
        sum=sum+10*L+R
        L=0
        R=0
    f.close()
    return sum


def day1_2():
    
    return None