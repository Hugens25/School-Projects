x = 5
y = 0

try:
    z = x/y
except:
    print("Cannot perform arithmetic")
finally:
    print(f"Did you mean {x}/1? This equals: {x}")
