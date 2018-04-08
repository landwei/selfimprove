import websocket
import time
import sys
import json
import hashlib
import zlib
import base64
import logging
import os
import pika
import logging.handlers 
import csv
import traceback
import Queue
import threading


if __name__ == "__main__":
    ws = websocket.WebSocket()
    ws.connect('wss://api.bitfinex.com/ws/2')
    #ws.send(json.dumps({'event': 'ping'})) 
    ws.send('{"event":"subscribe","channel":"ticker","symbol":"tBTCUSD"}')
    while True:
        data = ws.recv()
        print data 
    ws.close()
