#linear search
ar=[3,90,12,8,4]
key=int(input("enter key: "))
for i in range(len(ar)):
	if ar[i]==key:
		print("key found at index", i)
		break
else:
    print("not found")

