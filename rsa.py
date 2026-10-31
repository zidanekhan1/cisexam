from math import gcd

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d*e)%phi == 1:
            return d

    return None

p = int(input("enter first prime number p : "))
q = int(input("enter second prime number q : "))

n = p*q

phi = (p-1) * (q-1)

e = int(input("enter a value of e : "))

while gcd(e, phi) != 1:
    print("e must be coprime with : ", phi)
    e = int(input("enter another e"))

d = mod_inverse(e, phi)

print("\npublic key : ", (e,n))
print("private key : ", (d,n))

message = int(input("enter message : "))
cipher = pow(message, e, n)
print(cipher)
plain = pow(cipher, d, n)
print(plain)