#Write Python function to Implement Stack Operations using *args
def stack_operations(*args):
    stack = list(args)

    # Stack operations
    def push(item):
        stack.append(item)
        print(f"Pushed item: {item}")

    def pop():
        if not is_empty():
            item = stack.pop()
            print(f"Popped item: {item}")
        else:
            print("Stack is empty. Cannot perform pop operation.")

    def peek():
        if not is_empty():
            item = stack[-1]
            print(f"Top item: {item}")
        else:
            print("Stack is empty.")

    def is_empty():
        return len(stack) == 0

    push(10)
    push(20)
    push(30)
    peek()
    pop()
    peek()

stack_operations(1, 2, 3)
