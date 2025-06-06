import psycopg
import statistics
connection = psycopg.connect(
    dbname = "applicants",
    user = "postgres"
    )

def runquery(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        # Makes a list instead of tuple
        result = [r[0] for r in cursor.fetchall()]
        return result
    except:
        print(f"error occured")
        return "error"

def get_all_statistics():
    total = "SELECT id FROM applicants"
    total_count = len(runquery(connection, total))

    Fall25query = "SELECT id FROM applicants WHERE term='Fall 2025'"
    Fall25 = runquery(connection, Fall25query)

    internationalquery = "SELECT id FROM applicants WHERE us_or_international = 'International'"
    inter = len(runquery(connection, internationalquery))
    interper = inter/total_count * 100

    GPAquery = "SELECT gpa FROM applicants WHERE gpa IS NOT NULL"
    gpa = statistics.mean(runquery(connection, GPAquery))

    GREQuery = "SELECT gre FROM applicants WHERE gre IS NOT NULL"
    gre = statistics.mean(runquery(connection, GREQuery))

    GREVQuery = "SELECT gre_v FROM applicants WHERE gre_v IS NOT NULL"
    grev = statistics.mean(runquery(connection, GREVQuery))

    GREAWQuery = "SELECT gre_aw FROM applicants WHERE gre_aw IS NOT NULL"
    greaw = statistics.mean(runquery(connection, GREAWQuery))

    USgpaQuery = "SELECT gpa FROM applicants WHERE gpa IS NOT NULL AND us_or_international = 'American' AND term = 'Fall 2025'"
    usgpaavg = statistics.mean(runquery(connection, USgpaQuery))

    AcceptedSprQuery = "SELECT status FROM applicants WHERE status LIKE 'Accepted%' AND term = 'Fall 2025'"
    acceptedperc = len(runquery(connection, AcceptedSprQuery)) / len(Fall25) * 100

    AccptGPAQuery = "SELECT gpa FROM applicants WHERE status LIKE 'Accepted%' AND term = 'Fall 2025' AND gpa IS NOT NULL"
    acceptavg = statistics.mean(runquery(connection, AccptGPAQuery))

    JHUcompQuery = "SELECT program FROM applicants WHERE degree = 'Masters' AND program LIKE '%Computer Science%' AND program LIKE '%Johns Hopkins%'"
    JHUCSnum = len(runquery(connection, JHUcompQuery))
    # print(f"1. applicant of spring 2025: {len(Fall25)}")
    # print(f"2. International percentage: {interper:.2f}%")
    # print(f"3. Average GPA: {gpa}, Average GRE {gre}, Average GREV {grev}, Average GRE AW {greaw}")
    # print(f"4. Average GPA American: {usgpaavg}")
    # print(f"5. Accepted Percent: {acceptedperc}")
    # print(f"6. Average GPA Acceptance: {acceptavg}")
    # print(f"7. JHU Masters Computer Science count: {JHUCSnum}")

    return {
        'fall_2025_applicants': len(Fall25),
        'international_percentage': f"{interper:.2f}%",
        'average_gpa': f"{gpa:.2f}",
        'average_gre': f"{gre:.0f}",
        'average_gre_verbal': f"{grev:.0f}",
        'average_gre_aw': f"{greaw:.1f}",
        'us_average_gpa': f"{usgpaavg:.2f}",
        'acceptance_rate': f"{acceptedperc:.1f}%",
        'accepted_average_gpa': f"{acceptavg:.2f}",
        'jhu_cs_masters': JHUCSnum,
        'total_applicants': total_count
    }


if __name__ == "__main__":
    get_all_statistics()