""" This is an addition"""



def calculator(operator, numbers):
    """this is a calculator"""
    answer = 0

    if operator == 'addition':
        for element in numbers:
            answer += element

    if operator == 'multiply':
        answer = 1
        for element in numbers:
            answer *= element

    if operator == 'subtract':
        first = True
        for element in numbers:
            if first:
                answer = element
                first = not first
            else:
                answer -= element

    if operator == 'divide':
        first = True
        for element in numbers:
            if first:
                answer = element
                first = not first
            else:
                answer = answer / element

    return answer


numbers = [9, 3]
print(calculator("divide", numbers))
