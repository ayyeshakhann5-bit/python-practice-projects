"""

def week_days(day):
    match day:
        case 1:
            return "sunday"
        case 2:
            return "momday"
        case _:
            return "Not a valid day"
          
print(week_days("pizza"))    

"""


def is_weekend(day):
    match day:
      case "Saturday" | "Sunday":
        return True
      case "Monday" | "Tuesday":
        return False
      case _:
        return False
      
print(is_weekend("saturday"))      
