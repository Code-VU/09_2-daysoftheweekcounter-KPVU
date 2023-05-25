
def countDayOfTheWeek():
    # This first line is provided for you
    file_nameLong = "mbox-long.txt"
    file_nameShort = "mbox-short.txt"
    file_name = input("Enter a file name: ")
    dayCount: dict[str, str] = {}
    with open(file_name) as file:
        for line in file:
            if line.startswith("From "): #needs the space
                day = returnDay(line)
                dayCount[day] = dayCount.get(day, 0 ) + 1
    print(dayCount)

def returnDay(line: str) -> str:
    line = line.strip()
    lineList = line.split()
    day = lineList[2]
    return day
## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
