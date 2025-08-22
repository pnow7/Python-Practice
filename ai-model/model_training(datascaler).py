import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# --- 전처리된 데이터 불러오기 ---
# 'data_preprocessing.py' 파일에서 저장한 데이터를 불러옴
file_path = 'c:/Users/82108/Desktop/Developer/python/ai-model/split_data.pkl'

with open(file_path, 'rb') as f:
    X_train, X_test, y_train, y_test = pickle.load(f)

print("데이터 불러오기 완료")

# --- 데이터 스케일링(모델 성능 개선: 데이터 평균을 0, 표준편차를 1로 맞춤) ---
# 평균을 0, 표준편차를 1로 만드는 이유: 모든 데이터들의 특성값을 똑같은 출발선에 세워서 모델이 어떤 특성이든 공정하게 평가, 더 안정적으로 학습
# 한마디로 모든 특성들의 값을 비슷한 범위로 맞춰주는 역할
# StandardScaler 객체 생성
scaler = StandardScaler()

# 훈련 데이터에 StandardScaler를 적용하여 학습하고 변환
X_train_scaled = scaler.fit_transform(X_train)

# 테스트 데이터는 훈련 데이터의 기준으로 변환하기만 함
X_test_scaled = scaler.transform(X_test)

print("데이터 스케일링 완료")

# --- 모델 학습 ---
# 로지스틱 회귀 모델을 생성
# max_iter: 반복횟수 늘리면 정확도 올릴수 있음
model = LogisticRegression(max_iter=1000)

# 훈련 데이터를 사용하여 모델을 학습시킵니다.
print("*모델 학습 중*")
model.fit(X_train_scaled, y_train)

# --- 모델 예측 및 평가 ---
# 테스트 데이터(X_test)로 이탈 여부를 예측
y_pred = model.predict(X_test_scaled)

# 예측 결과(y_pred)와 실제 결과(y_test)를 비교하여 정확도를 계산
accuracy = accuracy_score(y_test, y_pred)
print("모델 학습 완료")
print(f"모델의 예측 정확도: {accuracy:.2f}")