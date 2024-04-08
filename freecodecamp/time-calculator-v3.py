week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def add_time(start, duration, *args):
    #SPLIT
    [ST, unit] = start.split(" ")
    [SH, SM] = ST.split(":")
    [DH, DM] = duration.split(":")


    #SUM
    total_minutes = int(SM) + int(DM)
    total_hours = int(SH) + int(DH)
    future_days = 0

    #IF HOUR INCREMENTED
    if total_minutes >= 60:
        total_minutes -= 60
        total_hours +=1
    
    #IF MINUTES < 10 MINUTES = 0X   WHERE X = MINUTES
    if total_minutes <10:
        total_minutes = f"{total_minutes}".zfill(2)

    if total_hours >= 12:
        half_days, hours = divmod(total_hours, 12)
        total_hours = hours if hours else total_hours
        #IF 24, 36, 48 ...
        if total_hours > 12:
            total_hours = total_hours - ((half_days - 1) * 12)
        
        if unit == "PM":
            future_days = ((half_days - 1) // 2) + 1
        else:
            future_days = half_days // 2

        if half_days > 0 and half_days % 2 != 0:
            unit = "AM" if unit == "PM" else "PM"

    new_time = str(total_hours) + ":"
    new_time += str(total_minutes) + f" {unit}"

    #GET START DAY + FUTURE DAY
    if args:
        day = args[0].title()
        if future_days > 0:
            DI = week.index(day)
            DI += future_days % 7
            if DI > 6:
                DI = DI - 7
            day = week[DI]

        new_time += f", {day}"

    #IF CHANGE IN DAY 
    if future_days == 1:
        new_time += " (next day)"
    elif future_days > 1:
        new_time += f" ({future_days} days later)".rjust(11)


    return new_time
