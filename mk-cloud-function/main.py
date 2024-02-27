
import functions_framework
import mysql.connector
from google.cloud.sql.connector import Connector
import sqlalchemy

iter="5"

# https://colab.research.google.com/github/GoogleCloudPlatform/cloud-sql-python-connector/blob/main/samples/notebooks/mysql_python_connector.ipynb#scrollTo=wfEvH386zX2V

# initialize Connector object
connector = Connector()

# function to return the database connection object
def getconn():
    conn = connector.connect(
        "hallta-on-gcp-409718:us-central1:mysql-dev2",
        "pymysql",
        user="chef",
        password="food",
        db="sandwiches"
    )
    return conn

# create connection pool with 'creator' argument to our connection object function
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)

@functions_framework.http
def hello_world(req):
    with pool.connect() as db_conn:
        return "\nohai" + iter

#   with pool.connect() as conn:

#       return "hello world"


#   # connect to connection pool
#   with pool.connect() as db_conn:
#       # create ratings table in our sandwiches database
#       db_conn.execute(
#           sqlalchemy.text(
#           "CREATE TABLE IF NOT EXISTS ratings "
#           "( id SERIAL NOT NULL, name VARCHAR(255) NOT NULL, "
#           "origin VARCHAR(255) NOT NULL, rating FLOAT NOT NULL, "
#           "PRIMARY KEY (id));"
#           )
#       )

#       # commit transaction (SQLAlchemy v2.X.X is commit as you go)
#       db_conn.commit()

#       # insert data into our ratings table
#       insert_stmt = sqlalchemy.text(
#           "INSERT INTO ratings (name, origin, rating) VALUES (:name, :origin, :rating)",
#       )

#       # insert entries into table
#       db_conn.execute(insert_stmt, parameters={"name": "HOTDOG", "origin": "Germany", "rating": 7.5})
#       db_conn.execute(insert_stmt, parameters={"name": "BÀNH MÌ", "origin": "Vietnam", "rating": 9.1})
#       db_conn.execute(insert_stmt, parameters={"name": "CROQUE MADAME", "origin": "France", "rating": 8.3})

#       # commit transactions
#       db_conn.commit()

#       # query and fetch ratings table
#       results = db_conn.execute(sqlalchemy.text("SELECT * FROM ratings")).fetchall()

#       # show results
#       res = ""
#       for row in results:
#           res = res + row + "<br/>"

#       return(res)