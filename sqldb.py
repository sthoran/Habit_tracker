import sqlite3

DATABASE_NAME = '../habit_database.db'


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
    #insert dummy data
    cur.execute("INSERT INTO habit VALUES ('1','maxthor','123wer4!','2022-06-30' ,'laundry', 'w', '2022-05-30')")
    cur.execute("INSERT INTO habit VALUES ('2','maxthor','123wer4!','2022-06-30' ,'laundry', 'w', '2022-06-06')")
    cur.execute("INSERT INTO habit VALUES ('3','maxthor','123wer4!','2022-06-30' ,'laundry', 'w', '2022-06-13')")
    cur.execute("INSERT INTO habit VALUES ('4','maxthor','123wer4!','2022-06-30' ,'laundry', 'w', '2022-06-27')")
    cur.execute("INSERT INTO habit VALUES ('5','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-05-30')")
    cur.execute("INSERT INTO habit VALUES ('6','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-05-31')")
    cur.execute("INSERT INTO habit VALUES ('7','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-01')")
    cur.execute("INSERT INTO habit VALUES ('8','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-02')")
    cur.execute("INSERT INTO habit VALUES ('9','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-03')")
    cur.execute("INSERT INTO habit VALUES ('10','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-04')")
    cur.execute("INSERT INTO habit VALUES ('11','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-05')")
    cur.execute("INSERT INTO habit VALUES ('12','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-06')")
    cur.execute("INSERT INTO habit VALUES ('13','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-07')")
    cur.execute("INSERT INTO habit VALUES ('14','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-08')")
    cur.execute("INSERT INTO habit VALUES ('15','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-09')")
    cur.execute("INSERT INTO habit VALUES ('16','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-10')")
    cur.execute("INSERT INTO habit VALUES ('17','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-11')")
    cur.execute("INSERT INTO habit VALUES ('18','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-12')")
    cur.execute("INSERT INTO habit VALUES ('19','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-13')")
    cur.execute("INSERT INTO habit VALUES ('20','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-14')")
    cur.execute("INSERT INTO habit VALUES ('21','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-15')")
    cur.execute("INSERT INTO habit VALUES ('22','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-16')")
    cur.execute("INSERT INTO habit VALUES ('23','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-17')")
    cur.execute("INSERT INTO habit VALUES ('24','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-18')")
    cur.execute("INSERT INTO habit VALUES ('25','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-19')")
    cur.execute("INSERT INTO habit VALUES ('26','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-20')")
    cur.execute("INSERT INTO habit VALUES ('27','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-25')")
    cur.execute("INSERT INTO habit VALUES ('28','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-26')")
    cur.execute("INSERT INTO habit VALUES ('29','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-27')")
    cur.execute("INSERT INTO habit VALUES ('30','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-28')")
    cur.execute("INSERT INTO habit VALUES ('31','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-29')")
    cur.execute("INSERT INTO habit VALUES ('32','stothor','345ert5!','2022-05-30','study 6 h', 'd', '2022-06-30')")
    cur.execute("INSERT INTO habit VALUES ('33','moma','890zui7!','2022-01-30','mop floor', 'w', '2022-01-30')")
    cur.execute("INSERT INTO habit VALUES ('34','moma','890zui7!','2022-01-30','mop floor', 'w', '2022-02-06')")
    cur.execute("INSERT INTO habit VALUES ('35','moma','890zui7!','2022-01-30','mop floor', 'w', '2022-02-13')")
    cur.execute("INSERT INTO habit VALUES ('36','moma','890zui7!','2022-01-30','mop floor', 'w', '2022-02-20')")
    cur.execute("INSERT INTO habit VALUES ('37','maxthor','123wer4!','2021-01-01','study', 'd', '2021-01-01')")
    cur.execute("INSERT INTO habit VALUES ('38','maxthor','123wer4!','2021-01-01','study', 'd', '2021-01-02')")
    cur.execute("INSERT INTO habit VALUES ('39','maxthor','123wer4!','2021-01-01','study', 'd', '2021-01-03')")
    cur.execute("INSERT INTO habit VALUES ('40','maxthor','123wer4!','2021-01-01','study', 'd', '2021-01-04')")
    cur.execute("INSERT INTO habit VALUES ('41','maxthor','123wer4!','2021-01-01','study', 'd', '2021-01-05')")
    cur.execute("INSERT INTO habit VALUES ('42','maxthor','123wer4!','2021-01-01','study', 'd', '2021-01-06')")
    cur.execute("INSERT INTO habit VALUES ('43','maxthor','123wer4!','2021-01-01','study', 'd', '2021-01-07')")
    cur.execute("INSERT INTO habit VALUES ('44','maxthor','123wer4!','2021-01-01','study', 'd', '2021-01-08')")
    cur.execute("INSERT INTO habit VALUES ('45','maxthor','123wer4!','2021-01-01','study', 'd', '2021-01-09')")
    cur.execute("INSERT INTO habit VALUES ('46','maxthor','123wer4!','2021-01-01','study', 'd', '2021-01-10')")
    cur.execute("INSERT INTO habit VALUES ('47','maxthor','123wer4!','2021-01-01','study', 'd', '2021-01-11')")
    cur.execute("INSERT INTO habit VALUES ('48','maxthor','123wer4!','2021-01-01','study', 'd', '2021-01-12')")
    cur.execute("INSERT INTO habit VALUES ('49','maxthor','123wer4!','2021-01-01','study', 'd', '2021-01-13')")
    cur.execute("INSERT INTO habit VALUES ('50','maxthor','123wer4!','2021-01-01','study', 'd', '2021-01-14')")
    cur.execute("INSERT INTO habit VALUES ('51','maxthor','123wer4!','2021-01-01','study', 'd', '2021-01-20')")
    cur.execute("INSERT INTO habit VALUES ('52','maxthor','123wer4!','2021-01-01','study', 'd', '2021-01-21')")
    cur.execute("INSERT INTO habit VALUES ('53','maxthor','123wer4!','2021-01-01','study', 'd', '2021-01-22')")
    cur.execute("INSERT INTO habit VALUES ('54','maxthor','123wer4!','2021-01-01','study', 'd', '2021-02-01')")
    cur.execute("INSERT INTO habit VALUES ('55','maxthor','123wer4!','2022-01-01','wash car', 'm', '2021-01-03')")
    cur.execute("INSERT INTO habit VALUES ('56','maxthor','123wer4!','2021-01-01','wash car', 'm', '2021-02-03')")
    cur.execute("INSERT INTO habit VALUES ('57','maxthor','123wer4!','2021-01-01','wash car', 'm', '2021-03-03')")
    cur.execute("INSERT INTO habit VALUES ('58','maxthor','123wer4!','2021-01-01','wash car', 'm', '2021-04-03')")
    cur.execute("INSERT INTO habit VALUES ('59','maxthor','123wer4!','2021-01-01','wash car', 'm', '2021-06-03')")
    cur.execute("INSERT INTO habit VALUES ('60','maxthor','123wer4!','2022-06-25','work out', 'd', '2022-06-25')")
    cur.execute("INSERT INTO habit VALUES ('61','maxthor','123wer4!','2022-06-25','work out', 'd', '2022-06-26')")
    cur.execute("INSERT INTO habit VALUES ('62','maxthor','123wer4!','2022-06-25','work out', 'd', '2022-06-27')")
    cur.execute("INSERT INTO habit VALUES ('63','maxthor','123wer4!','2022-06-25','work out', 'd', '2022-06-28')")
    cur.execute("INSERT INTO habit VALUES ('64','maxthor','123wer4!','2022-06-25','work out', 'd', '2022-07-06')")
    cur.execute("INSERT INTO habit VALUES ('65','maxthor','123wer4!','2022-06-25','work out', 'd', '2022-07-07')")
    cur.execute("INSERT INTO habit VALUES ('66','maxthor','123wer4!','2022-06-25','work out', 'd', '2022-07-08')")
    cur.execute("INSERT INTO habit VALUES ('67','maxthor','123wer4!','2022-06-25','work out', 'd', '2022-07-09')")
    cur.execute("INSERT INTO habit VALUES ('68','maxthor','123wer4!','2022-06-25','work out', 'd', '2022-07-10')")
    cur.execute("INSERT INTO habit VALUES ('69','maxthor','123wer4!','2022-06-25','work out', 'd', '2022-07-11')")
    cur.execute("INSERT INTO habit VALUES ('71','maxthor','123wer4!','2022-06-25','work out', 'd', '2022-07-12')")
    cur.execute("INSERT INTO habit VALUES ('72','maxthor','123wer4!','2022-06-25','work out', 'd', '2022-07-13')")
    cur.execute("INSERT INTO habit VALUES ('73','maxthor','123wer4!','2022-06-25','work out', 'd', '2022-07-14')")
    cur.execute("INSERT INTO habit VALUES ('74','maxthor','123wer4!','2022-06-25','work out', 'd', '2022-07-15')")
    cur.execute("INSERT INTO habit VALUES ('75','maxthor','123wer4!','2022-06-25','work out', 'd', '2022-07-16')")
    cur.execute("INSERT INTO habit VALUES ('76','maxthor','123wer4!','2022-06-25','work out', 'd', '2022-07-19')")




