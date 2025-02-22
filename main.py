
from flask import Flask, render_template, redirect
from urllib.parse import quote

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')    
def about():
    title = 'About'
    return render_template('about.html', title=title)

@app.route('/contact')    
def contact():
    title = 'Contact'
    return render_template('contact.html', title=title)

@app.route('/team')    
def team():
    title = 'Team'
    return render_template('team.html', title=title)

@app.route('/services')    
def services():
    title = 'Services'
    return render_template('services.html', title=title)

@app.route('/about_chairman')    
def about_chairman():
    title = 'About Chairman'
    return render_template('about_chairman.html', title=title)

@app.route('/about_web_creator')    
def about_web_creator():
    title = 'About Web Creator'
    return render_template('about_web_creator.html', title=title)

@app.route('/redirect_whatsapp')
def redirect_whatsapp():
    phone_number = '03242473853'  # No country code prefix (e.g., 91 for India)
    message = 'Hello from Flask!'
    encoded_message = quote(message)  # URL-encode the message
    whatsapp_url = f'https://wa.me/{phone_number}?text={encoded_message}'
    return redirect(whatsapp_url)


if __name__ == '__main__':
    app.run(debug=True)

