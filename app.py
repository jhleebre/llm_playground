import os
from flask import Flask, request, render_template, session, redirect, url_for
import requests
import markdown
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)
# Generate a secret key for session management
app.secret_key = os.urandom(24)

# Fetch API key, URL, and available models from environment variables
API_KEY = os.getenv('LLM_API_KEY')
API_URL = os.getenv('LLM_API_URL')
MODELS = os.getenv('LLM_MODELS').split(',')

# Function to call the language model API
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
    # Send a POST request to the API
    response = requests.post(API_URL, headers=headers, json=data)
    # Raise an error if the request was unsuccessful
    response.raise_for_status()
    return response.json()

# Route for the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize session variables if they do not exist
    if 'chat_history' not in session:
        session['chat_history'] = []
    if 'model' not in session:
        session['model'] = MODELS[0]
    if 'temperature' not in session:
        session['temperature'] = 0.7

    if request.method == 'POST':
        # Clear chat history if the 'clear' button is pressed
        if 'clear' in request.form:
            session['chat_history'] = []
            return redirect(url_for('index'))

        # Update session variables from the form inputs
        model = request.form['model']
        session['model'] = model
        system_message = request.form['system_message']
        user_message = request.form['user_message']
        temperature = float(request.form['temperature'])
        session['temperature'] = temperature

        # Reset chat history if a system message is provided
        if system_message:
            session['chat_history'] = [{"role": "system", "content": markdown.markdown(system_message, extensions=['fenced_code'])}]
        
        # Add the user's message to the chat history
        session['chat_history'].append({"role": "user", "content": markdown.markdown(user_message, extensions=['fenced_code'])})
        
        try:
            # Call the language model API
            api_response = call_llm_api(model, session['chat_history'], temperature)
            # Add the assistant's response to the chat history
            if 'choices' in api_response and len(api_response['choices']) > 0:
                response_message = api_response['choices'][0]['message']['content']
                session['chat_history'].append({"role": "assistant", "content": markdown.markdown(response_message, extensions=['fenced_code'])})
        except requests.exceptions.RequestException as e:
            # Add an error message to the chat history if the API call fails
            session['chat_history'].append({"role": "assistant", "content": f"Error: {str(e)}"})

        # Redirect to the main page to refresh the form and display the updated chat history
        return redirect(url_for('index'))

    # Render the main page template with the current session variables
    return render_template('index.html', chat_history=session['chat_history'], model=session['model'], temperature=session['temperature'], models=MODELS)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
