# Creator: Karan Singla
# Date: 10 Oct 2022

from urllib.parse import urlparse, parse_qs
from sqlite.sqlite_helper import SqliteHelper


class ApiBase:
    __sqliteHelperObj = SqliteHelper.instance()

    def __init__(self):
        pass

    def parse_query_params(self, path):
        self.__sqliteHelperObj.use_database_query()
        parsed = parse_qs(urlparse(path).query)
        return parsed

    def return_success_response(self, response, server):
        server.send_response(200, response)
        server.send_header("Content-type", "text/html")
        server.end_headers()
        server.wfile.write(bytes(str(response), "utf-8"))
