from flask import Flask, render_template
from Plotlydash.dashboard import init_dashboard

app = Flask(__name__)
with app.app_context():
    app = init_dashboard(app)

@app.route('/')
def index():
    return 'Hello Team Edge!'
    
@app.route('/python')
def hello_python():
    return 'Custom python place holder page'
    
@app.route('/codenext')
def code_next_page():
    return render_template("codenext.html")
    

if __name__ == '__main__':
    app.run(debug=True)
