from flask import Flask, render_template, request

app = Flask(__name__)

GRADES = {
    "4822":{"name":"Rebin","module":"CSC403","mark":72},
    "4823":{"name":"Sara","module":"CSC403","mark":65},
    "4824":{"name":"Ahmed","module":"CSC403","mark": 58},
}
CURRENT_USER = "4822"

@app.route('/grades')
def grades():
    student_id = request.args.get("student")
    record = GRADES.get(student_id)
    
    if record is None:
        return "NO such record", 413

    if student_id != CURRENT_USER:
        print ("Unauthorized access attempt by user:", CURRENT_USER, "to record:")
        return "You are not authorized to view this record", 403

    return  render_template("grades.html", sid=student_id, r=record)

@app.route('/')
def home():
    return 'Welcome to the Student Portal!'


@app.route('/student/<name>')
def student(name):
    return render_template("student.html",name=name)


@app.route('/course')
def course():
    return 'Course: Secure Software Development'

@app.route("/feedback", methods=["GET","POST"])
def feedback():
    message = None
    if request.method == "POST":
        name = request.form.get("name")
        feedback_text = request.form.get("feedback")
        print("Student:", name)
        print("Feedback:", feedback_text)
        message = "Thank you! Your feedback was recieved."
    return render_template("feedback.html",message=message)


if __name__ == '__main__':
    app.run()