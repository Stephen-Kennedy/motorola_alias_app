import sqlite3
import csv
import config


class Data:
    def __init__(self, database):
        self.database = database
        self.create_table()

    def create_table(self):
        try:
            self.conn = sqlite3.connect(self.database)
            self.cursor = self.conn.cursor()
            self.cursor.execute(config.table)
            self.conn.commit()
        except ValueError as e:
            print(e)

        try:
            self.build_data()
        except ValueError as e:
            print(e)

    def build_data(self):
        try:
            self.conn = sqlite3.connect(self.database)
            self.cur = self.conn.cursor()

            reader = csv.reader(
                open(config.upload_file, newline=""), delimiter=",", quotechar="|"
            )
            for row in reader:
                values = (
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                    row[9],
                    row[10],
                    row[11],
                    row[12],
                    row[13],
                    row[14],
                    row[15],
                    row[16],
                    row[17],
                    row[18],
                    row[19],
                    row[20],
                    row[21],
                    row[22],
                    row[23],
                    row[24],
                    row[25],
                    row[26],
                    row[27],
                )
                self.cur.execute(
                    "INSERT OR IGNORE INTO provisioner VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,"
                    "?,?,?,?,?,?,?)",
                    (values),
                )
            self.conn.commit()
        except ValueError as e:
            print(e)

    def insert_data(self, radio_id, serial, alias, agency):
        print("insert date")
        if agency == "SCSO":
            col_03 = 1
            col_04 = 4
            col_05 = 4
            col_06 = 1001
        elif agency == "SCFEMS":
            col_03 = 1
            col_04 = 812
            col_05 = 812
            col_06 = 1114
        self.conn = sqlite3.connect(self.database)
        self.cur = self.conn.cursor()
        values = (
            radio_id,
            serial,
            alias,
            col_03,
            col_04,
            col_05,
            col_06,
            config.col_07,
            config.col_08,
            config.col_09,
            config.col_10,
            config.col_11,
            config.col_12,
            config.col_13,
            config.col_14,
            config.col_15,
            config.col_16,
            config.col_17,
            config.col_18,
            config.col_19,
            config.col_20,
            config.col_21,
            config.col_22,
            config.col_23,
            config.col_24,
            config.col_25,
            config.col_26,
            config.col_27,
        )
        try:
            self.cur.execute(
                "INSERT OR IGNORE INTO provisioner VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (values),
            )
            self.conn.commit()
        except ValueError as e:
            print(e)

    def update_data(self, data_value, alias):
        self.conn = sqlite3.connect(self.database)
        self.cur = self.conn.cursor()
        values = (data_value, alias)
        try:
            self.cur.execute("UPDATE provisioner SET COL_02=? WHERE id_=?;", values)
            print(values)
            self.conn.commit()
        except ValueError as e:
            print(e)

    def search_data(self, data_value):
        self.conn = sqlite3.connect(self.database)
        self.cur = self.conn.cursor()
        values = ("sample", data_value)
        try:
            self.cur.execute("UPDATE provisioner SET COL_02=? WHERE id_=?;", values)
            print(values)
            self.conn.commit()
        except ValueError as e:
            print(e)

    def delete_data(self):
        print("delete data")

    def view_data(self):
        print("view data")
        self.conn = sqlite3.connect(self.database)
        self.cur = self.conn.cursor()
        for row in self.cur.execute("SELECT * FROM provisioner"):
            print(row)


db = Data(config.database)
# db.search_data()
# TODO db.create_table() # remove after testing.
# db.view_data()  # remove after testing
