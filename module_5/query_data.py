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
def get_all_statistics():
    """
    Run multiple queries to gather statistics about applicants.

    Returns:
        dict: Dictionary containing statistics such as applicant counts, averages, and percentages.
    """
    total_count_query = sql.SQL("SELECT {id_col} FROM {table} LIMIT {limit}").format(
        id_col=sql.Identifier("id"),
        table=sql.Identifier("applicants"),
        limit = sql.Literal(10000)
    )
    total_count = len(runquery(connection, total_count_query))

    fall_25 = runquery(
        connection,
        sql.SQL("""
            SELECT {id_col} 
            FROM {table} 
            WHERE {term_col} = %s 
            LIMIT {limit}""").format(
            id_col=sql.Identifier("id"),
            table=sql.Identifier("applicants"),
            term_col=sql.Identifier("term"),
            limit = sql.Literal(10000)),("Fall 2025",))

    inter_count = len(runquery(
        connection,
        sql.SQL("SELECT {id_col} FROM {table} WHERE {nationality_col} = %s LIMIT {limit}").format(
            id_col=sql.Identifier("id"),
            table=sql.Identifier("applicants"),
            nationality_col=sql.Identifier("us_or_international"),
            limit = sql.Literal(10000)
        ),
        ("International",)
    ))
    inter_percent = inter_count / total_count * 100

    gpa_values = runquery(
        connection,
        sql.SQL("SELECT {gpa_col} FROM {table} WHERE {gpa_col} IS NOT NULL LIMIT {limit}").format(
            gpa_col=sql.Identifier("gpa"),
            table=sql.Identifier("applicants"),
            limit = sql.Literal(10000)
        )
    )
    gre_values = runquery(
        connection,
        sql.SQL("SELECT {gre_col} FROM {table} WHERE {gre_col} IS NOT NULL LIMIT {limit}").format(
            gre_col=sql.Identifier("gre"),
            table=sql.Identifier("applicants"),
            limit = sql.Literal(10000)
        )
    )
    grev = statistics.mean(runquery(
        connection,
        sql.SQL("""
                SELECT {gre_v_col} 
                FROM {table} 
                WHERE {gre_v_col} IS NOT NULL 
                LIMIT {limit}""").format(
            gre_v_col=sql.Identifier("gre_v"),
            table=sql.Identifier("applicants"),
            limit = sql.Literal(10000)
        )
    ))
    greaw = statistics.mean(runquery(
        connection,
        sql.SQL("""
                SELECT {gre_aw_col} 
                FROM {table} 
                WHERE {gre_aw_col} IS NOT NULL 
                LIMIT {limit}""").format(
            gre_aw_col=sql.Identifier("gre_aw"),
            table=sql.Identifier("applicants"),
            limit = sql.Literal(10000)
        )
    ))
    us_gpa_avg = statistics.mean(runquery(
        connection,
        sql.SQL("""
            SELECT {gpa_col} FROM {table} 
            WHERE {gpa_col} IS NOT NULL 
            AND {nationality_col} = %s 
            AND {term_col} = %s
            LIMIT {limit}
        """).format(
            gpa_col=sql.Identifier("gpa"),
            table=sql.Identifier("applicants"),
            nationality_col=sql.Identifier("us_or_international"),
            term_col=sql.Identifier("term"),
            limit = sql.Literal(10000)
        ),
        ("American", "Fall 2025")
    ))
    accepted_count = len(runquery(
        connection,
        sql.SQL("""
            SELECT {status_col} FROM {table} 
            WHERE {status_col} LIKE %s 
            AND {term_col} = %s
            LIMIT {limit}
        """).format(
            status_col=sql.Identifier("status"),
            table=sql.Identifier("applicants"),
            term_col=sql.Identifier("term"),
            limit = sql.Literal(10000)
        ),
        ("Accepted%", "Fall 2025")
    ))
    fall_25_count = len(runquery(
        connection,
        sql.SQL("""
            SELECT {id_col} 
            FROM {table} 
            WHERE {term_col} = %s 
            LIMIT {limit}""").format(
            id_col=sql.Identifier("id"),
            table=sql.Identifier("applicants"),
            term_col=sql.Identifier("term"),
            limit = sql.Literal(10000)),("Fall 2025",)))
  
    acceptedperc = accepted_count / fall_25_count * 100
    acceptavg = statistics.mean(runquery(
        connection,
        sql.SQL("""
        SELECT {gpa_col} FROM {table} 
        WHERE {status_col} LIKE %s 
        AND {term_col} = %s 
        AND {gpa_col} IS NOT NULL
        LIMIT {limit}
    """).format(
        gpa_col=sql.Identifier("gpa"),
        table=sql.Identifier("applicants"),
        status_col=sql.Identifier("status"),
        term_col=sql.Identifier("term"),
        limit = sql.Literal(10000)
    ),
    ("Accepted%", "Fall 2025")
    ))
    jhu_cs_num = len(runquery(
        connection,
        sql.SQL("""
            SELECT {program_col} FROM {table} 
            WHERE {degree_col} = %s 
            AND {program_col} LIKE %s 
            AND {program_col} LIKE %s
            LIMIT {limit}
        """).format(
            program_col=sql.Identifier("program"),
            table=sql.Identifier("applicants"),
            degree_col=sql.Identifier("degree"),
            limit = sql.Literal(10000)
        ),
        ("Masters", "%Computer Science%", "%Johns Hopkins%")
    ))

    return {
        'fall_2025_applicants': len(fall_25),
        'international_percentage': f"{inter_percent:.2f}%",
        'average_gpa': f"{statistics.mean(gpa_values):.2f}",
        'average_gre': f"{statistics.mean(gre_values):.0f}",
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
