# Simple Streamlit + Flask + SQLite App

This app lets you add names to a SQLite database via a Flask API and view them with a Streamlit frontend.

## How to Run

1. Start the backend Flask server:

```bash
python flask_api.py
```

2. Start the frontend Streamlit app:

```bash
streamlit run streamlit_app.py
```

3. Open your browser to [http://localhost:8501](http://localhost:8501)

## Requirements

Install dependencies with: 
```bash
pip install -r requirements.txt
```

## Project Files
- `flask_api.py` -- Flask backend API that handles the SQLite database
- `streamlit_app.py` -- Streamlit frontend UI
- `app.db` -- SQLite database (created automatically)

## Summary
- Flask handles the API, and SQLite stores the data.
- Streamlit calls the API and displays the data.
- Add names via Streamlit and see all the names live.

# Author
Created by Jacob Klymenko
