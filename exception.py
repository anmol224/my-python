# try and except statements
#finally  will get executed whether we get an exception or not
a=10
b=7

try:
    print(a/b)
    a=int(input("enter a value"))


except ZeroDivisionError as e:
    print("you cannot divide number  by zero")

except ValueError as q:
    print("wrong input")

except Exception as i:
    print("something went wrong")
finally:
    print("execution completed")