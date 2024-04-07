from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resumegen.db'
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    work_position = db.Column(db.String(50), nullable=False)

    email = db.Column(db.String(50), nullable=False)
    contact = db.Column(db.String(50), nullable=False)

    work_exp_time = db.Column(db.Integer, nullable=False)

    work_exp_desc = db.Column(db.Text, nullable=False)
    hard_skills = db.Column(db.Text, nullable=False)
    education = db.Column(db.Text, nullable=False)
    other_info = db.Column(db.Text, nullable=False)
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    result = Post.query.all()
    return render_template('result.html', result=result)

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        work_position = request.form['work_position']
        email = request.form['email']
        contact = request.form['contact']
        work_exp_time = request.form['work_exp_time']
        work_exp_desc = request.form['work_exp_desc']
        hard_skills = request.form['hard_skills']
        education = request.form['education']
        other_info = request.form['other_info']

        post = Post(name=name, surname=surname, 
                    work_position=work_position, email=email, 
                    contact=contact, work_exp_time=work_exp_time, 
                    work_exp_desc=work_exp_desc, hard_skills=hard_skills, 
                    education=education, other_info=other_info)
        
        try: 
            db.session.add(post)
            db.session.commit()
            return redirect('/result')
        except: 
            return 'error'

        return redirect('/')
    else: 
        return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)