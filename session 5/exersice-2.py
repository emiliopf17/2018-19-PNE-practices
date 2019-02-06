seq1 = input("Please,enter a seq: ")
seq2 = input("Please,enter another seq: ")
def count_bases(seq1,seq2):
    print("Sequence 1")
    print('This sequence is', len(seq1), 'bases  lenght')
    count_A1 = 0
    count_C1 = 0
    count_G1 = 0
    count_T1 = 0
    for b in seq1:
        if b == 'A':
                count_A1 += 1
        elif b == 'C':
                count_C1 += 1
        elif b == 'G':
                count_G1 += 1
        elif b == 'T':
                count_T1 += 1
    percentage_A1 = ((count_A1 / len(seq1)) * 100)
    print('Base A')
    print('Counter:',count_A1)
    print('Percentage:',percentage_A1,'%')


    percentage_C1 = ((count_C1 / len(seq1)) * 100)
    print('Base C')
    print('Counter:', count_C1)
    print('Percentage',percentage_C1,'%')


    percentage_G1 = ((count_G1 / len(seq1)) * 100)
    print('Base G')
    print('Counter:', count_G1)
    print('Percentage:',percentage_G1,'%')


    percentage_T1 = ((count_T1 / len(seq1)) * 100)
    print('Base T')
    print('Counter:', count_T1)
    print('Percentage:',percentage_T1,'%')

    print("Sequence 2")
    print('This sequence is', len(seq2), 'bases  lenght')
    count_A2 = 0
    count_C2 = 0
    count_G2 = 0
    count_T2 = 0
    for c in seq2:
        if c == 'A':
                count_A2 += 1
        elif c == 'C':
                count_C2 += 1
        elif c == 'G':
                count_G2 += 1
        elif c == 'T':
                count_T2 += 1


    percentage_A2 = ((count_A2 / len(seq2)) * 100)
    print('Base A')
    print('Counter:',count_A2)
    print('Percentage:',percentage_A2,'%')


    percentage_C2 = ((count_C2 / len(seq2)) * 100)
    print('Base C')
    print('Counter:', count_C2)
    print('Percentage',percentage_C2,'%')


    percentage_G2 = ((count_G2 / len(seq2)) * 100)
    print('Base G')
    print('Counter:', count_G2)
    print('Percentage:',percentage_G2,'%')


    percentage_T2 = ((count_T2 / len(seq2)) * 100)
    print('Base T')
    print('Counter:', count_T2)
    print('Percentage:',percentage_T2,'%')
    return dict(A1=count_A1,  A2=count_A2,   C1=count_C1, C2=count_C2,   G1=count_G1,   G2=count_G2, T1 =count_T1,  T2 =count_T2)
count_bases(seq1,seq2)