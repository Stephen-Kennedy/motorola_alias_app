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
        #self.cur.close()

    def update_data(self, radio, alias):
        self.conn = sqlite3.connect(self.database)
        self.cur = self.conn.cursor()

        sql = """ UPDATE provisioner SET COL_02='{0}' WHERE id_ = {1}; """.format(alias, radio)

        try:  # TODO fix search bug seach is working, but timing out after. looks like maybe http issue
            print(sql)
            self.cur.execute(sql)
            self.conn.commit()
        except ValueError as e:
            print(e)

        self.cur.close()
    def search_data(self, _id, _serial, _alias):
        self.conn = sqlite3.connect(self.database)
        self.cur = self.conn.cursor()

        sql = """ SELECT * FROM provisioner WHERE id_={0} OR COL_01 = '{1}' OR COL_02 = '{2}'; """.format(_id, _serial, _alias)

        try: #TODO fix search bug seach is working, but timing out after. looks like maybe http issue
            self.y = self.cur.execute(sql)
            print (self.y.fetchall())
        except ValueError as e:
            print(e)
            return
        self.cur.close()

    def delete_data(self):
        print("delete data")

    def view_data(self):
        print("view data")
        self.conn = sqlite3.connect(self.database)
        self.cur = self.conn.cursor()
        for row in self.cur.execute("SELECT * FROM provisioner"):
            print(row)
        self.cur.close()




# TODO db.create_table() # remove after testing.



db = Data(config.database)
# db.update_data(4801008,"48001011")
db.search_data(4800001, "481CNP3902 2", "CHIEF2")
# db.view_data()