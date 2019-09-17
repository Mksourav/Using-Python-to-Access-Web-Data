import re
phone = input("Enter the number (xxx-xxx-xxxx)::")
# open('mbox-short.txt')
# dlist=list()
# while(1):
#     if(len(phone)==12):
#         for i in phone:
#             # line = line.rstrip()
#             stuff= re.findall('0-9', phone)
#             if len(stuff) != 1: continue
#             num = stuff[0]
#             dlist.append(num)
#         print('Maximum:', max(dlist))
#     else:
#         print("\nInvalid input!")
#         phone = input("Please enter the valid input::")

x = re.findall('\d{3}-\d{3}-\d{4}', phone)
if(len(phone) == 12 and len(x) == 1):
    print("Valid")
else:
    print("Invalid")
# print(x)
