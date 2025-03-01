from flask import Flask, render_template, request, redirect, url_for, flash, session
from backend import validate_login, ask_security_question  # Import functions from notebook

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for session handling

@app.route("/", methods=["GET", "POST"])
def login():
    if "attempts" not in session:
        session["attempts"] = 0  # Initialize failed attempts

    usual_login_start = datetime.now().replace(hour=13, minute=0, second=0)  # 1:00 PM
    usual_login_end = datetime.now().replace(hour=14, minute=0, second=0)  # 2:00 PM
    current_time = datetime.now()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        login_status = validate_login(username, password)  # Call Jupyter Notebook function

        if login_status == "success":
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            flash("Incorrect username or password", "Danger")

        # If credentials are correct but login is outside usual hours, trigger security question
        if login_status == "success":
            if current_time < usual_login_start or current_time > usual_login_end:
                flash("Unusual login time detected! Please answer the security question.", "warning")
                session["username"] = username  # Store username in session for security check
                return redirect(url_for("security_question"))

            session.pop("attempts", None)  # Reset failed attempts on success
            session["user"] = username  # Store user session
            return redirect(url_for("dashboard"))

        else:
            session["attempts"] += 1  # Increment failed attempt count
            if session["attempts"] >= 3:
                flash("Multiple failed login attempts. Please answer the security question.", "warning")
                session["username"] = username  # Store for security verification
                return redirect(url_for("security_question"))

            flash(f"Incorrect username or password. Attempt {session['attempts']} of 3.", "danger")

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return f"Welcome to Budgetly, {session['user']}!"

@app.route("/security_question", methods=["GET", "POST"])
def security_question():
    if "username" not in session:
        return redirect(url_for("login"))

    if "security_attempts" not in session:
        session["security_attempts"] = 0  # Initialize security question attempts

    if request.method == "POST":
        answer = request.form.get("security_answer").lower()
        correct_answer = ask_security_question()  # Fetch correct answer from notebook

        if answer == correct_answer.lower():
            flash("Security question passed!", "success")
            session["user"] = session.pop("username")  # Move user to logged-in session
            session.pop("attempts", None)  # Reset failed login attempts
            session.pop("security_attempts", None)  # Reset security question attempts
            return redirect(url_for("dashboard"))
        else:
            session["security_attempts"] += 1  # Increment security question attempts
            if session["security_attempts"] >= 3:
                flash("Too many failed security attempts. Access locked.", "danger")
                session.pop("username", None)  # Remove user session
                session.pop("security_attempts", None)  # Reset security attempts
                return redirect(url_for("login"))  # Lock out and return to login

            flash(f"Incorrect security answer. Attempt {session['security_attempts']} of 3.", "danger")

    return render_template("security.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)


















