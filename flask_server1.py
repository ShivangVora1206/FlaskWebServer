from flask import Flask , redirect , url_for, render_template, request
app = Flask(__name__)
@app.route("/home")
def home():
    #a = {1:'1',2:'2',3:'3'}
    f = open(r'flask_server\test.txt','r')
    x = f.readlines()
    return str(x)
@app.route("/<name>")
def login(name):
    return f'<h1>login {name}</h1>'

@app.route('/admin')
def admin():
    return redirect(url_for('login', name='admin!'))

@app.route('/resume')
def resume():
    return render_template("resume.html", first="shubam", last=1010)

@app.route('/powst', methods=["POST","GET"])
def powst():
    if request.method == 'POST':
        name = request.form['name']
        f = open(r'flask_server\test.txt','w')
        f.write(name)
        return render_template("forms.html")
    else:
        return render_template("forms.html")




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)