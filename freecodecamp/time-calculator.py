def add_time(start, duration, weekday=""):
    #SPLIT START
    unit_splited = start.split(" ")

    #SPLIT DURATION
    duration_splited = duration.split(":")

    #UNITS
    unit = ""
    day = (
        [0, "Monday"],
        [1, "Tuesday"],
        [2, "Wednesday"],
        [3, "Thursday"],
        [4, "Friday"],
        [5, "Saturday"],
        [6, "Sunday"]
    )
    base_hour = 0
    base_minutes = 0
    count_hour = 0 
    count_duration = 0
    count_day = 0
    sum_day = 0
    week = 0
    new_day = 0
    new_day2 = 0
    random_var = 0

    if weekday != "":
        for i in day:
            for text in i:
                if isinstance(text, str):
                    if weekday.lower() == text.lower():
                        sum_day = count_day
                        break
            count_day += 1
    
    new_day = count_day

    #START TIME
    for chars in unit_splited:
        for time_split in chars:
            #HOURS
            if time_split != ":" and time_split != "A" and time_split != "P" and time_split != "M" and count_hour < 3:
                if base_hour == 0:
                    base_hour += int(time_split)
                    count_hour += 1 # count_hour = 3
                elif count_hour < 2:
                    base_hour = str(base_hour) + str(time_split)
                    count_hour += 1 # count_hour = 2
                new_hour = int(base_hour)

            #SEPARATE HOURS FROM MINUTES  
            if time_split == ":":
                count_hour = 3

            #MINUTES
            if time_split != ":" and time_split != "A" and time_split != "P" and time_split != "M" and count_hour >= 3:
                if count_hour == 3:
                    base_minutes += int(time_split)
                    count_hour += 1
                else:
                    base_minutes = str(base_minutes) + str(time_split)
                    new_minutes = int(base_minutes)
            
        if chars == "AM":
            unit = chars
            if new_hour == 12:
                corrected_hour = 0
            else:
                corrected_hour = new_hour
        elif chars == "PM":
            unit = chars
            if new_hour == 12:
                corrected_hour = 12
            else:
                corrected_hour = new_hour + 12

    #DURATION TIME
    for char in duration_splited:
        if count_duration == 0:
            add_hour = int(char)
            count_duration += 1
        else:
            add_minutes = int(char)

    #SUM
    sum_hours = corrected_hour + add_hour
    sum_minutes = new_minutes + add_minutes

    #60 MINUTES FORMAT
    while sum_minutes >= 60:
        sum_minutes -=60
        sum_hours += 1

    #24 HOURS FORMAT
    while sum_hours >= 24:
        sum_hours -= 24
        sum_day += 1
        new_day2 += 1
        if sum_day >6:
            sum_day -= 6
            week += 1

    if len(str(sum_minutes)) == 1:
        corrected_minutes = "0" + str(sum_minutes)
    else:
        corrected_minutes = sum_minutes

    if sum_hours >= 12:
        sum_hours -= 12
        unit = "PM"
    else:
        unit = "AM"
        
    if sum_hours == 0:
        sum_hours = 12

    if weekday != "":
        sum_day_week = 0
        for day_week in day[sum_day]:
            if sum_day_week > 0:
                weekday = day_week
            else:
                new_weekday = (new_day2 // 6) - day_week
            sum_day_week += 1
        for name_day in day[new_weekday]:
            if random_var > 0:
                new_new_weekday = name_day
            random_var += 1



    if weekday and new_day2 >=2:
        new_time = print(f"\n{sum_hours}:{corrected_minutes} {unit}, {new_new_weekday} ({new_day2} days later)")
    elif weekday and new_day2 < 1:
        new_time = print(f"\n{sum_hours}:{corrected_minutes} {unit}, {new_new_weekday}")
    elif weekday == "" and new_day2 < 1:
        new_time = print(f"\n{sum_hours}:{corrected_minutes} {unit}")
    elif new_day2 >= 1 and new_day2 < 2:
        new_time = print(f"\n{sum_hours}:{corrected_minutes} {unit} (next day)")
    else:
        new_time = print(f"\n{sum_hours}:{corrected_minutes} {unit} ({new_day2} days later)")
        
    return new_time 





add_time("8:16 PM", "466:02", "tuesday")



