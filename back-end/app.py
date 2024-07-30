from flask import Flask, redirect, request, abort, send_file, render_template_string

from helper.functions import create_data

app = Flask(__name__)



@app.route("/")
def home_page():
    return render_template_string("""
        <h1>Hello Stranger</h1>
        <form action="/reg" method="post">
            Name: <input type="text" name="name"><br>
            Phone: <input type="text" name="phone"><br>
            <input type="submit">
        </form>
    """)

@app.route("/reg", methods=['POST', 'GET'])
def reg_excel():
    name = request.form.get('name')
    phone = request.form.get('phone')
    if name and phone:
        create_data(file_path="v1_ams.xlsx", name=name, phone=phone)
        return redirect("https://nasibajumayeva.uz/")
    return redirect("https://nasibajumayeva.uz/"),redirect("/")

@app.route('/download', methods=['GET'])
def download_file():
    password = request.args.get('password')
    if password == "mexroj17uz":
        try:
            # Ensure the path to the file is correct
            file_path = 'c:\\Users\\Sr Red\\Documents\\GitHub\\RLC-Landing-Page\\v1_ams.xlsx'
            return send_file(file_path, as_attachment=True)
        except Exception as e:
            return str(e), 500
    else:
        abort(403)
