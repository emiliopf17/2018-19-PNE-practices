N= input('Say the number that you want the sum: ')
N= int(N)
def sum(N):
    sum=0
    for i in range (N):
        sum=i sum+1
    print(sum)
sum(N)