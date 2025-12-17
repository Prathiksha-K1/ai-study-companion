from flask import Flask, render_template, request

app = Flask(__name__)

def generate_explanation(topic, level, style):
    if level == "Beginner":
        if style == "Analogy":
            return f"{topic} is like a simple real-life situation. Think of it as something you already experience daily, explained in an easy and friendly way."
        else:
            return f"{topic} explained in simple words with focus on basic exam understanding."
    
    elif level == "Intermediate":
        if style == "Analogy":
            return f"{topic} can be understood using relatable technical examples that connect concepts you already know."
        else:
            return f"{topic} explained with definitions, causes, and short examples suitable for semester exams."
    
    else:  # Advanced
        if style == "Analogy":
            return f"{topic} explained using system-level or real-world technical analogies for deeper insight."
        else:
            return f"{topic} explained with formal definitions, mechanisms, and exam-oriented structure."

@app.route("/", methods=["GET", "POST"])
def index():
    explanation = ""
    if request.method == "POST":
        topic = request.form["topic"]
        level = request.form["level"]
        style = request.form["style"]
        explanation = generate_explanation(topic, level, style)

    return render_template("index.html", explanation=explanation)

if __name__ == "__main__":
    app.run(debug=True)
