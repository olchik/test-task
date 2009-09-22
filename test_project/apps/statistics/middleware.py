"""
Statistical data middlewares
"""
from django.db import connection
from statistics.models import SQLLog


class SQLLogMiddleware():
    """
    Middleware, that saves into database information about db requests
    """

    def process_response(self, request, response):
        sql = curr_sql = ""
        time = 0.0
        for query in connection.queries:
            time += float(query['time'])
            curr_sql = query["sql"]
        if curr_sql:
            sql = sql + "\r\n" + curr_sql
        log = SQLLog(url=request.path, execution_time=time,
raw_sql=sql)
        log.save()
        return response
