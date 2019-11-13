from sys import argv

if __name__ == "__main__":
    script, first, second = argv
    Arr1 = first[1:-1].split(',')
    Arr2 = second[1:-1].split(',')

    outStr = ""
    Ind = False
    for i in Arr1:
        for j in Arr2:
            if (i==j):
                Ind = True
        if (Ind):
            outStr+="1"
        else:
            outStr+="0"
        Ind = False

    print(outStr)