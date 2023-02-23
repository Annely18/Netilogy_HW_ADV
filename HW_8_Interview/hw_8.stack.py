# Необходимо реализовать класс Stack со следующими методами:
# is_empty - проверка стека на пустоту. Метод возвращает True или False.
# push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
# pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
# peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
# size - возвращает количество элементов в стеке.

class Stack:

    def __init__(self):
        self.data = []

    def is_empty(self):
        if self.data:
            return True
        else:
            return False

    def push(self, el):
        self.data.append(el)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def size(self):
        return len(self.data)


# 2. Используя стек из задания 1 необходимо решить задачу на проверку сбалансированности скобок.
# Сбалансированность скобок означает, что каждый открывающий символ имеет соответствующий ему закрывающий,
# и пары скобок правильно вложены друг в друга.

def check_balance(arr):
    corr_parenth = {'}': '{', ')': '(', ']': '['}
    if len(arr) % 2 != 0 or arr[0] in corr_parenth:
        print('Несбалансированно')
    else:
        stack = Stack()
        for el in arr:
            if el in corr_parenth.values():
                stack.push(el)
            elif stack.data and el in corr_parenth and stack.peek() == corr_parenth[el]:
                stack.pop()

        if not stack.is_empty():
            print('Сбалансированно')
        else:
            print('Несбалансированно')


if __name__ == '__main__':

    a1 = '(((([{}]))))'
    a4 = '[([])((([[[]]])))]{()}'
    a2 = '[([])((([[[]]])))]'
    a3 = '{{[()]}}'
    b1 = '}{}'
    b2 = '{{[(])]}}'
    b3 = '[[{())}]'
    b4 = '}{}{'


    check_balance(b4)
    check_balance(a4)

