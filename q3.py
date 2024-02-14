def wordCount(fName):
    dict = {}  # Initialize an empty dictionary

    with open(fName, 'r') as file:
        for lineNum, line in enumerate(file, start=1):  # Enumerate lines, starting from 1
            words = line.strip().split()  # Split the line into words
            for w in words:
                if w not in dict:
                    dict[w] = []  # Initialize a new word into the empty list
                if lineNum not in dict[w]:  
                    dict[w].append(lineNum)# Append line number if not added

    return dict

print(wordCount('q3.txt'))
