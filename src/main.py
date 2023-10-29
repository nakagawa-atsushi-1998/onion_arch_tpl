import webserver


def main():
    web_server = webserver.WebServer()
    web_server.start() # Webサーバ起動
    try: input('Main Thread: waiting.')
    except KeyboardInterrupt: pass
    web_server.stop() # Webサーバ停止


if __name__ == '__main__':
    main()

