from flask import Flask, jsonify, abort, make_response, request,render_template
import sys, sqlite3, requests, datetime, time, re, json, optparse
import xmltodict
import helpers
import platform
import serial
app = Flask(__name__)

start = int(round(time.time()))
print("api running")

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

@app.route("/", methods=['GET', 'POST'])
def parse_xml():
    x= request.data
    print(x)
    content_dict = xmltodict.parse(x)
    print(content_dict["EventNotificationAlert"]["ipAddress"])
    if(content_dict["EventNotificationAlert"]["ipAddress"] == "192.168.10.80"):
        print("Test data")
        ser.write(b"a")
    if(content_dict["EventNotificationAlert"]["ipAddress"] == "192.168.100.21"):
        print("Front data")
        ser.write(b"a")
    if(content_dict["EventNotificationAlert"]["ipAddress"] == "192.168.100.22"):
        print("Right data")
        ser.write(b"b")
    if(content_dict["EventNotificationAlert"]["ipAddress"] == "192.168.100.23"):
        print("Rear data")
        ser.write(b"c")
    if(content_dict["EventNotificationAlert"]["ipAddress"] == "192.168.100.24"):
        print("Left data")
        ser.write(b"d")
    return content_dict

if __name__ == '__main__':
    print("Starting python app")
    app.run(host='0.0.0.0', port=8080, debug=False)
