week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def add_time(start, duration, *args):
    [L, unit] = start.split(" ")
    [SH, SM] = L.split(":")
    [DH, DM] = duration.split(":")

    print(f"User Insputs: {start}, {duration}, {args}")
    print(f"Start: {SH}:{SM} {unit}\nDuration: {DH}:{DM}")
    print("\n")

    #SUM
    total_minutes = int(SM) + int(DM)
    total_hours = int(SH) + int(DH)
    future_days = 0

    if total_minutes >= 60:
        total_minutes -= 60
        total_hours +=1
    
    if total_minutes <10:
        total_minutes = f"{total_minutes}".zfill(2)

    print(f"Total Hours: {total_hours}\nTotal Minutes: {total_minutes}\nUnit: {unit}\nFuture Days: {future_days}")
    print("\n")
    
    #TODAY'S DAY
    if args:
        for day in week:
            if args[0].lower() == day.lower():
                print(f"Day: {day}\nIndex: {week.index(day)}")

add_time("5:55 PM", "1:05", "Sunday")