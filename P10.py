#10. python program to display all integers within the range of 100 - 200 whose sum of digits is an even no.
for i in range(100,200):
    temp=i
    summ=0
    while(temp!=0):
        digit=temp%10
        summ=summ+digit
        temp=temp//10
    if (summ%2==0):
        print(i)
