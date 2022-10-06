'''lets build a function to test the try '''

def test_try():
    numb = input('Enter a number: ')
    print(f'==> {numb}, {type(numb)}')

    try:
        num = float(numb)
        print(f'{num}, "{type(num)}" <== as you can see "num" got converted to a "float" ')
    except Exception as e:
        print('Exeption was: ', e)
    
test_try()