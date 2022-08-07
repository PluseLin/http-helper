# http-helper

## 1.Introduction

This project is a single program which enable user to input HTTP URL, HTTP method and json data and receive data from HTTP server.

Currently GET,POST,PUT,DELETE methods are available.

I will keep updating in the future.

## 2.How to use

Just git clone and run main.py in python 3.x.

Executable file for Windows will come soon.

## 3.Cautions

1. This program can only send JSON file and "json.loads" is used to convert string to json data,so you SHOULD **ADD DOUBLE QUOTES** when using strings.
2. Unicode decode is not available,so you may see "\uxxxx" in received data.Solution may come soon in subsequent versions.

## 2.versions

* v1.0: GET,POST,PUT,DELETE methods
