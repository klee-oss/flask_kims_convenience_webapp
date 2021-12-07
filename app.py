from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/ins_choi/")
def ins_choi():
    return render_template("/ins_choi/ins_choi.html")


@app.route("/ins_choi2/")
def ins_choi2():
    return render_template("/ins_choi/ins_choi2.html")


@app.route("/ins_choi3/")
def ins_choi3():
    return render_template("/ins_choi/ins_choi3.html")


@app.route("/ins_choi4/")
def ins_choi4():
    return render_template("/ins_choi/ins_choi4.html")


@app.route("/ins_choi5/")
def ins_choi5():
    return render_template("/ins_choi/ins_choi5.html")


@app.route("/ins_choi_end/")
def ins_choi_end():
    return render_template("/ins_choi/ins_choi_end.html")


@app.route("/simu/")
def simu():
    return render_template("/simu/simu.html")


@app.route("/simu2/")
def simu2():
    return render_template("/simu/simu2.html")


@app.route("/simu3/")
def simu3():
    return render_template("/simu/simu3.html")


@app.route("/simu4/")
def simu4():
    return render_template("/simu/simu4.html")


@app.route("/simu5/")
def simu5():
    return render_template("/simu/simu5.html")


@app.route("/simu_end/")
def simu_end():
    return render_template("/simu/simu_end.html")


@app.route("/jean/")
def jean():
    return render_template("/jean/jean.html")


@app.route("/jean2/")
def jean2():
    return render_template("/jean/jean2.html")


@app.route("/jean3/")
def jean3():
    return render_template("/jean/jean3.html")


@app.route("/jean4/")
def jean4():
    return render_template("/jean/jean4.html")


@app.route("/jean5/")
def jean5():
    return render_template("/jean/jean5.html")


@app.route("/jean_end/")
def jean_end():
    return render_template("/jean/jean_end.html")


@app.route("/paul/")
def paul():
    return render_template("/paul/paul.html")


@app.route("/paul2/")
def paul2():
    return render_template("/paul/paul2.html")


@app.route("/paul3/")
def paul3():
    return render_template("/paul/paul3.html")


@app.route("/paul4/")
def paul4():
    return render_template("/paul/paul4.html")


@app.route("/paul5/")
def paul5():
    return render_template("/paul/paul5.html")


@app.route("/paul_end/")
def paul_end():
    return render_template("/paul/paul_end.html")


@app.route("/kevin/")
def kevin():
    return render_template("/kevin/kevin.html")


@app.route("/kevin2/")
def kevin2():
    return render_template("/kevin/kevin2.html")


@app.route("/kevin3/")
def kevin3():
    return render_template("/kevin/kevin3.html")


@app.route("/kevin_end/")
def kevin_end():
    return render_template("/kevin/kevin_end.html")


@app.route("/simu_no/")
def simu_no():
    return render_template("/simu/simu_no.html")


@app.route("/simu_no2/")
def simu_no2():
    return render_template("/simu/simu_no2.html")


@app.route("/simu_no3/")
def simu_no3():
    return render_template("/simu/simu_no3.html")


@app.route("/simu_no4/")
def simu_no4():
    return render_template("/simu/simu_no4.html")


@app.route("/simu_no5/")
def simu_no5():
    return render_template("/simu/simu_no5.html")


@app.route("/jean_no/")
def jean_no():
    return render_template("/jean/jean_no.html")


@app.route("/jean_no2/")
def jean_no2():
    return render_template("/jean/jean_no2.html")


@app.route("/jean_no3/")
def jean_no3():
    return render_template("/jean/jean_no3.html")


@app.route("/jean_no4/")
def jean_no4():
    return render_template("/jean/jean_no4.html")


@app.route("/jean_no5/")
def jean_no5():
    return render_template("/jean/jean_no5.html")


@app.route("/paul_no/")
def paul_no():
    return render_template("/paul/paul_no.html")


@app.route("/paul_no2/")
def paul_no2():
    return render_template("/paul/paul_no2.html")


@app.route("/paul_no3/")
def paul_no3():
    return render_template("/paul/paul_no3.html")


@app.route("/paul_no4/")
def paul_no4():
    return render_template("/paul/paul_no4.html")


@app.route("/paul_no5/")
def paul_no5():
    return render_template("/paul/paul_no5.html")


@app.route("/ins_choi_no/")
def ins_choi_no():
    return render_template("/ins_choi/ins_choi_no.html")


@app.route("/ins_choi_no2/")
def ins_choi_no2():
    return render_template("/ins_choi/ins_choi_no2.html")


@app.route("/ins_choi_no3/")
def ins_choi_no3():
    return render_template("/ins_choi/ins_choi_no3.html")


@app.route("/ins_choi_no4/")
def ins_choi_no4():
    return render_template("/ins_choi/ins_choi_no4.html")


@app.route("/ins_choi_no5/")
def ins_choi_no5():
    return render_template("/ins_choi/ins_choi_no5.html")


@app.route("/kevin_no/")
def kevin_no():
    return render_template("/kevin/kevin_no.html")


@app.route("/kevin_no2/")
def kevin_no2():
    return render_template("/kevin/kevin_no2.html")


@app.route("/kevin_no3/")
def kevin_no3():
    return render_template("/kevin/kevin_no3.html")


if __name__ == "__main__":
    app.run()
