months = ('January', 'February', 'March', 'April', 'May', 'June', 'July',\
          'August', 'September', 'October', 'November', 'December')

def problem3_3(month, day, year):

    int(month)
    month = months[month-1]
    m = str(month)
    d = str(day)
    y = str(year)
  
    print(m +' '+ d+',',year)

