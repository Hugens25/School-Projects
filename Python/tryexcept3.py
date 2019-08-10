'''
pylint practive script
'''

def ask():
    '''
    function takes input and squares the input
    '''
    while True:
        try:
            num = int(input("Please enter number to square: "))
            num = num**2
        except ValueError:
            print("Invalid number, please try again.")
        else:
            print(f"Thanks your new number is {num}. I hope this helped!")
            break
ask()
