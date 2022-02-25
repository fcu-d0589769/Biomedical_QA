import csv
textline = []

a = 'abc'
print('' in a)
# with open('train.txt') as f:
#     for a in f.readlines():
#         if a == '\n':continue
#         elif a[:3] == '###': continue
#         elif a[:10] == 'BACKGROUND': a=a[10:]
#         elif a[:7] == 'METHODS': a=a[7:]
#         elif a[:7] == 'RESULTS': a=a[7:]
#         elif a[:11] == 'CONCLUSIONS': a=a[11:]
#         elif a[:9] == 'OBJECTIVE': a=a[9:]
#         #print(a.strip())
#         textline.append(a.strip())

# with open('biomedicine.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(textline)
# with open('biomedicine.csv', 'r', newline='') as csvfile:
#     rows = csv.reader(csvfile)

#     for r in rows:
#         print(len(r))
#         for a in r:
#             print(a)
#             break
        
