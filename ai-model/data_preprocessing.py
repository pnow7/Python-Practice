import pandas as pd

file_path = 'c:/Users/82108/Desktop/Developer/python/ai-model/WA_Fn-UseC_-Telco-Customer-Churn.csv'

df = pd.read_csv(file_path)

print(df.head())

#print(df.info())

# TotalCharges 데이터 타입 변환(object -> float64)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
#print(df.info())

# NaN 값 제거(데이터 타입 변환하는 과정에서 생긴 NaN(결측치))
df = df.dropna()

print(df.info())

"""
<범주형 데이터 인코딩>

인코딩:  gender, Partner, Churn 처럼 문자열로 된 열들을 모델이 이해할 수 있는 숫자로 변환
방법: Yes/No나 Male/Female처럼 두 가지 값만 있는 열들은 각각 1, 0으로 바꿔주는 이진 인코딩 사용

"""

# gender 열의 Male과 Female을 0과 1로 변환
df['gender'] = df['gender'].replace({'Male': 0, 'Female': 1})

# 나머지 Yes/No 열들도 0과 1로 변환
binary_cols = ['Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'PaperlessBilling', 'Churn']

for col in binary_cols:
    df[col] = df[col].replace({'Yes': 1, 'No': 0})

# 변환된 데이터의 첫 5개 행 출력
print(df.head())

"""
<원 핫 인코딩>

이진 인코딩을 했떤 열들을 제외한 다른 열들은 Yes/No 처럼 두 가지 값만 가지고 있는게 아닌
여러 가지 값(범주)을 가지고 있음

이런 경우에 0, 1, 2처럼 숫자로 바꾸면 모델이 잘못된 해석을 할 수 있음
해결하기 위해 One-Hot Encoding 이라는 방법 사용

One-Hot Encoding: 각 범주(카테고리)를 새로운 열로 만들고
해당하면 1, 아니면 0으로 채우는 방식

"""

# 원-핫 인코딩 적용할 열 선택
categorical_cols = ['InternetService', 'Contract', 'PaymentMethod']

# pd.get_dummies() 함수를 사용해서 원-핫 인코딩 적용
df = pd.get_dummies(df, columns=categorical_cols, dtype=int)

# 불필요한 열 제거(customerID열은 고객을 식별하는 고유한 값이라서 모델 학습에는 아무런 의미가 없음)
df = df.drop('customerID', axis=1)

print(df.head())

print(df.columns)