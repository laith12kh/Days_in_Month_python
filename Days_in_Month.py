# we have to write a function that resivice from the user year and moth and returns how many days where in that month
# example year 2022 month 2 => the outpot will be 28 days

# this function checks if the year is leap or not 
def check_if_leap(year):
    if year % 4 == 0 :
        if year % 100 == 0 :
            if year % 400 == 0 :
                return True
            else :
                return False
        else :
            return True
    else : 
        return False


# this is the function that we need to write
def check_days_in_month(year_to_check,month_to_check):
    amount_of_days_in_month=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if check_if_leap(year_to_check) and month_to_check == 2 :
        return 29
    return amount_of_days_in_month[month_to_check - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = check_days_in_month(year, month)
print(days)
      