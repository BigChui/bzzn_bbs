# !/usr/bin/env python3
# - * - coding:utf-8 - * -
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """系统主页面"""
    return "hello world!"

if __name__ == "__main__":
    app.run(debug=True)

