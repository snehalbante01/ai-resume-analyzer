from flask import Flask, render_template, request
from utils.resume_parser import extract_text_from_pdf
from utils.analyzer import extract_skills, calculate_ats_score

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    resume = request.files["resume"]
    job_desc = request.form["job_description"]

    resume_text = extract_text_from_pdf(resume)
    skills = extract_skills(resume_text)
    score = calculate_ats_score(resume_text, job_desc)

    return render_template(
        "result.html",
        score=score,
        skills=skills[:20]
    )

if __name__ == "__main__":
    app.run(debug=True)
