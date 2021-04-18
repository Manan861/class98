def countWords():
    fileName=input("Type in the file name: ")
    WordCount=0
    file=open(fileName,'r')
    for line in file:
        words=line.split()
        WordCount=WordCount+len(words)
    print("Number of words in the file are: " )
    print(WordCount)

countWords()
