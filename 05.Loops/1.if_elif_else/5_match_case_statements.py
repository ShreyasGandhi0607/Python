ch = int(input("Enter ur choice : "))
match ch:
    case 1:
        print("Hello")
    case 2:
        print("Hi")
    case _ if ch == 3:
        print(ch, " is ur choice")
    case 4:
        print("Bye")
    case 5:
        print("Good Night")



