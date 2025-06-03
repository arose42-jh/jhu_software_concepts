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
        print(f"error occured")
        return "error"

total = "SELECT id FROM applicants"
total_count = len(runquery(connection, total))

spring25 = "SELECT id FROM applicants WHERE term='Spring 2025'"
ids = runquery(connection, spring25)#

international = "SELECT id FROM applicants WHERE us_or_international = 'International'"
inter = len(runquery(connection, international))
interper = inter/total_count * 100

print(f"1. applicant of spring 2025: {len(ids)}")
print(f"2. International percentage: {interper:.2f}%")