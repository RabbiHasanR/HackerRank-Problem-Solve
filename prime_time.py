def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True
# print(test_prime(25))
# print([0]*256)
ount1=[0]*52
ount2=[0]*52
print(ount1)
print(ount2)