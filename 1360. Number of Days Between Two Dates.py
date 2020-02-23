class Solution:
    def daysBetweenDates(self, date1, date2):
        def is_big_year(year):
            if(year % 100 == 0):
                return year % 400 == 0
            elif(year % 4 == 0):
                return True
            else:
                return False
        def calculate_days(year1, month1, day1, month2, day2):
            ans = 0
            if(month1 == month2):
            	return day2 - day1
            for i in range(month1 + 1, month2):
                if(i != 2):
                    ans += month_days[i]
                elif(is_big_year(year1)):
                    ans += 29
                else:
                    ans += 28
            ans += day2
            ans += month_days[month1] - day1
            if(is_big_year(year1) and month1 == 2):
                ans += 1
            return ans
        
        def calculate_year_days(year1, year2):
            ans = 0
            for i in range(year1, year2+1, 1):
                if(is_big_year(i)):
                    ans += 366
                else:
                    ans += 365
            return ans

        month_days = [0, 31,28,31,30,31,30,31,31,30,31,30,31]
        year1 = int(date1[0:4])
        month1 = int(date1[5:7])
        day1 = int(date1[8:10])
        year2 = int(date2[0:4])
        month2 = int(date2[5:7])
        day2 = int(date2[8:10])
        if(year1 > year2):
            temp = year1
            year1 = year2
            year2 = temp
            temp = month1
            month1 = month2
            month2 = temp
            temp = day1
            day1 = day2
            day2 = temp
        elif(year1 == year2):
            if(month1 > month2):
                temp = month1
                month1 = month2
                month2 = temp
                temp = day1
                day1 = day2
                day2 = temp
            elif(month1 == month2):
                if(day1 > day2):
                    temp = day1
                    day1 = day2
                    day2 = temp     
        if(year1 != year2):
        	ans = calculate_days(year1, month1, day1, 12, 31) + calculate_days(year2, 1, 1, month2, day2)
        	ans += calculate_year_days(year1 + 1, year2 - 1)
        	ans += 1
        else:
        	ans = calculate_days(year1, month1, day1, month2, day2)
        # ans = calculate_days(year1, month1, day1, former_year, former_month, former_day) + (year2, 1, 1, year2, month2, day2) + 1
        return ans
      