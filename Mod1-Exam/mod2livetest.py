def hours_to_minutes(hours):
    minutes = hours * 60
    return minutes


hours = float(input('Enter the number of houre: '))
print(f"{hours} hours is equal to {hours_to_minutes(hours)} minutes.")
