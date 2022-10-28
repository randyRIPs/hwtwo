from flask import Flask, render_template,request
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>羅翊綸的網頁</h1>"
    homepage += "<a href=/mis>有興趣的MIS相關工作</a><br>"
    homepage += "<a href=/today>顯示日期時間</a><br>"
    homepage += "<a href=/welcome?nick=tcyang>自傳</a><br>"
        return homepage

@app.route("/mis")
def course():
    return "<h1>MIS工程師</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html", datetime = str(now))

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)

#if __name__ == "__main__":
#   app.run()
