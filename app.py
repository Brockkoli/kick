from flask import Flask, request, render_template, redirect, url_for
from markupsafe import escape
import re

app = Flask(__name__)

def is_safe_input(input_str):
    # Regular expression patterns for detecting potential XSS and SQL Injection
    #xss_pattern = re.compile(r'<[^>]*>')
    xss_pattern = re.compile(r'(<[^>]+>|javascript:|data:text/html|vbscript:|on[a-z]+=?|&#)', re.IGNORECASE)
    sql_injection_pattern = re.compile(r'(UNION|SELECT|INSERT|DELETE|UPDATE|CREATE|DROP|ALTER|EXEC|EXECUTE|;|--|\bOR\b|\bAND\b)', re.IGNORECASE)

    # Check for XSS
    if xss_pattern.search(input_str):
        return False

    # Check for SQL Injection
    if sql_injection_pattern.search(input_str):
        return False

    return True

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        search_term = request.form['search']
        if is_safe_input(search_term):
            return redirect(url_for('search', term=search_term))
        else:
            return render_template('index.html', error="Invalid input.")
    return render_template('index.html')

@app.route('/search')
def search():
    term = request.args.get('term', '')
    term = escape(term)  # Escaping the term to prevent XSS
    return render_template('search.html', term=term)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
