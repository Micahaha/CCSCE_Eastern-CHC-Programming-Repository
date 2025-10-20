def main():
    userInput()

    
def userInput():

    list = []

    while True:

        line = input("Enter a sequence of heights, to stop enter stop: ")

        if line == '-1':
            break

        if line.strip() == '-1':
            exit

        list.append(yesOrNo(line))

    index = 0

    for i in list: 
        print(list[index])
        index += 1  



def yesOrNo(inp):

    lineList = inp.split()
    print (lineList)
    if sorted(lineList) == lineList or sorted(lineList, reverse=True) == lineList:
        return 'yes'
    else:
        return 'no'


main()