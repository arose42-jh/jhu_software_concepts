"""
Module for querying applicant statistics from the PostgreSQL database.

Provides functions to run SQL queries and aggregate statistics for reporting.
"""

import statistics
import psycopg
from psycopg import sql

#Connect to Database
connection = psycopg.connect(
    dbname = "applicants",
    user = "postgres"
    )

#builds the query execute
def runquery(db_connection, query, parameters = None):
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
    cursor.execute(query, parameters)
    # Makes a list instead of tuple
    result = [r[0] for r in cursor.fetchall()]
    return result

#All the desired queries go here
def get_all_statistics(table, column, limit,):
    """
    Run multiple queries to gather statistics about applicants.

    Returns:
        dict: Dictionary containing statistics such as applicant counts, averages, and percentages.
    """
    total_count_query = sql.SQL("SELECT {id_col} FROM {table} LIMIT {limit}").format(
        id_col=sql.Identifier("id"),
        table=sql.Identifier("applicants")
    )
    total_count = len(runquery(connection, total_count_query))

    fall_25_query = sql.SQL("SELECT {id_col} FROM {table} WHERE {term_col} = %s LIMIT {limit}").format(
        id_col=sql.Identifier("id"),
        table=sql.Identifier("applicants"),
        term_col=sql.Identifier("term")
    )
    fall_25 = runquery(connection, fall_25_query, ("Fall 2025",))

    international_query = sql.SQL("SELECT {id_col} FROM {table} WHERE {nationality_col} = %s LIMIT {limit}").format(
        id_col=sql.Identifier("id"),
        table=sql.Identifier("applicants"),
        nationality_col=sql.Identifier("us_or_international")
    )
    inter_count = len(runquery(connection, international_query, ("International",)))
    inter_percent = inter_count / total_count * 100

    gpa_query = sql.SQL("SELECT {gpa_col} FROM {table} WHERE {gpa_col} IS NOT NULL LIMIT {limit}").format(
        gpa_col=sql.Identifier("gpa"),
        table=sql.Identifier("applicants")
    )
    gpa_values = runquery(connection, gpa_query)
    gpa = statistics.mean(gpa_values)

    gre_query = sql.SQL("SELECT {gre_col} FROM {table} WHERE {gre_col} IS NOT NULL LIMIT {limit}").format(
        gre_col=sql.Identifier("gre"),
        table=sql.Identifier("applicants")
    )
    gre_values = runquery(connection, gre_query)
    gre = statistics.mean(gre_values)

    grev_query = sql.SQL("SELECT {gre_v_col} FROM {table} WHERE {gre_v_col} IS NOT NULL LIMIT {limit}").format(
        gre_v_col=sql.Identifier("gre_v"),
        table=sql.Identifier("applicants")
    )
    grev_values = runquery(connection, grev_query)
    grev = statistics.mean(grev_values)

    greaw_query = sql.SQL("SELECT {gre_aw_col} FROM {table} WHERE {gre_aw_col} IS NOT NULL LIMIT {limit}").format(
        gre_aw_col=sql.Identifier("gre_aw"),
        table=sql.Identifier("applicants")
    )
    greaw_values = runquery(connection, greaw_query)
    greaw = statistics.mean(greaw_values)

    us_gpa_query = sql.SQL("""
        SELECT {gpa_col} FROM {table} 
        WHERE {gpa_col} IS NOT NULL 
        AND {nationality_col} = %s 
        AND {term_col} = %s
        LIMIT {limit}
    """).format(
        gpa_col=sql.Identifier("gpa"),
        table=sql.Identifier("applicants"),
        nationality_col=sql.Identifier("us_or_international"),
        term_col=sql.Identifier("term")
    )
    us_gpa_values = runquery(connection, us_gpa_query, ("American", "Fall 2025"))
    us_gpa_avg = statistics.mean(us_gpa_values)

    accepted_query = sql.SQL("""
        SELECT {status_col} FROM {table} 
        WHERE {status_col} LIKE %s 
        AND {term_col} = %s
        LIMIT {limit}
    """).format(
        status_col=sql.Identifier("status"),
        table=sql.Identifier("applicants"),
        term_col=sql.Identifier("term")
    )
    accepted_count = len(runquery(connection, accepted_query, ("Accepted%", "Fall 2025")))
    acceptedperc = accepted_count / len(fall_25) * 100

    accpt_gpa_query = ("SELECT gpa FROM applicants WHERE status "
                       "LIKE 'Accepted%' AND term = 'Fall 2025' AND gpa IS NOT NULL")
    acceptavg = statistics.mean(runquery(connection, accpt_gpa_query))

    jhu_comp_query = sql.SQL("""
        SELECT {program_col} FROM {table} 
        WHERE {degree_col} = %s 
        AND {program_col} LIKE %s 
        AND {program_col} LIKE %s
        LIMIT {limit}
    """).format(
        program_col=sql.Identifier("program"),
        table=sql.Identifier("applicants"),
        degree_col=sql.Identifier("degree"),
        limit = sql.Literal(limit)
    )
    jhu_cs_num = len(runquery(connection, jhu_comp_query,
                               ("Masters", "%Computer Science%", "%Johns Hopkins%")))

    return {
        'fall_2025_applicants': len(fall_25),
        'international_percentage': f"{inter_percent:.2f}%",
        'average_gpa': f"{statistics.mean(runquery(connection, gpa)):.2f}",
        'average_gre': f"{statistics.mean(runquery(connection, gre)):.0f}",
        'average_gre_verbal': f"{grev:.0f}",
        'average_gre_aw': f"{greaw:.1f}",
        'us_average_gpa': f"{us_gpa_avg:.2f}",
        'acceptance_rate': f"{acceptedperc:.1f}%",
        'accepted_average_gpa': f"{acceptavg:.2f}",
        'jhu_cs_masters': jhu_cs_num,
        'total_applicants': total_count
    }


if __name__ == "__main__":
    print(get_all_statistics())
