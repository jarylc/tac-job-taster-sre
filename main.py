from http.server import BaseHTTPRequestHandler, HTTPServer

HOST_NAME = "127.0.0.1"
PORT = 8081


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(
            bytes(f"# HELP balance Current balance in bank\n# TYPE balance gauge\nbalance {_get_balance()}", "utf-8")
        )
        _reduce_balance_by_expense()

    def log_message(self, format, *args):
        return


def _get_balance() -> str:
    with open("balance.txt", "r", encoding="utf-8") as f:
        return f.read()


def _reduce_balance_by_expense():
    with open("expense.txt", "r", encoding="utf-8") as e:
        expense = int(e.read())
        with open("income.txt", "r", encoding="utf-8") as i:
            income = int(i.read())
            with open("balance.txt", "r+", encoding="utf-8") as b:
                balance = int(b.read())
                final = max(balance - expense + income, 0)
                b.seek(0)
                b.write(str(final))
                b.truncate()


if __name__ == "__main__":
    web_server = HTTPServer((HOST_NAME, PORT), MyServer)
    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass
    web_server.server_close()
    print("Server stopped.")
