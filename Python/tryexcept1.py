for i in ['a','b','c','d']:
    try:
        print (i**2)
    except TypeError:
        print("Invalid Type")
    except:
        print("Something went wrong")
    
