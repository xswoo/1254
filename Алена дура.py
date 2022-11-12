'''print(maxim)
print(Hello)'''
try:
    print('start code')
    print(illia)
    print('no error')
except:
    print('Wave have an error')
print('кинець')
print('$$$$$$$$$$$$$$$$$$$$$$$$$')
try:
    print('start code')
    print(10/0)
    print('no error')
except NameError:
    print("we have an error NameError")
except ZeroDIvisionError:
    print("we have an error ZeroDIvisionError ")
print("кинець")
print('$$$$$$$$$$$$$$$$$$$$$$$$$')
try:
    print('start code')
    print(5/0)
    print('no error')
except (NameError, ZeroDivisionError) as error:
    print(error)
    print('$$$$$$$$$$$$$$$$$$$$$$$$$')
try:
    try:
        print('star code')
        print(error)
        print('no error')
    except SyntaxError:
        print("Wrong Syntax")
except NameError as error:
    print(error)
