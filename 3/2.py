n=int(input("till what range you want"))
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
m_a=set()
for i in range(1,n+1):
    m_a.add(a*i)
m_b=set()
for i in range(1,n+1):
    m_b.add(b*i)
lcm=m_a.intersection(m_b)
print("lcm is:",min(lcm))