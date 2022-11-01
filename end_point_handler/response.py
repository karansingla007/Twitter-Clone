def returnSuccessResponse(self, response):
    self.send_response(200, response)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(bytes(str(response), "utf-8"))