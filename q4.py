def stat_decorator(func):
    def wrapper(fName):
        with open(fName, 'r') as f: # we open the file in read only mode
            for line in f:
                numbers = func(line) # Calls the decorated function from the file as an argument
                if numbers:
                    print("------------------------------")
                    print("Numbers read:", numbers)
                    print("Count:", len(numbers))
                    print("AVG:", sum(numbers) / len(numbers))
                    print("MAX:", max(numbers))
                    print("------------------------------")
    return wrapper

@stat_decorator # we modify the func by calling the decorator before it
def printStats(line):
    #splits them into numbers because they are strings and we return them as a list
    numbers = [int(num) for num in line.split()] 
    return numbers

printStats('q4.txt')