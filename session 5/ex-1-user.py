def count_a(seq):
    result = 0
    for b in seq:
        if b == 'A':
            result += 1
    return result

s = input("Please,enter a valid code: ")

na = count_a(s)

print("The are {} As in the sequence".format(na))

tl = len(s)

if tl>0:
    perc=round (100.0 * na/tl,1)
else:
    perc=0

print("This sequence is {} bases in length".format(tl))

print("The percentages of As is {}%".format(round(100.0 * na/tl, 1)))

