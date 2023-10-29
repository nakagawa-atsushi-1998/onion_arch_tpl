import socketserver
import http.server
import threading


class WebServer:
    def __init__(
        self,
        port:int=8000
    ):
        self.port=port
        self.server=None
        self.thread=None
    
    def is_runnning(self):
        try: return self.thread.is_alive()
        except: return False

    def start(self):
        if not self.server: pass
        else: return None
        self.server = socketserver.TCPServer(('', self.port), http.server.SimpleHTTPRequestHandler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        print(f'WebServer Thread: started.')

    def stop(self):
        if self.server: pass
        else: return None
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()
        print(f'WebServer Thread: stopped.')

    def restart(self):
        self.stop()
        self.start()


if __name__ == '__main__':
    web_server = WebServer()
    web_server.start() # Webサーバ起動
    try: input('Main Thread: waiting.')
    except KeyboardInterrupt: pass
    web_server.stop() # Webサーバ停止

