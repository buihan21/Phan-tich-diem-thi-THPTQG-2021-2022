import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
desired_width = 320
pd.set_option('display.width', desired_width)

# Xoá cột rỗng: "Tên", "Ngày Sinh", "Giới tính"
diem_2021_df = pd.read_csv('DATA_2021.csv')
diem_2021_df = diem_2021_df.drop(diem_2021_df.columns[[1,2,3]], axis=1)

# Chuẩn hoá tên các môn học
diem_2021_df = diem_2021_df.rename(columns={'Văn':'Ngữ văn', 'Lý':'Vật lý', 'Hoá':'Hoá học','Sinh':'Sinh học',
                                            'Lịch Sử':'Lịch sử','Địa Lý':'Địa lý','Ngoại Ngữ':'Ngoại ngữ'})

# Tính điểm tổ hợp "KHTN" & "KHXH"
diem_2021_df['KHTN'] = round((diem_2021_df['Vật lý'] + diem_2021_df['Hoá học'] + diem_2021_df['Sinh học']) / 3, 2)
diem_2021_df['KHXH'] = round((diem_2021_df['Lịch sử'] + diem_2021_df['Địa lý'] + diem_2021_df['GDCD']) / 3, 2)

# Tạo cột "Tỉnh thành" dựa trên SBD
temp = {'1': 'TP HÀ NỘI', '2': 'TP HỒ CHÍ MINH', '3': 'TP HẢI PHÒNG', '4': 'TP ĐÀ NẴNG', '5': 'HÀ GIANG',
        '6': 'CAO BẰNG', '7': 'LAI CHÂU', '8': 'LÀO CAI', '9': 'TUYÊN QUANG', '10': 'LẠNG SƠN',
        '11': 'BẮC KẠN', '12': 'THÁI NGUYÊN', '13': 'YÊN BÁI', '14': 'SƠN LA', '15': 'PHÚ THỌ',
        '16': 'VĨNH PHÚC', '17': 'QUẢNG NINH', '18': 'BẮC GIANG', '19': 'BẮC NINH',
        '21': 'HẢI DƯƠNG', '22': 'HƯNG YÊN', '23': 'HÒA BÌNH', '24': 'HÀ NAM',
        '25': 'NAM ĐỊNH', '26': 'THÁI BÌNH', '27': 'NINH BÌNH', '28': 'THANH HÓA',
        '29': 'NGHỆ AN', '30': 'HÀ TĨNH',
        '31': 'QUẢNG BÌNH', '32': 'QUẢNG TRỊ', '33': 'THỪA THIÊN - HUẾ', '34': 'QUẢNG NAM',
        '35': 'QUẢNG NGÃI', '36': 'KON TUM', '37': 'BÌNH ĐỊNH', '38': 'GIA LAI',
        '39': 'PHÚ YÊN', '40': 'ĐẮK LẮK',
        '41': 'KHÁNH HÒA', '42': 'LÂM ĐỒNG', '43': 'BÌNH PHƯỚC', '44': 'BÌNH DƯƠNG',
        '45': 'NINH THUẬN', '46': 'TÂY NINH', '47': 'BÌNH THUẬN', '48': 'ĐỒNG NAI',
        '49': 'LONG AN', '50': 'ĐỒNG THÁP',
        '51': 'AN GIANG', '52': 'BÀ RỊA', '53': 'TIỀN GIANG', '54': 'KIÊN GIANG',
        '55': 'TP CẦN THƠ', '56': 'BẾN TRE', '57': 'VĨNH LONG', '58': 'TRÀ VINH', '59': 'SÓC TRĂNG',
        '60': 'BẠC LIÊU',
        '61': 'CÀ MAU', '62': 'ĐIỆN BIÊN', '63': 'ĐĂK NÔNG', '64': 'HẬU GIANG'}
location = []
location = np.floor(diem_2021_df['SBD'] // 10 ** 6)
location = location.astype(int)

tinhThanh = []
for i in range(len(location)):
        tmp = str(location[i])
        tinhThanh.append(temp.get(tmp))
diem_2021_df['Tỉnh thành'] = tinhThanh

# Chuyển cột "Tỉnh thành" từ cuối lên sau cột "SBD"
column_to_move = diem_2021_df.pop('Tỉnh thành')
diem_2021_df.insert(1, 'Tỉnh thành', column_to_move)

# Tính điểm tốt nghiệp
diem_theo_khtn = (diem_2021_df['Toán']+diem_2021_df['Ngữ văn']+diem_2021_df['Ngoại ngữ']+diem_2021_df['KHTN']) / 4
diem_theo_khxh = (diem_2021_df['Toán']+diem_2021_df['Ngữ văn']+diem_2021_df['Ngoại ngữ']+diem_2021_df['KHXH']) / 4
diem_2021_df['Điểm tốt nghiệp'] = pd.DataFrame({'KHTN':diem_theo_khtn, 'KHXH':diem_theo_khxh}).max(axis=1)
diem_2021_df.dropna(subset=['Điểm tốt nghiệp'], inplace=True)

# Tính điểm tốt nghiệp trung bình, cao nhất và thấp nhất ở các tỉnh thành
diem_2021_mean = diem_2021_df.groupby('Tỉnh thành')['Điểm tốt nghiệp'].mean()
diem_2021_max = diem_2021_df.groupby('Tỉnh thành')['Điểm tốt nghiệp'].max()
diem_2021_min = diem_2021_df.groupby('Tỉnh thành')['Điểm tốt nghiệp'].min()
infor_2021 = pd.DataFrame({'Điểm tốt nghiệp trung bình':diem_2021_mean,
                           'Điểm tốt nghiệp cao nhất':diem_2021_max,
                           'Điểm tốt nghiệp thấp nhất':diem_2021_min})
# pd.set_option('display.max_columns', None)
# print(infor_2021)

# Liệt kê 5 tỉnh có điểm trung bình cao nhất, điểm tốt nghiệp cao nhất, và điểm thấp thấp nhất
index_max = [-1, -2, -3, -4, -5] # Ngược lại so với read data 2022.py
top5_tb_max = infor_2021['Điểm tốt nghiệp trung bình'].sort_values()[index_max].index
top5_tb_min = infor_2021['Điểm tốt nghiệp trung bình'].sort_values()[0:5].index
top5_infor2021_df = pd.DataFrame({'Điểm tốt nghiệp trung bình cao nhất': top5_tb_max,
                                  'Điểm tốt nghiệp trung bình thấp nhất': top5_tb_min})
# pd.set_option('display.max_columns', None)
# print(top5_infor2021_df)


# Tính điểm liệt mỗi tỉnh, quy định điểm liệt là từ điểm 1 trở xuống
diem_liet_toan = diem_2021_df[diem_2021_df['Toán'] <= 1]['Tỉnh thành'].value_counts()
diem_liet_van = diem_2021_df[diem_2021_df['Ngữ văn'] <= 1]['Tỉnh thành'].value_counts()
diem_liet_ngoaingu = diem_2021_df[diem_2021_df['Ngoại ngữ'] <= 1]['Tỉnh thành'].value_counts()
diem_liet_hoa = diem_2021_df[diem_2021_df['Hoá học'] <= 1]['Tỉnh thành'].value_counts()
diem_liet_sinh = diem_2021_df[diem_2021_df['Sinh học'] <= 1]['Tỉnh thành'].value_counts()
diem_liet_ly = diem_2021_df[diem_2021_df['Vật lý'] <= 1]['Tỉnh thành'].value_counts()
diem_liet_dia = diem_2021_df[diem_2021_df['Địa lý'] <= 1]['Tỉnh thành'].value_counts()
diem_liet_su = diem_2021_df[diem_2021_df['Lịch sử'] <= 1]['Tỉnh thành'].value_counts()
diem_liet_gdcd = diem_2021_df[diem_2021_df['GDCD'] <= 1]['Tỉnh thành'].value_counts()
diem_liet_df = pd.DataFrame({'Toán học':diem_liet_toan,'Ngữ văn':diem_liet_van,'Ngoại ngữ':diem_liet_ngoaingu,
                             'Hoá học':diem_liet_hoa,'Vật lý':diem_liet_ly,'Sinh học':diem_liet_sinh,
                             'Địa lý':diem_liet_dia,'Lịch sử':diem_liet_su,'GDCD':diem_liet_gdcd})
diem_liet_df = diem_liet_df.replace(np.nan,0)
# pd.set_option('display.max_columns', None)
# print(diem_liet_df)

# Liệt kê 5 tỉnh mà số lượng điểm liệt cao
top5_liet_toan = diem_liet_df['Toán học'].sort_values()[index_max].index
top5_liet_van = diem_liet_df['Ngữ văn'].sort_values()[index_max].index
top5_liet_nn = diem_liet_df['Ngoại ngữ'].sort_values()[index_max].index
top5_liet_hoa = diem_liet_df['Hoá học'].sort_values()[index_max].index
top5_liet_ly = diem_liet_df['Vật lý'].sort_values()[index_max].index
top5_liet_sinh = diem_liet_df['Sinh học'].sort_values()[index_max].index
top5_liet_dia = diem_liet_df['Địa lý'].sort_values()[index_max].index
top5_liet_su = diem_liet_df['Lịch sử'].sort_values()[index_max].index
top5_liet_gdcd = diem_liet_df['GDCD'].sort_values()[index_max].index
top5_diemliet_df = pd.DataFrame({'Toán học':top5_liet_toan,'Ngữ văn':top5_liet_van,'Ngoại ngữ':top5_liet_nn,
                                 'Hoá học':top5_liet_hoa,'Vật lý':top5_liet_ly,'Sinh học':top5_liet_sinh,
                                 'Địa lý':top5_liet_dia,'Lịch sử':top5_liet_su,'GDCD':top5_liet_gdcd})
# pd.set_option('display.max_columns', None)
# print(top5_diemliet_df)


# Tính điểm cao theo từng môn của từng tỉnh
point = 8
diem_cao_toan = diem_2021_df[diem_2021_df['Toán'] >= point]['Tỉnh thành'].value_counts()/diem_2021_df.groupby('Tỉnh thành')['Toán'].count()
diem_cao_van = diem_2021_df[diem_2021_df['Ngữ văn'] >= point]['Tỉnh thành'].value_counts()/diem_2021_df.groupby('Tỉnh thành')['Ngữ văn'].count()
diem_cao_nn = diem_2021_df[diem_2021_df['Ngoại ngữ'] >= point]['Tỉnh thành'].value_counts()/diem_2021_df.groupby('Tỉnh thành')['Ngoại ngữ'].count()
diem_cao_hoa = diem_2021_df[diem_2021_df['Hoá học'] >= point]['Tỉnh thành'].value_counts()/diem_2021_df.groupby('Tỉnh thành')['Hoá học'].count()
diem_cao_ly = diem_2021_df[diem_2021_df['Vật lý'] >= point]['Tỉnh thành'].value_counts()/diem_2021_df.groupby('Tỉnh thành')['Vật lý'].count()
diem_cao_sinh = diem_2021_df[diem_2021_df['Sinh học'] >= point]['Tỉnh thành'].value_counts()/diem_2021_df.groupby('Tỉnh thành')['Sinh học'].count()
diem_cao_dia = diem_2021_df[diem_2021_df['Địa lý'] >= point]['Tỉnh thành'].value_counts()/diem_2021_df.groupby('Tỉnh thành')['Địa lý'].count()
diem_cao_su = diem_2021_df[diem_2021_df['Lịch sử'] >= point]['Tỉnh thành'].value_counts()/diem_2021_df.groupby('Tỉnh thành')['Lịch sử'].count()
diem_cao_gdcd = diem_2021_df[diem_2021_df['GDCD'] >= point]['Tỉnh thành'].value_counts()/diem_2021_df.groupby('Tỉnh thành')['GDCD'].count()
diem_cao_df = pd.DataFrame({'Toán học':diem_cao_toan,'Ngữ văn':diem_cao_van,'Ngoại ngữ':diem_cao_nn,
                            'Hoá học':diem_cao_hoa,'Vật lý':diem_cao_ly,'Sinh học':diem_cao_sinh,
                            'Địa lý':diem_cao_dia,'Lịch sử':diem_cao_su,'GDCD':diem_cao_gdcd})
diem_cao_df = diem_cao_df.replace(np.nan,0)
# pd.set_option('display.max_columns', None)
# print(diem_cao_df)

# 5 tỉnh điểm cao nhất theo từng môn
top5_cao_toan = diem_cao_df['Toán học'].sort_values()[index_max].index
top5_cao_van = diem_cao_df['Ngữ văn'].sort_values()[index_max].index
top5_cao_nn = diem_cao_df['Ngoại ngữ'].sort_values()[index_max].index
top5_cao_hoa = diem_cao_df['Hoá học'].sort_values()[index_max].index
top5_cao_ly = diem_cao_df['Vật lý'].sort_values()[index_max].index
top5_cao_sinh = diem_cao_df['Sinh học'].sort_values()[index_max].index
top5_cao_dia = diem_cao_df['Địa lý'].sort_values()[index_max].index
top5_cao_su = diem_cao_df['Lịch sử'].sort_values()[index_max].index
top5_cao_gdcd = diem_cao_df['GDCD'].sort_values()[index_max].index
top5_diemcao_df = pd.DataFrame({'Toán':top5_cao_toan,'Ngữ văn':top5_cao_van,'Ngoại ngữ':top5_cao_nn,
                                'Hoá học':top5_cao_hoa,'Vật lý':top5_cao_ly,'Sinh học':top5_cao_sinh,
                                'Địa lý':top5_cao_dia,'Lịch sử':top5_cao_su,'GDCD':top5_cao_gdcd})
pd.set_option('display.max_columns', None)
print(top5_diemcao_df)

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# print(diem_2021_df)
