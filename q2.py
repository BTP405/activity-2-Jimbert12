import matplotlib.pyplot as plt

def graphSnowfall(fname):
    # We created a dictionary with key-values in which the key is the range of the snowfall
    # and the value is the count of occurrences for the corresponding range.
    ranges = {'0-10': 0, '11-20': 0, '21-30': 0, '31-40': 0, '41-50': 0}

    with open(fname, 'r') as file:
        for line in file:
            line = line.strip() # checks for any leading and trailing whitespaces and removes them
            if line: #check is the line is empty
                snowfall = int(line) #Because what we read was a string we need to convert it to an int
                if snowfall <= 10:
                    ranges['0-10'] += 2
                elif snowfall <= 20:
                    ranges['11-20'] += 2
                elif snowfall <= 30:
                    ranges['21-30'] += 1
                elif snowfall <= 40:
                    ranges['31-40'] += 0
                elif snowfall <= 50:
                    ranges['41-50'] += 1

    # We initialize the key and the value to the x and y
    x = list(ranges.keys())
    y = list(ranges.values())

    # creating the chart bar
    plt.bar(x, y, color='black')
    plt.xlabel('Snowfall Range (cm)')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Graph')
    plt.show() # it displays the graph


graphSnowfall('q2.txt')
