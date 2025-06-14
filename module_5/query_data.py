"""
Module for querying applicant statistics from the PostgreSQL database.

Provides functions to run SQL queries and aggregate statistics for reporting.
"""

import statistics
import psycopg

#Connect to Database
connection = psycopg.connect(
    dbname = "applicants",
    user = "postgres"
    )

#builds the query execute
def runquery(db_connection, query):
    """
    Execute a SQL query and return the first column of all results as a list.

    Args:
        db_connection: psycopg database connection object.
        query (str): SQL query to execute.
    Returns:
        list: List of values from the first column of the query result.
    """
    cursor = db_connection.cursor()
    result = None
    cursor.execute(query)
    # Makes a list instead of tuple
    result = [r[0] for r in cursor.fetchall()]
    return result

#All the desired queries go here
def get_all_statistics():
    """
    Run multiple queries to gather statistics about applicants.

    Returns:
        dict: Dictionary containing statistics such as applicant counts, averages, and percentages.
    """
    total_count = len(runquery(connection, "SELECT id FROM applicants"))

    fall_25 = runquery(connection, "SELECT id FROM applicants WHERE term='Fall 2025'")

    inter_percent = (len(runquery(connection, "SELECT id FROM applicants WHERE "
                                  "us_or_international = 'International'"))/total_count * 100)

    gpa = statistics.mean(runquery(connection, "SELECT gpa FROM applicants WHERE gpa IS NOT NULL"))

    gre = statistics.mean(runquery(connection, "SELECT gre FROM applicants WHERE gre IS NOT NULL"))

    grev = statistics.mean(runquery(connection,
                                     "SELECT gre_v FROM applicants WHERE gre_v IS NOT NULL"))

    greaw = statistics.mean(runquery(connection,
                                     "SELECT gre_aw FROM applicants WHERE gre_aw IS NOT NULL"))

    us_gpa_query = ("SELECT gpa FROM applicants WHERE gpa IS NOT NULL "
                    "AND us_or_international = 'American' AND term = 'Fall 2025'")
    usgpaavg = statistics.mean(runquery(connection, us_gpa_query))

    accepted_spr_query = ("SELECT status FROM applicants WHERE "
                          "status LIKE 'Accepted%' AND term = 'Fall 2025'")
    acceptedperc = (len(runquery(connection, accepted_spr_query))
                    / len(fall_25) * 100)

    accpt_gpa_query = ("SELECT gpa FROM applicants WHERE status "
                       "LIKE 'Accepted%' AND term = 'Fall 2025' AND gpa IS NOT NULL")
    acceptavg = statistics.mean(runquery(connection, accpt_gpa_query))

    jhu_comp_query = ("SELECT program FROM applicants WHERE degree = 'Masters' "
                      "AND program LIKE '%Computer Science%' AND program LIKE '%Johns Hopkins%'")
    jhu_cs_num = len(runquery(connection, jhu_comp_query))

    return {
        'fall_2025_applicants': len(fall_25),
        'international_percentage': f"{inter_percent:.2f}%",
        'average_gpa': f"{statistics.mean(runquery(connection, gpa)):.2f}",
        'average_gre': f"{statistics.mean(runquery(connection, gre)):.0f}",
        'average_gre_verbal': f"{grev:.0f}",
        'average_gre_aw': f"{greaw:.1f}",
        'us_average_gpa': f"{usgpaavg:.2f}",
        'acceptance_rate': f"{acceptedperc:.1f}%",
        'accepted_average_gpa': f"{acceptavg:.2f}",
        'jhu_cs_masters': jhu_cs_num,
        'total_applicants': total_count
    }


if __name__ == "__main__":
    get_all_statistics()
