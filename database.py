import mysql.connector


class DatabaseHelper:
    def __init__(self):
        HOST = "mysql-af31601-fatemehvaleh-89c0.aivencloud.com"
        PORT = 26712
        USER = "avnadmin"
        PASSWORD = "AVNS_rykcFEWrx0fnr-KKeki"
        DATABASE = "defaultdb"

        self.table_name = "advertisement"
        self.db = mysql.connector.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )

        self.cursor = self.db.cursor()

        # self.cursor.execute("create table advertisement ("
        #                     "id int not null primary key auto_increment,"
        #                     "description varchar(255),"
        #                     "email varchar(255),"
        #                     "status varchar(255),"
        #                     "category varchar(255)"
        #                     ") auto_increment=10")
        # self.cursor.execute(f"drop table {self.table_name}")

    def foo(self):
        print("helooo")
        self.cursor.execute(f"SELECT * FROM {self.table_name}")

        myresult = self.cursor.fetchall()

        for x in myresult:
            print(x)

    def insert_to_db(self, description, email):
        sql = f"INSERT INTO {self.table_name} (description, email, status) VALUES (%s, %s, %s)"
        val = (description, email, 'in_progress')
        self.cursor.execute(sql, val)

        self.db.commit()

        print(self.cursor.rowcount, "record inserted.")
        id_inserted = self.cursor.lastrowid

        self.cursor.execute(f"SELECT * FROM {self.table_name}")

        myresult = self.cursor.fetchall()

        for x in myresult:
            print(x)

        return id_inserted

    def select_from_db(self, field, _id):
        query = f"select {field} from {self.table_name} where id={_id}"
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def update_in_db(self, field, _id, new_data):
        query = f"update {self.table_name} set {field}={new_data} where id=_id"
        self.cursor.execute(query)
        self.db.commit()


if __name__ == '__main__':
    DatabaseHelper().foo()
