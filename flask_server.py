from flask import Flask , redirect , render_template , request, url_for, Response
from random import randrange
app = Flask(__name__)

@app.route('/bazinga') 
def feed(): 
    return render_template('feed.html') 
def gen(): 
    import cv2
    vc = cv2.VideoCapture(0) 
    while True: 
        rval, frame = vc.read() 
        frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('pic.jpg', frame2) 
        yield (b'--frame\r\n' 
                b'Content-Type: image/jpeg\r\n\r\n' + open('pic.jpg', 'rb').read() + b'\r\n') 
@app.route('/video_feed') 
def video_feed(): 
    return Response(gen(), 
                mimetype='multipart/x-mixed-replace; boundary=frame') 

@app.route('/madlib0')
def mad0():
    name = request.args.get('name')
    name2 = request.args.get('name2')
    adj = request.args.get('adj')
    animal = request.args.get('animal')
    return render_template('mad0.html', name=name, name2=name2, adj=adj, animal=animal)


@app.route('/madlib1')
def mad1():
    name = request.args.get('name')
    name2 = request.args.get('name2')
    adj = request.args.get('adj')
    animal = request.args.get('animal')
    return render_template('mad1.html', name=name, name2=name2, adj=adj, animal=animal)

@app.route('/madlib2')
def mad2():
    name = request.args.get('name')
    name2 = request.args.get('name2')
    adj = request.args.get('adj')
    animal = request.args.get('animal')
    return render_template('mad2.html', name=name, name2=name2, adj=adj, animal=animal)

@app.route('/madlib3')
def mad3():
    name = request.args.get('name')
    name2 = request.args.get('name2')
    adj = request.args.get('adj')
    animal = request.args.get('animal')
    ec = request.args.get('ec')
    insect = request.args.get('insect')
    return render_template('mad3.html', name=name, name2=name2, adj=adj, animal=animal, ec=ec, insect=insect)

@app.route('/madlib4')
def mad4():
    name = request.args.get('name')
    name2 = request.args.get('name2')
    adj = request.args.get('adj')
    animal = request.args.get('animal')
    return render_template('mad4.html', name=name, name2=name2, adj=adj, animal=animal)

@app.route('/', methods=['POST','GET'])
def alpha():
    if request.method == 'POST':
        name = request.form['Name']
        name2 = request.form['Name2']
        adj = request.form['Adjective']
        animal = request.form['animal']
        ec = request.form['ec']
        insect = request.form['insect']
        i = randrange(start=0, stop=5)
        add = 'mad'+str(i)
        if adj == "bazinga":
            return render_template('feed.html')
        else:
            return redirect(url_for(add, name=name, name2=name2, adj=adj, animal=animal, ec=ec, insect=insect))
    else:
        return render_template('powst.html')



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)