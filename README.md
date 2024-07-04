# LLM Chat Playground

이 프로젝트는 사용자가 LLM과 상호 작용할 수 있는 웹 애플리케이션입니다. Flask를 사용하여 구축되었으며, PyInstaller를 사용하여 단일 실행 파일로 패키징할 수 있습니다.

## 요구 사항

이 프로젝트를 실행하기 위해 다음이 필요합니다:
- Python 3.x
- pip (Python 패키지 관리자)
- PyInstaller

## 설치 방법

### 1. 종속성 설치

먼저, 프로젝트의 종속성을 설치합니다. 프로젝트 루트 디렉토리에서 다음 명령어를 실행하세요:

```bash
pip install -r requirements.txt
```

### 2. 환경 변수 설정

프로젝트 루트 디렉토리에 `.env` 파일을 생성하고 다음과 같이 설정합니다:

```makefile
# LLM API 키 설정
LLM_API_KEY=your_llm_api_key_here

# LLM API URL 설정
LLM_API_URL=https://api.openai.com/v1/chat/completions

# 사용할 모델 목록 설정 (쉼표로 구분)
LLM_MODELS=gpt-3.5-turbo,gpt-4o
```

여기서 `your_llm_api_key_here` 부분을 실제 LLM API 키로 바꿔주세요.

### 3. 애플리케이션 실행

로컬 개발 환경에서 애플리케이션을 실행하려면 다음 명령어를 사용하세요:

```bash
python app.py
```

브라우저에서 `http://127.0.0.1:5000`에 접속하여 애플리케이션을 사용할 수 있습니다.

### 4. 패키징

PyInstaller를 사용하여 애플리케이션을 단일 실행 파일로 패키징하려면 다음 명령어를 실행하세요:

```bash
pyinstaller --onefile --add-data "templates;templates" --add-data "static;static" app.py
```

패키징이 완료되면 `dist` 디렉토리에 `app.exe` 파일이 생성됩니다. 이 파일을 실행하여 애플리케이션을 사용할 수 있습니다.

## 사용 방법

1. `dist` 디렉토리에서 `app.exe` 파일을 실행합니다.

2. 브라우저에서 `http://127.0.0.1:5000`에 접속하여 애플리케이션을 사용합니다.

3. `.env` 파일을 수정하여 API 키, 엔드포인트 URL, 및 모델 목록을 변경할 수 있습니다.

## 주의 사항

- `.env` 파일은 민감한 정보를 포함하고 있으므로, 이를 안전하게 관리하세요.
- API 키를 공개 저장소에 절대 올리지 마세요.

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 LICENSE 파일을 참조하세요.
