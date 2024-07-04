import os
from flask import Flask, request, render_template, session, redirect, url_for
import requests
import markdown
from dotenv import load_dotenv

load_dotenv()  # .env 파일의 환경 변수 로드

app = Flask(__name__)
app.secret_key = os.urandom(24)  # 보안을 위해 임의의 24바이트 문자열 사용

# 환경 변수에서 설정 값 가져오기
API_KEY = os.getenv('LLM_API_KEY')
API_URL = os.getenv('LLM_API_URL')
MODELS = os.getenv('LLM_MODELS').split(',')

# LLM API 호출 함수
def call_llm_api(model, messages, temperature):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature
    }
    response = requests.post(API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def index():
    # 세션 초기화 및 기본값 설정
    if 'chat_history' not in session:
        session['chat_history'] = []
    if 'model' not in session:
        session['model'] = MODELS[0]  # 기본 모델 설정
    if 'temperature' not in session:
        session['temperature'] = 0.7  # 기본 temperature 설정

    if request.method == 'POST':
        if 'clear' in request.form:
            session['chat_history'] = []
            return redirect(url_for('index'))

        model = request.form['model']
        session['model'] = model  # 모델 선택을 세션에 저장
        system_message = request.form['system_message']
        user_message = request.form['user_message']
        temperature = float(request.form['temperature'])
        session['temperature'] = temperature  # temperature 선택을 세션에 저장

        # system_message가 설정되어 있으면 초기화
        if system_message:
            session['chat_history'] = [{"role": "system", "content": markdown.markdown(system_message, extensions=['fenced_code'])}]
        
        # 사용자 메시지를 대화 기록에 추가
        session['chat_history'].append({"role": "user", "content": markdown.markdown(user_message, extensions=['fenced_code'])})
        
        # LLM API 호출
        try:
            api_response = call_llm_api(model, session['chat_history'], temperature)
            if 'choices' in api_response and len(api_response['choices']) > 0:
                response_message = api_response['choices'][0]['message']['content']
                session['chat_history'].append({"role": "assistant", "content": markdown.markdown(response_message, extensions=['fenced_code'])})
        except requests.exceptions.RequestException as e:
            session['chat_history'].append({"role": "assistant", "content": f"Error: {str(e)}"})

        return redirect(url_for('index'))

    return render_template('index.html', chat_history=session['chat_history'], model=session['model'], temperature=session['temperature'], models=MODELS)

if __name__ == '__main__':
    app.run(debug=True)
