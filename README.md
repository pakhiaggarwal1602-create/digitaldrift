# Digital Drift — Flask demo site

This is a lightweight Flask app that demonstrates a bold, vibrant digital marketing website with a CSS 3D hero, bouncing service cards and detailed service pages. Forms are stubbed to `/signup` and print leads to console.

Quick start (Streamlit)

1. Create and activate a Python virtualenv and install dependencies:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the app with Streamlit:

```bash
streamlit run app.py
```

Open the URL shown by Streamlit (usually http://localhost:8501).

Notes
- Replace `static/img/logo.svg` and the work SVGs with your provided logo and screenshots.
- The site uses placeholder assets if you don't upload them.
- Leads submitted via the form are printed to the server console; integrate with your CRM/DB as needed.
