# Start at 1 o'clock
hours = 1
while hours <= 12:
    # Each hour starts at 0 minutes
    minutes = 0
    while minutes < 60:
        # Each minute starts at 0 seconds
        seconds = 0
        while seconds < 60:
            print(f'{hours}:{minutes}:{seconds}')
            # After printing the  current hour:minutes:seconds,
            # increment the seconds counter
            seconds = seconds + 1
        # After we reach 59 seconds, go to the next minute
            minutes = minutes + 1
    # After we reach 59 minutes, go to the next hour
            hours = hours + 1