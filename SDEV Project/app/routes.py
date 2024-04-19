from app import app
from flask import render_template, session, redirect, request
@app.route('/')
@app.route('/index')

def index():
    if session['language'] == 'da':
        return render_template ('danish.html')
    elif session['language'] == 'el':
        return render_template ('greek.html')
    else:
        return render_template ('english.html')



@app.route('/set-lang/<lang_code>')
def set_language(lang_code):
    #Pop the session variable to None to force an overwrite
    session.pop('language', None)
    #Set the session variable lang to whatever code was used in the url
    session["language"] = lang_code
    #refresh the page from which the set language request was made
    return redirect(request.referrer)

@app.before_request
def set_session_language():
    if 'language' not in session:
        session['language'] = 'en'  # Set default language here