exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_timestamp = exam_hour * 60 + exam_min
arrival_timestamp = arrival_hour * 60 + arrival_minute
diff = exam_timestamp - arrival_timestamp

if 0 <= diff <= 30:
    print("On time")
    if diff > 0:
        print(f"{diff} minutes before the start")
elif diff < 0:
    print("Late")
    diff_late = abs(diff)
    if diff_late <= 59:
        print(f"{diff_late} minutes after the start")
    elif diff_late >= 60:
        hours_diff = diff_late // 60
        mins_diff = diff_late % 60
        print(f"{hours_diff}:{mins_diff:02d} hours after the start")
elif diff > 30:
    print("Early")
    if diff <= 59:
        print(f"{diff} minutes before the start")
    elif diff >= 60:
        hours_diff = diff // 60
        mins_diff = diff % 60
        print(f"{hours_diff}:{mins_diff:02d} hours before the start")
