# LLM Chat Playground

LLM Chat Playground is a web application that allows users to interact with various Large Language Models (LLMs). It is built using Flask and can be packaged into a single executable using PyInstaller.

## Requirements

To run this project, you will need:
- Python 3.x
- pip (Python package manager)
- PyInstaller

## Installation


### 1. Set Up a Virtual Environment

Setting up a virtual environment helps manage dependencies and avoid conflicts. Follow the instructions below based on your operating system.

#### Windows

Open Command Prompt and run the following commands:

```sh
python -m venv venv
venv\Scripts\activate
```

#### macOS

Open Terminal and run the following commands:

```sh
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

Install the project's dependencies. Run the following command from the project root directory:

#### Windows

```sh
pip install -r requirements.txt
```

#### macOS

```sh
pip3 install -r requirements.txt
```

### 3. Setting Environment Variables

Create a `.env` file in your project root directory and set it up like this:

```sh
# LLM API key
LLM_API_KEY=your_llm_api_key_here

# LLM API URL
LLM_API_URL=https://api.openai.com/v1/chat/completions

# List of models to use (separated by commas)
LLM_MODELS=gpt-3.5-turbo,gpt-4o
```

Replace `your_llm_api_key_here` with your actual LLM API key.

### 4. Run the Application

To run the application in your local development environment, use the following command:

#### Windows

```sh
python app.py
```

#### macOS

```sh
python3 app.py
```

You can use the application by accessing `http://127.0.0.1:5000` from your browser.

### 5. Packaging

To package your application into a single executable using PyInstaller, run the following command:

#### Windows

```sh
pyinstaller --onefile --add-data "templates;templates" --add-data "static;static" app.py
```

#### macOS

Use the following command on macOS:

```sh
pyinstaller --onefile --add-data "templates:templates" --add-data "static:static" app.py
```

Once packaging is complete, `app.exe` (or just `app` on macOS) will be created in your `dist` directory. You can run this file to use the application. You might need to adjust the permissions to make the file executable. You can do this using the `chmod` command:

```sh
chmod +x dist/app
```

## How to Use

1. Execute the `app.exe` (or just `app` on macOS) file in the `dist` directory.

2. You can use the application by accessing `http://127.0.0.1:5000` from your browser.

3. You can change the API key, endpoint URL, and model list by editing the `.env` file.

## Caution

- The `.env` file contains sensitive information, so keep it safe.
- Never post your API keys to a public repository.

## License

This project is distributed under the MIT License. See the `LICENSE` file for details.
