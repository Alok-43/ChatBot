# Custom Gemini Chatbot by Shivam

A custom chatbot powered by Google's Gemini AI using LangChain and Streamlit.

## Features
- 🤖 Powered by Google Gemini 2.5 Flash
- 🔗 LangChain integration
- 📊 LangSmith tracking
- 🎨 Clean Streamlit UI

## Prerequisites
- Python 3.8+
- Google API Key
- LangChain API Key (optional, for tracking)

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/gemini-langchain-chatbot.git
cd gemini-langchain-chatbot
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
cp .env.example .env
```

Then edit `.env` and add your API keys:
```
GOOGLE_API_KEY=your_google_api_key_here
LANGCHAIN_API_KEY=your_langchain_api_key_here
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## Configuration

- **Model**: Gemini 2.5 Flash
- **Temperature**: 0.7
- **LangSmith Tracking**: Enabled 

## Project Structure
```
├── app.py              # Main Streamlit application
├── config.py           # Configuration and environment setup
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment variables
└── README.md          # Project documentation
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

## License

MIT License

## Author

Created by Shivam
