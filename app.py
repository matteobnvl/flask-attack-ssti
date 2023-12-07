from flask import Flask, render_template, request, render_template_string

app = Flask(__name__)

@app.route('/',  methods=['GET', 'POST'])
def hello_geek():
    user = ''
    if request.form.get('name'):
        user = request.form.get('name')
        template = """ <p>Welcome, {}</p>""".format(user)
        return render_template_string(template)
    return render_template('index.html', context={'user': user})


if __name__ == "__main__":
    app.run(debug=True)