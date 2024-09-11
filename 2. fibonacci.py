def fibonacci(number):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < number:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    if number in fib_sequence:
        print("Pertence")
    else:
        print("Não pertence")

fibonacci(35)
fibonacci(34)
fibonacci(55)