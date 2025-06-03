import psycopg

connection = psycopg.connect(
    dbname = "applicants",
    user = "postgres"
    )

def runquery(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except:
        print(f"The error '{e}' occured")

query1 = "SELECT id FROM applicants WHERE term='Spring 2025'"
ids = runquery(connection, query1)

print(len(ids))