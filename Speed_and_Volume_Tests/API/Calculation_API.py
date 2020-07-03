# Calculate the average speeds for fixed and mobile per a country
def average_speeds(speeds):
    answer = 0
    total = 0

    for speed in speeds:
        answer += float(speed)
        total += 1

    answer = answer / total

    return '{:.2f}'.format(answer)


# Calculate the average volumes for fixed and mobile per a country
def average_volumes(volumes):
    answer = 0
    total = 0

    for volume in volumes:
        answer += (float(volume) * 100)
        total += 1

    answer = answer / total

    return '{:.2f}'.format(answer)