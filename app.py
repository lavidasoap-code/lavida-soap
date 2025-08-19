from flask import Flask, render_template, request, flash

app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')

app.secret_key = 'your-secret-key-here'  # Required for flash messages

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/process')
def process():
    return render_template('process.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Print form data to console
        print("\nContact Form Submission:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Subject: {subject}")
        print(f"Message: {message}\n")
        
        flash('Thank you for your message! We will get back to you soon.')
        
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
