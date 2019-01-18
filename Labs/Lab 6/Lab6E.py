def show_time(hour,min):
    if hour == 0 and min == 0:
        hour = 12
        min = "00"
    elif min == 0:
        min = "00"
        
    if hour > 12:
        PMorAM = "pm"
        main_hour = hour - 12
    elif hour < 12:
        PMorAM = "am"
    if min < 10:
        main_min = "0{0}".format(min)
        
       
    print("{0}:{1}{2}".format(main_hour, main_min, PMorAM))
    ans = "{0}:{1}{2}".format(main_hour, main_min, PMorAM)
    return ans

show_time(22,5)
    