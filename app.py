from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        "question": "Which language is used for web development?",
        "options": ["Python", "HTML", "C++", "Java"],
        "answer": "HTML"
    },
    {
        "question": "Which database is relational?",
        "options": ["MongoDB", "PostgreSQL", "Firebase", "Redis"],
        "answer": "PostgreSQL"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    }
]

@app.route("/", methods=["GET", "POST"])
def quiz():
    score = None

    if request.method == "POST":
        score = 0
        for i, q in enumerate(questions):
            selected = request.form.get(f"question-{i}")
            if selected == q["answer"]:
                score += 1

    return render_template("index.html", questions=questions, score=score)

if __name__ == "__main__":
    app.run(debug=True)
