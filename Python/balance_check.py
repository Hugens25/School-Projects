def balance_check(s):
    parens = {'[':']', '{':'}', '(':')', ']':'[', '}':'{', ')':'('}
    stack = []
    if len(s) % 2 != 0:
        return False


    for char in s:
        if len(stack) != 0 and char == stack[0]:
            stack.pop(0)
            continue
        stack.insert(0, parens[char])
    return len(stack) == 0



print(balance_check("()[]{[{([{}])}]}({})"))
