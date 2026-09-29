from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "dev-secret-key"  # change in production

# Fake user database
USERS = {
    "admin": "admin123",
    "user1": "pass123",
    "test": "test123",
}

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        if username in USERS and USERS[username] == password:
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            error = "Invalid username or password"

    return render_template("login.html", error=error)

@app.route("/welcome")
def welcome():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("welcome.html", user=session["user"])

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
