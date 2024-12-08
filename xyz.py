import streamlit as st

col1, col2= st.columns(2)
with col1:
  st.title('Trà Sữa CoTAI')
  st.image("trasua.jpg")
  option = st.multiselect('Topping', ('Trân châu trắng (5K)', 'Trân châu đen (5K)', 'Thạch rau câu (6K)', 'Vải (7K)', 'Nhãn (8K)', 'Đào (10K)'))
with col2:
  radio = st.radio('Kích cỡ', ('Nhỏ (30K)', 'Vừa (40K)', 'Lớn (50K)'), horizontal=True)
  st.write('Thêm')
  col3, col4= st.columns(2)
  with col3:
    Milk = st.checkbox('Sữa (5K)')
    Cafe = st.checkbox('Cà phê (8K)')
  with col4:
    Kem = st.checkbox('Kem (10K)')
    Trung = st.checkbox('Trứng (15K)')
  number = st.number_input('Số lượng', 1)
textarea = st.text_area('Ghi chú', 'Ghi chú')
if radio == 'Nhỏ (30K)':
  a = 30
elif radio == 'Vừa (40K)':
  a = 40
elif radio == 'Lớn (50K)':
  a = 50
b = []
if Milk == True:
  b.append('Sữa (5K)')
if Cafe == True:
  b.append('Cà phê (8K)')
if Kem == True:
  b.append('Kem (10K)')
if Trung == True:
  b.append('Trứng (15K)')
c = []
if "Trân châu trắng (5K)" in option:
  c.append(5)
if "Trân châu đen (5K)" in option:
  c.append(5)
if "Thạch rau câu (6K)" in option:
  c.append(6)
if "Vải (7K)" in option:
  c.append(7)
if "Nhãn (8K)" in option:
  c.append(8)
if "Đào (10K)" in option:
  c.append(10)
d = sum(c)
money = number *(a + d + (Milk*5) + (Cafe*8) + (Kem*10) + (Trung*15))
if st.button('Đặt hàng'):
  st.write('Cỡ :',radio)
  st.write('Thêm :',*b)
  st.write('Topping :',*option)
  st.text(textarea)
  st.write('Số lượng',number)
  st.write('Thành tiền',money)
