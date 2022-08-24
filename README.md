# http-helper

## 1.Introduction

This project is a single program which enable user to input HTTP URL, HTTP method and json data and receive data from HTTP server.

Currently GET,POST,PUT,DELETE methods are available.

I will keep updating in the future.

## 2.How to use

Just git clone and run main.py in python 3.x.

Executable file for Windows will come soon.

## 3.Cautions

1. This program can only send JSON file and "json.loads" is used to convert string to json data,so you should **ADD DOUBLE QUOTES** when using strings.
2. Unicode decode is not available,so you may see "\uxxxx" in received data.Solution may come soon in subsequent versions.

## 4.versions

* v1.0: GET,POST,PUT,DELETE methods.
* v1.1: Add function that user can select json file for input and dump received data to json files.
* v1.2: Repair the bug that GET method will meet error if send data is None.(That means all GET method cannot carry any json data.)
