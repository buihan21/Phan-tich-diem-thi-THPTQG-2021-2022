# p = input().strip().lstrip()
# l = p.split(':')
# print(l[1].strip().lstrip())

# res = []
# val = dict()
# for i in range(65):
#     p = input().strip().lstrip()
#     l = p.split(':')
#     st = l[0]
#     st.strip().lstrip()
#     l2 = st.split('–')
#     ma = l2[0]
#     tinh = l2[1]
#     print(ma, tinh, sep=" ")
#     val[ma] = tinh
#
# for x in val:
#     print(x, val[x], sep=" ")
# import re
#
#
# for i in range(64):
#     p = input().strip().lstrip()
#     Arr = re.split('[:-]', p)
#     print(Arr)

# new_dict = {'ma' : 'tinh'}
# for i in range(64):
#     p = input().strip().lstrip()
#     l = p.split(" ", 1)
#     ma = l[0].strip().lstrip()
#     tinh = l[-1].strip().lstrip()
#     new_dict[ma] = tinh
#
# print(new_dict)

# import shutil
#
# with open('output_file.txt','wb') as wfd:
#     for f in ['1.txt','2.txt','3.txt','4.txt','5.txt','6.txt','7.txt','8.txt','9.txt','10.txt','11.txt','12.txt',
#               '13.txt','14.txt','15.txt','16.txt','17.txt','18.txt','19.txt','20.txt','21.txt','22.txt','23.txt',
#               '24.txt','25.txt','26.txt','27.txt','28.txt','29.txt','30.txt','31.txt','32.txt','33.txt','34.txt',
#               '35.txt','36.txt','37.txt','38.txt','39.txt','40.txt','41.txt','42.txt','43.txt','44.txt','45.txt',
#               '46.txt','47.txt','48.txt','49.txt','50.txt','51.txt','52.txt','53.txt','54.txt','55.txt','56.txt',
#               '57.txt','58.txt','59.txt','60.txt','61.txt','62.txt','63.txt','64.txt']:
#         with open(f,'rb') as fd:
#             shutil.copyfileobj(fd, wfd.write()

# for i in range(1,65):
#     print("'",i,".txt'", sep='', end=',')



# Gộp các file.xlsx thành 1 file duy nhất => chuyển về file.csv = Execl
# import pandas as pd
# import glob
#
# path = "C:/Users/laptop/PycharmProjects/PTDLThiTNQG/data2021"
#
# file_list = glob.glob(path + "/*.xlsx")
# excel_list = []
#
# for file in file_list:
#     excel_list.append(pd.read_excel(file))
# excel_merged = pd.concat(excel_list, ignore_index=True)
# excel_merged.to_excel('DATA.xlsx', index=False)

