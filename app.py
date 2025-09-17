from flask import Flask, request, render_template_string
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    msg = ""
    if request.method == "POST":
        name = request.form.get("name","")
        subscribe = "subscribe" in request.form
        msg = f"Hello {name}. Subscribed: {subscribe}"
    return render_template_string("""
      <h1>Hello, World!</h1>
      <form method="post">
        <input name="name" type="text">
        <input name="subscribe" type="checkbox">
        <button type="submit">Submit</button>
      </form>
      <div>{{message}}</div>
    """, message=msg)

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
