import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import re

# 1. FastAPI 앱 생성
app = FastAPI()

# 2. 저장된 모델과 벡터라이저 불러오기
try:
    model = joblib.load('spam_model.pkl')
    tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')
    print("✅ 모델과 벡터라이저를 성공적으로 불러왔습니다.")
except FileNotFoundError:
    print("Error: 'spam_model.pkl' 또는 'tfidf_vectorizer.pkl' 파일을 찾을 수 없습니다.")
    print("모델 학습 및 저장을 먼저 실행해주세요.")
    model = None
    tfidf_vectorizer = None
    
# 3. 요청 데이터 구조 정의
class EmailRequest(BaseModel):
    text: str

# 4. 텍스트 전처리 함수
def clean_text(text):
    text = str(text)
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ' ', text)
    text = re.sub(r'[^\w\s\n]|<[^>]+>',' ', text).strip()
    return ' '.join(text.split())

@app.get("/")
def read_root():
    return {"Hello": "Model API is ready!"}

# 5. 예측 API 엔드포인트 생성
@app.post("/predict")
def predict_spam(request: EmailRequest):
    if not model or not tfidf_vectorizer:
        return {"error": "모델이 로드되지 않았습니다."}
    
    # 받은 텍스트 전처리
    cleaned_text = clean_text(request.text)
    
    # TF-IDF 변환
    text_vector = tfidf_vectorizer.transform([cleaned_text])
    
    # 모델 예측
    prediction = model.predict(text_vector)[0]
    
    # 예측 결과 반환
    result = "스팸 메일" if prediction == 1 else "정상 메일"
    return {"prediction": int(prediction), "result": result}

# uvicorn main:app --reload