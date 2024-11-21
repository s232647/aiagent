# 분류 모델 웹앱 만들기
import streamlit as st

# 1.기계학습 모델 파일 로드
import joblib
model = joblib.load('model (2).pkl') 

# 2.모델 설명
st.title('Iris 탐정단')
col1,col2,col3 = st.columns( 3 )      # 몇 개의 컬럼으로 나눌까?
with col1:
      st.subheader(' 모델 설명 ')
      st.write(' - 기계학습 알고리즘 : 로지스틱 회귀 ')
      st.write(' - 학습 데이터 출처 :https://www.kaggle.com/datasets/himanshunakrani/iris-dataset?select=iris.csv')
      st.write(' - 훈련    데이터 : 105건')
      st.write(' - 테스트 데이터 : 45건')
      st.write(' - 모델 정확도 : 0.97')
# 3.데이터시각화
with col2:
      st.subheader('데이터시각화1')
      st.image('시각화1.png' )   # 이미지 불러오기
with col3:
      st.subheader('데이터시각화2')
      st.image('시각화2.png' )   # 이미지 불러오기
col4,col5,col6 = st.columns( 3 )      # 몇 개의 컬럼으로 나눌까?
with col4:
      st.subheader('데이터시각화3')
      st.image('시각화3.png' )   # 이미지 불러오기
with col5:
      st.subheader('데이터시각화4')
      st.image('시각화4.png' )   # 이미지 불러오기
with col6:
      st.subheader('데이터시각화5')
      st.image('시각화5.png' )   # 이미지 불러오기

# 4. 모델 활용
st.subheader('모델 활용')
st.write('**** 꽃의 정보를 입력하세요.')

a = st.number_input(' 꽃받침의 길이를 입력하세요. ', value=0.0)   # 사용자 입력
b = st.number_input(' 꽃받침의 폭을 입력하세요. ', value=0.0)
c = st.number_input(' 꽃잎의 길이를 입력하세요. ', value=0.0)
d = st.number_input(' 꽃잎의 폭을 입력하세요. ', value=0.0)

if st.button('이 꽃은 무엇입니다!'):              # 사용자가 '합불분류' 버튼을 누르면
        input_data = [[ a,b,c,d ]]          # 사용자가 입력한 a,b,c 를 input_data에 저장하고
        p = model.predict(input_data)      # model이 분류한 값을 p에 저장한다
        if p[0] == 0 :
              st.success('setosa')
        elif p[0] == 1 :
              st.success('versicolor')
        elif p[0] == 2 :
              st.success('virginica')
              


