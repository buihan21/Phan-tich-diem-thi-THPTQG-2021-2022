import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
desired_width = 320
pd.set_option('display.width', desired_width)


diem2022_df = pd.read_csv('DATA_2022.csv')

diem2022_df = diem2022_df.rename(
    columns={'sbd': 'SBD', 'ngu_van': 'Ngữ văn', 'toan': 'Toán', 'ngoai_ngu': 'Ngoại ngữ', 'vat_li': 'Vật lý',
             'hoa_hoc': 'Hoá học', 'sinh_hoc': 'Sinh học', 'lich_su': 'Lịch sử', 'dia_li': 'Địa lý', 'gdcd': 'GDCD'})
diem2022_df['KHTN'] = round((diem2022_df['Hoá học'] + diem2022_df['Vật lý'] + diem2022_df['Sinh học']) / 3, 2)
diem2022_df['KHXH'] = round((diem2022_df['Địa lý'] + diem2022_df['Lịch sử'] + diem2022_df['GDCD']) / 3, 2)

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
location = np.floor(diem2022_df['SBD'] // 10 ** 6)
location = location.astype(int)

tinhThanh = []
for i in range(len(location)):
        tmp = str(location[i])
        tinhThanh.append(temp.get(tmp))
diem2022_df['Tỉnh thành'] = tinhThanh

diem2022_df = pd.DataFrame({'SBD':diem2022_df['SBD'],'Tỉnh thành':diem2022_df['Tỉnh thành'],'Toán':diem2022_df['Toán'],
                            'Ngữ văn':diem2022_df['Ngữ văn'],'Vật lý':diem2022_df['Vật lý'],'Hoá học':diem2022_df['Hoá học'],
                            'Sinh học':diem2022_df['Sinh học'], 'KHTN':diem2022_df['KHTN'],'Lịch sử':diem2022_df['Lịch sử'],
                            'Địa lý':diem2022_df['Địa lý'],'GDCD':diem2022_df['GDCD'], 'KHXH':diem2022_df['KHXH'], 'Ngoại ngữ':diem2022_df['Ngoại ngữ']})

# Tính điểm tốt nghiệp
diem_khtn = (diem2022_df['Toán']+diem2022_df['Ngữ văn']+diem2022_df['Ngoại ngữ'] + diem2022_df['KHTN']) / 4
diem_khxh = (diem2022_df['Toán']+diem2022_df['Ngữ văn']+diem2022_df['Ngoại ngữ'] + diem2022_df['KHXH']) / 4
diem2022_df['Điểm tốt nghiệp'] = pd.DataFrame({'KHTN':diem_khtn, 'KHXH':diem_khxh}).max(axis=1)
diem2022_df.dropna(subset=['Điểm tốt nghiệp'], inplace=True)

# Tính điểm tốt nghiệp trung bình, cao nhất và thấp nhất ở các tỉnh thành
diem2022_mean = diem2022_df.groupby('Tỉnh thành')['Điểm tốt nghiệp'].mean()
diem2022_max = diem2022_df.groupby('Tỉnh thành')['Điểm tốt nghiệp'].max()
diem2022_min = diem2022_df.groupby('Tỉnh thành')['Điểm tốt nghiệp'].min()
infor_2022 = pd.DataFrame({'Điểm tốt nghiệp trung bình':diem2022_mean, 'Điểm tốt nghiệp cao nhất':diem2022_max, 'Điểm tốt nghiệp thấp nhất':diem2022_min})
# pd.set_option('display.max_columns', None)
# print(infor_2022)
# print(infor_2022.loc['NAM ĐỊNH'])

# Liệt kê 5 tỉnh có điểm trung bình cao nhất, điểm tốt nghiệp cao nhất, và điểm thấp thấp nhất
index_max = [-5, -4, -3, -2, -1] # mảng index để lấy các index max
top5_tb_max = infor_2022['Điểm tốt nghiệp trung bình'].sort_values()[index_max].index
top5_tb_min = infor_2022['Điểm tốt nghiệp trung bình'].sort_values()[0:5].index
top5_tb1 = infor_2022['Điểm tốt nghiệp trung bình']
top5_infor2022_df = pd.DataFrame({'Điểm tốt nghiệp trung bình cao nhất':top5_tb_max,
                                  'Điểm tốt nghiệp trung bình thấp nhất':top5_tb_min})
# pd.set_option('display.max_columns', None)
# print(top5_infor2022_df)

# Tính điểm liệt mỗi tỉnh, quy định điểm liệt là điểm từ 1 trở xuống
diem_liet_toan = diem2022_df[diem2022_df['Toán'] <= 1]['Tỉnh thành'].value_counts()
diem_liet_van = diem2022_df[diem2022_df['Ngữ văn'] <= 1]['Tỉnh thành'].value_counts()
diem_liet_ngoaiNgu = diem2022_df[diem2022_df['Ngoại ngữ'] <= 1]['Tỉnh thành'].value_counts()
diem_liet_hoa = diem2022_df[diem2022_df['Hoá học'] <= 1]['Tỉnh thành'].value_counts()
diem_liet_sinh = diem2022_df[diem2022_df['Sinh học'] <= 1]['Tỉnh thành'].value_counts()
diem_liet_ly = diem2022_df[diem2022_df['Vật lý'] <= 1]['Tỉnh thành'].value_counts()
diem_liet_dia = diem2022_df[diem2022_df['Địa lý'] <= 1]['Tỉnh thành'].value_counts()
diem_liet_su = diem2022_df[diem2022_df['Lịch sử'] <= 1]['Tỉnh thành'].value_counts()
diem_liet_gdcd = diem2022_df[diem2022_df['GDCD'] <= 1]['Tỉnh thành'].value_counts()
diem_liet_df = pd.DataFrame({'Toán học':diem_liet_toan,'Ngữ văn':diem_liet_van,'Ngoại ngữ':diem_liet_ngoaiNgu,
                             'Hoá học':diem_liet_hoa,'Vật lý':diem_liet_ly,'Sinh học':diem_liet_sinh,
                            'Địa lý':diem_liet_dia,'Lịch sử':diem_liet_su,'GDCD':diem_liet_gdcd})
diem_liet_df = diem_liet_df.replace(np.nan, 0)
# pd.set_option('display.max_columns', None)
# print(diem_liet_df)

# Liệt kê top 5 tỉnh có nhiều điểm liệt nhiều nhất theo từng môn học
top5_liet_toan = diem_liet_df['Toán học'].sort_values()[index_max].index
top5_liet_van = diem_liet_df['Ngữ văn'].sort_values()[index_max].index
top5_liet_nn = diem_liet_df['Ngoại ngữ'].sort_values()[index_max].index
top5_liet_hoa = diem_liet_df['Hoá học'].sort_values()[index_max].index
top5_diem_ly = diem_liet_df['Vật lý'].sort_values()[index_max].index
top5_liet_sinh = diem_liet_df['Sinh học'].sort_values()[index_max].index
top5_liet_dia = diem_liet_df['Địa lý'].sort_values()[index_max].index
top5_liet_su = diem_liet_df['Lịch sử'].sort_values()[index_max].index
top5_liet_gdcd = diem_liet_df['GDCD'].sort_values()[index_max].index
top5_diemliet_df = pd.DataFrame({'Toán':top5_liet_toan,'Ngữ văn':top5_liet_van,'Ngoại ngữ':top5_liet_nn,
                                 'Hoá học':top5_liet_hoa,'Vật lý':top5_diem_ly,'Sinh học':top5_liet_sinh,
                                 'Địa lý':top5_liet_dia,'Lịch sử':top5_liet_su,'GDCD':top5_liet_gdcd})
# pd.set_option('display.max_columns', None)
# print(top5_diemliet_df)

# Tính điểm cao theo từng môn của từng tỉnh
point = 8
diemcao_toan = diem2022_df[diem2022_df['Toán'] >= point]['Tỉnh thành'].value_counts()/diem2022_df.groupby('Tỉnh thành')['Toán'].count()
diemcao_van = diem2022_df[diem2022_df['Ngữ văn'] >= point]['Tỉnh thành'].value_counts()/diem2022_df.groupby('Tỉnh thành')['Ngữ văn'].count()
diemcao_nn = diem2022_df[diem2022_df['Ngoại ngữ'] >= point]['Tỉnh thành'].value_counts()/diem2022_df.groupby('Tỉnh thành')['Ngoại ngữ'].count()
diemcao_hoa = diem2022_df[diem2022_df['Hoá học'] >= point]['Tỉnh thành'].value_counts()/diem2022_df.groupby('Tỉnh thành')['Hoá học'].count()
diemcao_sinh = diem2022_df[diem2022_df['Sinh học'] >= point]['Tỉnh thành'].value_counts()/diem2022_df.groupby('Tỉnh thành')['Sinh học'].count()
diemcao_ly = diem2022_df[diem2022_df['Vật lý'] >= point]['Tỉnh thành'].value_counts()/diem2022_df.groupby('Tỉnh thành')['Vật lý'].count()
diemcao_dia = diem2022_df[diem2022_df['Địa lý'] >= point]['Tỉnh thành'].value_counts()/diem2022_df.groupby('Tỉnh thành')['Địa lý'].count()
diemcao_su = diem2022_df[diem2022_df['Lịch sử'] >= point]['Tỉnh thành'].value_counts()/diem2022_df.groupby('Tỉnh thành')['Lịch sử'].count()
diemcao_gdcd = diem2022_df[diem2022_df['GDCD'] >= point]['Tỉnh thành'].value_counts()/diem2022_df.groupby('Tỉnh thành')['Lịch sử'].count()
diemcao_df = pd.DataFrame({'Toán học':diemcao_toan,'Ngữ văn':diemcao_van,'Ngoại ngữ':diemcao_nn,
                           'Hoá học':diemcao_hoa,'Vật lý':diemcao_ly,'Sinh học':diemcao_sinh,
                           'Địa lý':diemcao_dia,'Lịch sử':diemcao_su,'GDCD':diemcao_gdcd})
diemcao_df = diemcao_df.replace(np.nan, 0)
#print(diemcao_df.loc['THÁI BÌNH'])
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# print(diemcao_df)

# 5 tỉnh cao nhất theo từng môn
top5_cao_toan = diemcao_df['Toán học'].sort_values()[index_max].index
top5_cao_van = diemcao_df['Ngữ văn'].sort_values()[index_max].index
top5_cao_nn = diemcao_df['Ngoại ngữ'].sort_values()[index_max].index
top5_cao_hoa = diemcao_df['Hoá học'].sort_values()[index_max].index
top5_cao_ly = diemcao_df['Vật lý'].sort_values()[index_max].index
top5_cao_sinh = diemcao_df['Sinh học'].sort_values()[index_max].index
top5_cao_dia = diemcao_df['Địa lý'].sort_values()[index_max].index
top5_cao_su = diemcao_df['Lịch sử'].sort_values()[index_max].index
top5_cao_gdcd = diemcao_df['GDCD'].sort_values()[index_max].index
top5_diemcao_df = pd.DataFrame({'Toán':top5_cao_toan,'Ngữ văn':top5_cao_van,'Ngoại ngữ':top5_cao_nn,
                                'Hoá học':top5_cao_hoa,'Vật lý':top5_cao_ly,'Sinh học':top5_cao_sinh,
                                'Địa lý':top5_cao_dia,'Lịch sử':top5_cao_su,'GDCD':top5_cao_gdcd})
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(top5_diemcao_df)


# pd.set_option('display.max_columns', None)
# print(diem2022_df)
