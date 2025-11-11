from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    skills = request.form['skills'] # comma-separated string of skills
    skills = [s.strip().lower() for s in skills.split(",")]
    
    match_score = 0 
    
    job_desciption_skills = ["tensorflow", "keras", "pytorch", "scikit-learn", "llm", "rag"]
    
    for skill in job_desciption_skills:
        if skill in skills:
            match_score += 1
    
    match_score = (match_score / len(job_desciption_skills)) * 100
    match_score = round(match_score, 2)

    return render_template('result.html', name=name, email=email, match_score=match_score)

if __name__ == '__main__':
    app.run(debug=True)