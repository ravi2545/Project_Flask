import psycopg2
class ShowDict:
    def __init__(self):
        self.conn=psycopg2.connect(database="ravi", user="postgres", password="Ravi@143", host="127.0.0.1", port="5432")
        self.cursor=self.conn.cursor()


    def ins(self):
        cur=self.cursor
        cur.execute('''CREATE TABLE onlineDict
              (NAME           TEXT    NOT NULL,
              Meaning            TEXT     NOT NULL);''')

        self.conn.commit()
        self.conn.close()


    def dis(self,name):
        self.l=[]
        cur=self.cursor
        cur.execute("SELECT meaning FROM onlinedict WHERE name='{}'".format(name))
        rows = cur.fetchall()
        for i in rows:
            for j in i:
                self.l.append(j)
        return self.l