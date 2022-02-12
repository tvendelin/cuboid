#!/usr/bin/python3
from appserver import create_api

app = create_api()

if __name__ == '__main__':
    app.run()
