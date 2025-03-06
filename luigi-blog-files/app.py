import os
from flask import Flask, render_template
from flask_flatpages import FlatPages
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default-secret-key")

# Configure FlatPages
app.config['FLATPAGES_AUTO_RELOAD'] = True
app.config['FLATPAGES_EXTENSION'] = '.md'
app.config['FLATPAGES_ROOT'] = 'content'
pages = FlatPages(app)

@app.route('/')
def index():
    essays = [p for p in pages if "essays" in p.path]
    essays.sort(key=lambda p: p.meta.get('date', ''), reverse=True)
    return render_template('index.html', essays=essays)

@app.route('/essay/<path:path>/')
def essay(path):
    essay = pages.get_or_404(f'essays/{path}')
    return render_template('essay.html', essay=essay)

@app.route('/archive')
def archive():
    essays = [p for p in pages if "essays" in p.path]
    essays.sort(key=lambda p: p.meta.get('date', ''), reverse=True)
    return render_template('archive.html', essays=essays)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('base.html', error="404 - Page not found"), 404
