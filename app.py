from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def read_data():
    with open("data.txt", "r") as file:
        data = file.read().splitlines()
    return [line.split('\t') for line in data]

def write_data(data):
    with open("data.txt", "w") as file:
        for item in data:
            file.write('\t'.join(item) + '\n')

@app.route('/')
def index():
    data = read_data()
    return render_template('index.html', data=data)

@app.route('/add', methods=['POST'])
def add():
    new_question = request.form.get('question')
    new_answer = request.form.get('answer')
    data = read_data()
    data.append([new_question, new_answer])
    write_data(data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
