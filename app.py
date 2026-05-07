from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def home():

    cgpa = None

    if request.method == 'POST':

        sem1 = float(request.form['sem1'])
        sem2 = float(request.form['sem2'])
        sem3 = float(request.form['sem3'])
        sem4 = float(request.form['sem4'])
        sem5 = float(request.form['sem5'])
        sem6 = float(request.form['sem6'])
        sem7 = float(request.form['sem7'])
        sem8 = float(request.form['sem8'])

        total = (
            sem1 + sem2 + sem3 + sem4 +
            sem5 + sem6 + sem7 + sem8
        )

        cgpa = round(total / 8, 2)

    return render_template('index.html', cgpa=cgpa)

if __name__ == '__main__':

    app.run(debug=True)