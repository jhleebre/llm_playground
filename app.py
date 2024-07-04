import os
from flask import Flask, request, render_template, session, redirect, url_for
import requests
import markdown
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

API_KEY = os.getenv('LLM_API_KEY')
API_URL = os.getenv('LLM_API_URL')
MODELS = os.getenv('LLM_MODELS').split(',')

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
    if 'chat_history' not in session:
        session['chat_history'] = []
    if 'model' not in session:
        session['model'] = MODELS[0]
    if 'temperature' not in session:
        session['temperature'] = 0.7

    if request.method == 'POST':
        if 'clear' in request.form:
            session['chat_history'] = []
            return redirect(url_for('index'))

        model = request.form['model']
        session['model'] = model
        system_message = request.form['system_message']
        user_message = request.form['user_message']
        temperature = float(request.form['temperature'])
        session['temperature'] = temperature

        if system_message:
            session['chat_history'] = [{"role": "system", "content": markdown.markdown(system_message, extensions=['fenced_code'])}]
        
        session['chat_history'].append({"role": "user", "content": markdown.markdown(user_message, extensions=['fenced_code'])})
        
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
