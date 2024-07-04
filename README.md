# LLM Chat Playground

This project is a web application that allows users to interact with various LLMs. It is built using Flask and can be packaged into a single executable using PyInstaller.

## Requirements

To run this project you will need:
- Python 3.x
- pip (Python package manager)
- PyInstaller

## How to install

### 1. Install dependencies

First, install the project's dependencies. Run the following command from the project root directory:

```bash
pip install -r requirements.txt
```

### 2. Setting environment variables

Create `.env` file in your project root directory and set it up like this:

```makefile
# LLM API key
LLM_API_KEY=your_llm_api_key_here

# LLM API URL
LLM_API_URL=https://api.openai.com/v1/chat/completions

# List of models to use (separated by commas)
LLM_MODELS=gpt-3.5-turbo,gpt-4o
```
Please replace `your_llm_api_key_here` with your actual LLM API key.

### 3. Run the application

To run the application in your local development environment, use the following command:

```bash
python app.py
```
You can use the application by accessing `http://127.0.0.1:5000` from your browser.

### 4. Packaging

To package your application into a single executable using PyInstaller, run the following command:

```bash
# Windows
pyinstaller --onefile --add-data "templates;templates" --add-data "static;static" app.py
```

You may need to use following command on MacOS:

```bash
# MacOS
pyinstaller --onefile --add-data "templates:templates" --add-data "static:static" app.py
```

Once packaging is complete, `app.exe` (or just `app` in MacOS) file will be created in your directory `dist`. You can run this file to use the application. You might need to adjust the permissions to make the file executable. You can do this using the `chmod` command:

```bash
chmod +x dist/app
```

## How to use

1. Execute `app.exe` file in `dist` directory.

2. You can use the application by accessing `http://127.0.0.1:5000` from your browser.

3. You can change the API key, endpoint URL, and model list by editing `.env` file.

## Caution

- `.env` file contains sensitive information, so keep it safe.
- Never post your API keys to a public repository.

## License

This project is distributed under the MIT License. See the `LICENSE` file for details.
