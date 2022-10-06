

phone_numbers = {"abbie":"(860) 123-4535", "beverly":"(901) 454-3241",\
                 "james": "(212) 567-8149", "thomas": "(795) 342-9145"}

def problem3_5(name):
    key = phone_numbers.get(name)
    print(key)
    # for value in name:
    #      print(value,end='')
    # key = phone_numbers.get(name)
    # print(value, key, end='')
       
  
problem3_5('beverly')