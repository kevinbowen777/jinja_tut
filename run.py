from flask import Flask, render_template

app = Flask(__name__)


@app.template_filter()
def datetimefilter(value, format='%Y%/%m/%d %H:%M'):
    """convert a datetime to a different format."""
    return value.strftime(format)


app.jinja_env.filters['datetimefilter'] = datetimefilter


@app.route("/")
def template_test():
    return render_template("body.html",
                           my_string="April is the cruelest month",
                           my_list=[0, 1, 2, 3, 4, 5],
                           title="Home ",
                           )


@app.route("/home")
def home():
    return render_template("body.html",
                           my_string="Welcome Home",
                           my_list=[6, 7, 8, 9, 10, 11],
                           title="Home ",
                           )


@app.route("/about")
def about():
    return render_template("body.html",
                           my_string="What is this about?",
                           my_list=[12, 13, 14, 15, 16, 17],
                           title="About ",
                           )


@app.route("/contact")
def contact():
    return render_template("body.html",
                           my_string="Give us a ring!",
                           my_list=[18, 19, 20, 21, 22, 23],
                           title="Contact ",
                           )


if __name__ == '__main__':
    app.run(debug=True)
