daysrun = 0
timesum = 0

while True:
    response = input("Enter 10km run time:")
    if response == 'q':
        break
    else:
        daysrun += 1
        timesum += float(response)

average = timesum / daysrun
print(f"Average of {average}, over {daysrun} runs")    
