def valid(string):
    open_brackets = ('(', '[', '{')
    close_brackets = (')', ']', '}')
    #Заводим стек, в котором будем хранить скобки, встретившиеся в имеющемся выражении
    stack = []
    for symbol in string:
        #Если символ выражения - открывающая скобка, кладём ее в стек
        if symbol in open_brackets:
            stack.append(symbol)
        #Если символ выражения - закрывающая скобка и если при этом стек пуст, 
        # значит первая ск. в выражении - закрывающая ( возвращаем False)
        if symbol in close_brackets:    
            if len(stack) == 0:
                return False
            #Для закрывающей ск. находим аналогичную открывающую (АО)
            index = close_brackets.index(symbol)
            bracket_open = open_brackets[index]
            #Если АО - последняя, удаляем ее из стека. Скобки валидны, если в итоге стек пуст.
            if stack[-1] == bracket_open:
                stack = stack[:-1]
                
            else: return False  
    return (not stack)


str1 = input('Введите выражение со скобками:')
print(valid(str1))