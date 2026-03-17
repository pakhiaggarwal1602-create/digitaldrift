# Digital Drift — Flask demo site

This is a lightweight Flask app that demonstrates a bold, vibrant digital marketing website with a CSS 3D hero, bouncing service cards and detailed service pages. Forms are stubbed to `/signup` and print leads to console.

Quick start

1. Create and activate a Python virtualenv.

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the app

```bash
set FLASK_APP=app.py
flask run
```

Open http://127.0.0.1:5000/

Notes
- Replace `/static/img/logo.svg` and the work SVGs with your provided logo and screenshots.
- The site uses placeholder assets if you don't upload them.
- The lead form currently flashes a message and prints to console; integrate with your CRM as needed.
