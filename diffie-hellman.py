p = int(input("enter prime p: "))
g = int(input("enter prime q: "))

a = int(input("enter alice priv key: "))
b = int(input("enter bob priv key: "))

A = pow(g,a,p)
B = pow(g,b,p)

KA = pow(B,a,p)
KB = pow(A,b,p)

print("alice public: ",A)
print("bob public: ",B)

print("alice shared secret : ", KA)
print("bob shared secret : ", KB)

if KA==KB:
    print("key exchange success")
else:
    print("unsuccess")