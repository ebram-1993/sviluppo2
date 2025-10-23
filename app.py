from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head><title>Quiz</title></head>
<body>
  <h1>Mini Quiz</h1>
  <form method="post">
    <p>Do you want to play?</p>
    <input name="project"><br><br>
    <p>What is the CPU?</p>
    <input name="cpu"><br><br>
    <p>Cosa sono le VLAN?</p>
    <input name="vlan"><br><br>
    <p>Cosa sono le VPN?</p>
    <input name="vpn"><br><br>
    <button type="submit">Submit</button>
  </form>
  {% if result is defined %}
    <h3>{{ result }}</h3>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        win = 0
        if request.form.get("project") != "yes":
            return render_template_string(HTML, result="Hai scelto di non giocare 😢")

        if request.form.get("cpu") == "central processing unit":
            win += 1
        if request.form.get("vlan") == "virtual local area network":
            win += 1
        if request.form.get("vpn") == "virtual private network":
            win += 1

        return render_template_string(HTML, result=f"Hai segnato {win} risposte corrette 🎯")

    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
