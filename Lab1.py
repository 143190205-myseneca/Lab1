def inputToAge():
    try:
        age = int(input("Please enter your age"))
        return age
    except ValueError:
        print("Invalid Input, please use an integer!")
        return None


def helloWorld():
	print("Hello World")


helloWorld()


