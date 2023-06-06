def extented_euclidean_algo(a,b):
    if b==0:
        return a,1,0
    gcd,x1,y1=extented_euclidean_algo(b,a%b)
    x=y1
    y=x1-(a//b)*y1
    return gcd,x,y
def find_mod_inv(a,m):
    gcd,x,y=extented_euclidean_algo(a,m)
    if gcd!=1:
        raise ValueError("Inverse doesn't exist!")
    return x%m
a=int(input("Enter a number to find inverse : "))
m=int(input("Enter the number whose modulus is to be found : "))
inverse=find_mod_inv(a,m)
print("Modular inverse of",a,"mod",m,"is :",inverse)
