from flask import Flask, jsonify
import pymysql


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'testuser'
app.config['MYSQL_PASSWORD'] = 'testuser123'
app.config['MYSQL_DB'] = 'test_db'
app.config['MYSQL_PORT'] = 3306

mysql = pymysql.connect(
    host = app.config['MYSQL_HOST'],
    user = app.config['MYSQL_USER'],
    password= app.config['MYSQL_PASSWORD'],
    db = app.config['MYSQL_DB'],
    port = app.config['MYSQL_PORT'],
    autocommit=True,
)

def create_tables():
    try:
        print('Creating Table Started =====')
        cur = mysql.cursor()
        cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS items (
                id INT AUTO_INCREMENT PRIMARY KEY ,
                name VARCHAR(255) NOT NULL,
                description TEXT
            )
            '''
        )
        mysql.commit()
        cur.close()
        print('Items Table Created =====')
    except Exception as e:
        print("Error while creating table", e)

create_tables()


@app.route('/')
def hello():
    return 'Hello Flask World'


@app.route('/items:create')
def create_item():
    cursor = mysql.cursor()
    sql = "INSERT INTO items(name, description) VALUES ('doyeon', 'i love you');"
    cursor.execute(sql)
    results = cursor.fetchall()
    return jsonify(results)


@app.route('/items')
def get_items():
    cursor = mysql.cursor()
    sql = "SELECT * FROM items"
    cursor.execute(sql)
    results = cursor.fetchall()
    return jsonify(results)

    
if __name__ == '__main__':
    app.run()
