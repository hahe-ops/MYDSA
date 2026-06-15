m=int(input("enter lenght"))
n=int(input("enter width"))
print("*" * n)

for j in range(m-2):
    print("*" + " " * (m-2) + "*")

print("*" * n)
