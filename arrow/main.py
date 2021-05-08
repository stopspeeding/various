import arrow

utc = arrow.utcnow()


def timeq():
    choice = input("What is your timezone? e for Eastern or p for pacific").lower()
    if choice == 'e':
        local = utc.to('US/Eastern')
        local.format('hh:mm:ss a ZZ')
        print("The date and time in your timezone is: ")
        print(local.format())
    elif choice == 'p':
        local = utc.to('US/Pacific')
        local.format('hh:mm:ss a ZZ')
        print("The date and time is: ")
        print(local.format())
    else:
        print("invalid input, try again.")
        timeq()


timeq()
