import sqlite3

DATABASE_NAME = 'habit_database.db'


def connect_db():
    con = sqlite3.connect(DATABASE_NAME)
    cur = con.cursor()
    return con, cur


def close_db(con):
    con.commit()
    con.close()


def create_table():
    con, cur = connect_db()
    #create table
    cur.execute("DROP TABLE IF EXISTS habit")
    cur.execute(''' CREATE TABLE habit
                    (user_id integer UNIQUE PRIMARY KEY AUTOINCREMENT,
                    username varchar(50),
                    password varchar(10),
                    start_date DATE,
                    habit TEXT,
                    period TEXT,
                    check_off DATE)''')
    close_db(con)


def show_db():
    con, cur = connect_db()
    for row in cur.execute('SELECT * FROM habit'):
        print(row)
    close_db(con)


def dummy_fill_db(cur):
    """ fill database with dummy data  """
    cur.execute("INSERT INTO habit VALUES ('1','user1','123wer4!','2022-06-30' ,'laundry', 'w', '2022-06-30')")
    cur.execute("INSERT INTO habit VALUES ('2','user1','123wer4!','2022-06-30' ,'laundry', 'w', '2022-07-05')")
    cur.execute("INSERT INTO habit VALUES ('3','user1','123wer4!','2022-06-30' ,'laundry', 'w', '2022-07-12')")
    cur.execute("INSERT INTO habit VALUES ('4','user1','123wer4!','2022-06-30' ,'laundry', 'w', '2022-07-26')")
    cur.execute("INSERT INTO habit VALUES ('5','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-06-29')")
    cur.execute("INSERT INTO habit VALUES ('6','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-06-30')")
    cur.execute("INSERT INTO habit VALUES ('7','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-07-01')")
    cur.execute("INSERT INTO habit VALUES ('8','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-07-02')")
    cur.execute("INSERT INTO habit VALUES ('9','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-07-03')")
    cur.execute("INSERT INTO habit VALUES ('10','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-07-04')")
    cur.execute("INSERT INTO habit VALUES ('11','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-07-05')")
    cur.execute("INSERT INTO habit VALUES ('12','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-07-06')")
    cur.execute("INSERT INTO habit VALUES ('13','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-07-07')")
    cur.execute("INSERT INTO habit VALUES ('14','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-07-08')")
    cur.execute("INSERT INTO habit VALUES ('15','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-07-09')")
    cur.execute("INSERT INTO habit VALUES ('16','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-07-10')")
    cur.execute("INSERT INTO habit VALUES ('17','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-07-11')")
    cur.execute("INSERT INTO habit VALUES ('18','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-07-12')")
    cur.execute("INSERT INTO habit VALUES ('19','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-07-13')")
    cur.execute("INSERT INTO habit VALUES ('20','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-07-14')")
    cur.execute("INSERT INTO habit VALUES ('21','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-07-15')")
    cur.execute("INSERT INTO habit VALUES ('22','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-07-16')")
    cur.execute("INSERT INTO habit VALUES ('23','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-07-17')")
    cur.execute("INSERT INTO habit VALUES ('24','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-07-18')")
    cur.execute("INSERT INTO habit VALUES ('25','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-07-19')")
    cur.execute("INSERT INTO habit VALUES ('26','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-07-20')")
    cur.execute("INSERT INTO habit VALUES ('27','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-07-25')")
    cur.execute("INSERT INTO habit VALUES ('28','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-07-26')")
    cur.execute("INSERT INTO habit VALUES ('29','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-07-27')")
    cur.execute("INSERT INTO habit VALUES ('30','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-07-28')")
    cur.execute("INSERT INTO habit VALUES ('31','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-08-01')")
    cur.execute("INSERT INTO habit VALUES ('32','user2','345ert5!','2022-06-29','study 6 h', 'd', '2022-08-02')")
    cur.execute("INSERT INTO habit VALUES ('33','user3','890zui7!','2022-07-04','mop floor', 'w', '2022-07-04')")
    cur.execute("INSERT INTO habit VALUES ('34','user3','890zui7!','2022-07-04','mop floor', 'w', '2022-07-18')")
    cur.execute("INSERT INTO habit VALUES ('35','user3','890zui7!','2022-07-04','mop floor', 'w', '2022-07-26')")
    cur.execute("INSERT INTO habit VALUES ('36','user3','890zui7!','2022-07-04','mop floor', 'w', '2022-08-01')")
    cur.execute("INSERT INTO habit VALUES ('37','user1','123wer4!','2022-07-01','study', 'd', '2022-07-01')")
    cur.execute("INSERT INTO habit VALUES ('38','user1','123wer4!','2022-07-01','study', 'd', '2022-07-02')")
    cur.execute("INSERT INTO habit VALUES ('39','user1','123wer4!','2022-07-01','study', 'd', '2022-07-03')")
    cur.execute("INSERT INTO habit VALUES ('40','user1','123wer4!','2022-07-01','study', 'd', '2022-07-04')")
    cur.execute("INSERT INTO habit VALUES ('41','user1','123wer4!','2022-07-01','study', 'd', '2022-07-05')")
    cur.execute("INSERT INTO habit VALUES ('42','user1','123wer4!','2022-07-01','study', 'd', '2022-07-06')")
    cur.execute("INSERT INTO habit VALUES ('43','user1','123wer4!','2022-07-01','study', 'd', '2022-07-07')")
    cur.execute("INSERT INTO habit VALUES ('44','user1','123wer4!','2022-07-01','study', 'd', '2022-07-08')")
    cur.execute("INSERT INTO habit VALUES ('45','user1','123wer4!','2022-07-01','study', 'd', '2022-07-09')")
    cur.execute("INSERT INTO habit VALUES ('46','user1','123wer4!','2022-07-01','study', 'd', '2022-07-10')")
    cur.execute("INSERT INTO habit VALUES ('47','user1','123wer4!','2022-07-01','study', 'd', '2022-07-11')")
    cur.execute("INSERT INTO habit VALUES ('48','user1','123wer4!','2022-07-01','study', 'd', '2022-07-12')")
    cur.execute("INSERT INTO habit VALUES ('49','user1','123wer4!','2022-07-01','study', 'd', '2022-07-13')")
    cur.execute("INSERT INTO habit VALUES ('50','user1','123wer4!','2022-07-01','study', 'd', '2022-07-14')")
    cur.execute("INSERT INTO habit VALUES ('51','user1','123wer4!','2022-07-01','study', 'd', '2022-07-20')")
    cur.execute("INSERT INTO habit VALUES ('52','user1','123wer4!','2022-07-01','study', 'd', '2022-07-21')")
    cur.execute("INSERT INTO habit VALUES ('53','user1','123wer4!','2022-07-01','study', 'd', '2022-07-22')")
    cur.execute("INSERT INTO habit VALUES ('54','user1','123wer4!','2022-07-01','study', 'd', '2022-08-01')")
    cur.execute("INSERT INTO habit VALUES ('55','user1','123wer4!','2022-02-03','wash car', 'm', '2022-02-03')")
    cur.execute("INSERT INTO habit VALUES ('56','user1','123wer4!','2022-02-03','wash car', 'm', '2022-03-03')")
    cur.execute("INSERT INTO habit VALUES ('57','user1','123wer4!','2022-02-03','wash car', 'm', '2022-05-03')")
    cur.execute("INSERT INTO habit VALUES ('58','user1','123wer4!','2022-02-03','wash car', 'm', '2022-06-03')")
    cur.execute("INSERT INTO habit VALUES ('59','user1','123wer4!','2022-02-03','wash car', 'm', '2022-08-03')")
    cur.execute("INSERT INTO habit VALUES ('60','user1','123wer4!','2022-06-25','work out', 'd', '2022-07-09')")
    cur.execute("INSERT INTO habit VALUES ('61','user1','123wer4!','2022-06-25','work out', 'd', '2022-07-10')")
    cur.execute("INSERT INTO habit VALUES ('62','user1','123wer4!','2022-06-25','work out', 'd', '2022-07-14')")
    cur.execute("INSERT INTO habit VALUES ('63','user1','123wer4!','2022-06-25','work out', 'd', '2022-07-15')")
    cur.execute("INSERT INTO habit VALUES ('64','user1','123wer4!','2022-06-25','work out', 'd', '2022-07-16')")
    cur.execute("INSERT INTO habit VALUES ('65','user1','123wer4!','2022-06-25','work out', 'd', '2022-07-17')")
    cur.execute("INSERT INTO habit VALUES ('66','user1','123wer4!','2022-06-25','work out', 'd', '2022-07-18')")
    cur.execute("INSERT INTO habit VALUES ('67','user1','123wer4!','2022-06-25','work out', 'd', '2022-07-19')")
    cur.execute("INSERT INTO habit VALUES ('68','user1','123wer4!','2022-06-25','work out', 'd', '2022-07-20')")
    cur.execute("INSERT INTO habit VALUES ('69','user1','123wer4!','2022-06-25','work out', 'd', '2022-07-21')")
    cur.execute("INSERT INTO habit VALUES ('71','user1','123wer4!','2022-06-25','work out', 'd', '2022-07-22')")
    cur.execute("INSERT INTO habit VALUES ('72','user1','123wer4!','2022-06-25','work out', 'd', '2022-07-23')")
    cur.execute("INSERT INTO habit VALUES ('73','user1','123wer4!','2022-06-25','work out', 'd', '2022-07-24')")
    cur.execute("INSERT INTO habit VALUES ('74','user1','123wer4!','2022-06-25','work out', 'd', '2022-07-25')")
    cur.execute("INSERT INTO habit VALUES ('75','user1','123wer4!','2022-06-25','work out', 'd', '2022-07-26')")
    cur.execute("INSERT INTO habit VALUES ('76','user1','123wer4!','2022-06-25','work out', 'd', '2022-07-29')")


def init_db():
    create_table()
    con, cur = connect_db()
    dummy_fill_db(cur)
    close_db(con)
    show_db()

