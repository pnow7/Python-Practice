import pandas as pd
from sklearn.model_selection import train_test_split
import pickle

# 데이터 파일 경로를 지정
file_path = 'c:/Users/82108/Desktop/Developer/python/ai-model/WA_Fn-UseC_-Telco-Customer-Churn.csv'
df = pd.read_csv(file_path)

# --- 데이터 전처리 ---
# 1. TotalCharges 열의 데이터 타입을 변환하고 결측치(NaN)를 제거
# df.dropna(inplace=True): df = df.dropna()와 같은 역할을 하지만 원본 df에 바로 변경사항을 적용
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(inplace=True)

# 2. 이진 인코딩을 적용
df['gender'] = df['gender'].replace({'Male': 0, 'Female': 1})

binary_cols = ['Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'PaperlessBilling', 
                   'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 
                   'StreamingTV', 'StreamingMovies']

for col in binary_cols:
    df[col] = df[col].replace({'Yes': 1, 'No': 0, 'No internet service': 0, 'No phone service': 0})

# 3. Churn 열을 마지막에 이진 인코딩
df['Churn'] = df['Churn'].replace({'Yes': 1, 'No': 0})

# 4. 원-핫 인코딩을 적용
categorical_cols = ['InternetService', 'Contract', 'PaymentMethod']
df = pd.get_dummies(df, columns=categorical_cols, dtype=int)

# 5. 불필요한 customerID 열을 제거
df = df.drop('customerID', axis=1)

# --- 모델 학습을 위한 데이터 분리 ---
# 독립 변수(X)와 종속 변수(y)를 분리
# df.drop('Churn', axis=1)를 사용해서 Churn열을 제외한 모든 열을 X에 할당, axis = 1은 열을 기준으로 삭제
# df['Churn']을 y에 할당하여 예측 목표 명확화
X = df.drop('Churn', axis=1)
y = df['Churn']

# 훈련 데이터와 테스트 데이터를 8:2 비율로 나눔
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 분리된 데이터의 크기를 확인하여 최종 점검
print(f"훈련 데이터(X_train)의 크기: {X_train.shape}")
print(f"테스트 데이터(X_test)의 크기: {X_test.shape}")
print(f"훈련 데이터(y_train)의 크기: {y_train.shape}")
print(f"테스트 데이터(y_test)의 크기: {y_test.shape}")

# 분리된 데이터를 파일로 저장
with open('split_data.pkl', 'wb') as f:
    pickle.dump((X_train, X_test, y_train, y_test), f)

print("데이터 전처리 및 분리 완료 'split_data.pkl' 파일 생성")