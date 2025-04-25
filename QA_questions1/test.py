data = "devops     asdasdas  asdasdasd asdasdasd : asdasd asd"
s=""

print(data.title())
print(data.capitalize())
print(data.swapcase())
print("split retursn list" , data.split())
print("join retruns string fron joining list = "," ".join(data.split()))
print(data.find("z"))
# print(data.index("z")) throws error if not found
s2 = "banana apple banana banana"
print(s2.replace("banana", "orange", 2))  # "orange apple banana"


my_list = [10, 20, 30, 40]
print(my_list[1:3])
empty_list = []  # Empty list
list_from_tuple = list((1, 2, 3))  # Convert tuple to list

print(my_list[0])   # 10 (First element)
print(my_list[-1])  # 40 (Last element)
 # [20, 30] (Slicing)


# print(data.split(":"))
# for i in data:
#     print(i)
#
#
