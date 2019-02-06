seq = input("Please,enter a valid code: ")
def count_bases(seq):
    print('This sequence is', len(seq), 'bases in lenght')
    count_A = 0
    count_C = 0
    count_G = 0
    count_T = 0
    for b in seq:
        if b == 'A':
                count_A += 1
        elif b == 'C':
                count_C += 1
        elif b == 'G':
                count_G += 1
        elif b == 'T':
                count_T += 1
    percentage_A = ((count_A / len(seq)) * 100)
    print('Base A')
    print('Counter:',count_A)
    print('Percentage:',percentage_A,'%')


    percentage_C = ((count_C / len(seq)) * 100)
    print('Base C')
    print('Counter:', count_C)
    print('Percentage',percentage_C,'%')


    percentage_G = ((count_G / len(seq)) * 100)
    print('Base G')
    print('Counter:', count_G)
    print('Percentage:',percentage_G,'%')


    percentage_T = ((count_T / len(seq)) * 100)
    print('Base T')
    print('Counter:', count_T)
    print('Percentage:',percentage_T,'%')
    return dict(A=count_A,C=count_C,G=count_G, T =count_T)
count_bases(seq)