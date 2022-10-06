'''Learning to format print() function '''
name = '"Teddy" Rossevelt'
name1 = 'Theodore "Teddy" Roosevelt'
age = 60
wt = 199.151515

# minimal formatting ..... {n} represent data item n --- notice misalignment
out1 = 'name: {0} age: {1} weight: {2}'

print('\nname: {0} age: {1} weight: {2}'.format(name,age,wt))
print('name: {0} age{1} weight: {2}'.format(name1,age,wt))

print('\n==================================================================================\n')

'''better formatting > means right align (< end ^ would be left and center )
   the numbers represent the minimum characters accupied by the datum'''
   
'''here we can declare how we want to formatting to look like or we can do it all inside the print() function'''
out2 = 'name: {0: >26} age: {1: >2} weight: {2: >10.2f}'
'''we can use the string variable out2, like so'''
print(out2.format(name1,age,wt))
#print('name: {0: >26} age: {1: >2} weight: {2: >10.2f}.format(name,age,wt')
print(out2.format(name,age,wt))
# here we can formatt the decimal places of weight to two 
print(out2.format(name1,age,wt))

print('\n==================================================================================\n')
s = 'my short string'
n = 5.1234
print('Start|| {0:25} ||End'.format(s))# strings are left justify
print('Start|| {0:25} ||End'.format(n)) #Number are right justify

print('\n==================================================================================\n')

'''Practice the string format '''

prt = 'Hello, there'
out2 = 'phrase: {0}'

'''the format statement to modify and work with'''

print('Start||{}||End'.format(prt))
print('Start||{:25}||End'.format(prt))# minimum width 25
print('Start||{0: >25}||End'.format(prt))# width 25, right aligned
print('Start||{0: <25}||End'.format(prt))# width 25, left aligned
print('Start||{0: ^25}||End'.format(prt))# width 25, center