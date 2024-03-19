def fibonaci(n):
    sequence=[0, 1]
    for i in range (2, n):
        next_term = sequence[i-1] + sequence[i-2]
        sequence.append(next_term)
    return sequence[:n] #[:n] start the beginning of the list and include all the elements except of index n
    
nums =int(input('Enter the value of n: '))
fibonacci_sequence = fibonaci(nums)
print(f'the first {nums} terms in fibonacci sequence is: ',fibonacci_sequence)
