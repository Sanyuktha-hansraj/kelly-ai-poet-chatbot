# Kelly — AI Scientist Poet Chatbot

Kelly is a Streamlit-based chatbot that responds in the voice of a skeptical AI scientist poet. It formats every answer as a poem and aims to provide evidence-aware, analytical responses about AI topics.

This repository contains a tiny Streamlit app (`app.py`) that calls the Groq chat completions API (via the `groq` Python package). Environment variables are loaded from a `.env` file using `python-dotenv`.

## Features

- Conversational UI built with Streamlit
- Every assistant reply is returned as a poem (Kelly's persona)
- Uses the Groq chat completions API
- Simple session-based chat history with a clear chat button

## Prerequisites

- Python 3.10+ recommended
- A Groq API key (set as `GROQ_API_KEY` in a `.env` file or your environment)
- Windows PowerShell or another shell

## Install

1. Clone or copy the repository to your machine.
2. Create and activate a virtual environment (recommended).

PowerShell example:

```powershell
python -m venv .venv;
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies from `requirements.txt`:

```powershell
pip install -r requirements.txt
```

## Configure

Create a file named `.env` in the repository root (same folder as `app.py`) and add your Groq API key:

```
GROQ_API_KEY=your_real_groq_api_key_here
```

The app uses `python-dotenv` to load this automatically. Alternatively, you can set `GROQ_API_KEY` as an environment variable in your shell.

## Run

Start the Streamlit app:

```powershell
streamlit run app.py
```

This will open a local web UI (or show a local URL in the terminal) where you can ask Kelly questions about AI and receive poetic, skeptical replies.

## Files of interest

- `app.py` — main Streamlit application
- `requirements.txt` — required Python packages

## Notes & caveats

- The app depends on the `groq` Python package and the Groq API. Ensure your API key has the correct permissions and quota.
- Model settings (model name, temperature, max_tokens) are defined in `app.py`. Adjust them there if needed.
- The Groq API may incur usage charges — monitor your usage and cost limits.

## Troubleshooting

- If the app displays `Groq API key not found in .env file!`, confirm your `.env` file is present and contains `GROQ_API_KEY`, or that the environment variable is exported.
- If generation fails due to API errors, check network connectivity and that your API key is valid.
- If Streamlit pages do not load, ensure the virtual environment is activated and the packages installed.

## Contributing

Small fixes and improvements welcome. Open an issue or a PR with a clear description of the change.

## License

Add a license file as needed. This README does not set a project license. If you want a permissive license, consider adding an `MIT` or `Apache-2.0` license file.

