from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def template_test():
    return render_template("body.html",
                           my_string="April is the cruelest month",
                           my_list=[0, 1, 2, 3, 4, 5],
                           title="Home "
                           )


if __name__ == '__main__':
    app.run(debug=True)
