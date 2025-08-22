import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# --- 전처리된 데이터 불러오기 ---
# 'data_preprocessing.py' 파일에서 저장한 데이터를 불러옴
with open('split_data.pkl', 'rb') as f:
    X_train, X_test, y_train, y_test = pickle.load(f)

print("데이터 불러오기 완료!")

# --- 모델 학습 ---
# 1. 로지스틱 회귀 모델을 생성
model = LogisticRegression(max_iter=1000)

# 2. 훈련 데이터를 사용하여 모델을 학습시킵니다.
print("*모델 학습 중*")
model.fit(X_train, y_train)

# --- 모델 예측 및 평가 ---
# 1. 테스트 데이터(X_test)로 이탈 여부를 예측
y_pred = model.predict(X_test)

# 2. 예측 결과(y_pred)와 실제 결과(y_test)를 비교하여 정확도를 계산
accuracy = accuracy_score(y_test, y_pred)
print("모델 학습 완료")
print(f"모델의 예측 정확도: {accuracy:.2f}")