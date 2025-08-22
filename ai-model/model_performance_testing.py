import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier 

# --- 전처리된 데이터 불러오기 ---
file_path = 'c:/Users/82108/Desktop/Developer/python/ai-model/split_data.pkl'

with open(file_path, 'rb') as f:
    X_train, X_test, y_train, y_test = pickle.load(f)

print("데이터 불러오기 완료")

# --- 데이터 스케일링 ---
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("데이터 스케일링 완료")

# --- 모델 학습 및 평가 ---
# 1. 로지스틱 회귀 모델
print("\n=== 로지스틱 회귀 모델 학습 ===")
log_reg_model = LogisticRegression(max_iter=1000)
log_reg_model.fit(X_train_scaled, y_train)
log_reg_pred = log_reg_model.predict(X_test_scaled)
log_reg_accuracy = accuracy_score(y_test, log_reg_pred)
print(f"로지스틱 회귀 모델의 예측 정확도: {log_reg_accuracy:.2f}")

# 2. 랜덤 포레스트 모델(여러개의 의사결정나무를 숲처럼 모아놓은 모델)
# 데이터의 일부를 무작위로 뽑아 여러개의 작은 의사 결정 나무를 만듬
# 각 나무들은 자기만의 규칙으로 데이터를 분석하고 예측함(개별 나무의 예측)
# 숲에 있는 모든 나무들의 예측을 모아 가장 많은 나무들이 내린 결정을 최종 예측 결과로 삼음(최종 결정)
print("\n=== 랜덤 포레스트 모델 학습 ===")
# n_estimators: 결정 트리의 개수
# random_state: 결과 고정을 위함
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
# 랜덤 포레스트는 스케일링이 필요 없음
rf_model.fit(X_train, y_train) 
rf_pred = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_pred)
print(f"랜덤 포레스트 모델의 예측 정확도: {rf_accuracy:.2f}")

# 랜덤 포레스트 장점
# 1. 과적합 방지: 의사 결정 나무는 한두 개만 쓰면 특정 데이터에만 너무 잘 맞는 과적합 문제가 발생할 수 있음
# 하지만 랜덤 포레스트는 여러 개의 나무가 다양한 관점에서 예측을 하기 때문에 이런 문제를 크게 줄여줌
# 2. 다양한 데이터 처리: 선형 모델인 로지스틱 회귀와 달리, 랜덤 포레스트는 복잡하고 비선형적인 데이터 패턴도 잘 잡아낼 수 있음
# 그래서 로지스틱 회귀보다 더 높은 성능을 보일 때 있음