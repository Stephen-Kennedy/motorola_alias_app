from flask import Flask, render_template, request
from send_email import send_email
import csv
from database import Data
import config

app = Flask(__name__)
db = Data(config.database)


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/home")
def home():
    return render_template("home.html")
    radioid = request.form["radio_id"]
    serialnum = request.form["serial_num"]

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/data_exchange")
def data_exchange():
    return render_template("data_exchange.html")


@app.route("/success", methods=["POST"])
def success():
    if request.method == "POST":
        radio_id = request.form["radio_id"]
        alias = request.form["alias"].upper()
        serial = request.form["serial_num"].upper()
        agency = request.form["agency"].upper()
        # TODO need a filter for agency to update capability/radio profile assignment
        #Data.update_data(db, alias, radio_id)
        Data.insert_data(db, radio_id, serial, alias, agency)
        send_email("medicup@gmail.com", "this is a test")
        return "no hits"


@app.route("/data_exchange", methods=["POST"])
def upload():
    global file
    if request.method == "POST":
        file = request.files["file"]
        file.save("uploaded" + file.filename)
        with open("uploaded" + file.filename, "a") as f:
            f.write("This was added later!")
        print(file)
        print(type(file))
        return render_template("data_exchange.html", btn="download.html")


def read_file(conn):
    with open(config.upload_file, newline="") as f:
        reader = csv.reader(open(config.upload_file, newline=''), delimiter=',', quotechar='|')
        #radio_list = list(reader)
        cur = conn.cursor()
        for row in reader:
            print(','.join(row))
        # try:
        #     cur.executemany(
        #         "INSERT INTO provisioner VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        #         radio_list,
        #     )
        #     conn.commit()
        # except ValueError as e:
        #     print(e)


if __name__ == "__main__":

    app.debug = True
    app.run()
