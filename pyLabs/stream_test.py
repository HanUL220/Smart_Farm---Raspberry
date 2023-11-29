import io
import picamera
import logging
from threading import Condition
from http.server import BaseHTTPRequestHandler, HTTPServer
import serial
import threading

# 아두이노 데이터를 가져오는 시리얼 포트 설정
ser = serial.Serial('/dev/ttyACM0', 9600)

# 아두이노 데이터를 보관하는 변수
arduino_data = ""

# 아두이노 데이터를 주기적으로 업데이트하는 함수
def update_arduino_data():
    global arduino_data
    while True:
        arduino_data = ser.readline().decode().strip()

# 아두이노 데이터 업데이트를 백그라운드 스레드로 시작
update_thread = threading.Thread(target=update_arduino_data)
update_thread.daemon = True
update_thread.start()

# 웹 페이지 HTML 템플릿
PAGE = """\
<html>
<head>
<title>Smart Farm streaming</title>
</head>
<body>
<h1>Smart Farm streaming</h1>
<img src="stream.mjpg" width="960" height="640" />

<h1>Arduino Data</h1>
<p id="arduino-data">{}</p>

<script>
    // 이 함수는 주기적으로 데이터를 가져와서 업데이트합니다.
    function updateArduinoData() {
        const arduinoDataElement = document.getElementById('arduino-data');
        arduinoDataElement.textContent = "{}";
    }

    // 일정한 간격으로 데이터 업데이트 함수를 호출합니다.
    setInterval(updateArduinoData, 1000);  // 1초마다 업데이트 (1000ms)
</script>
</body>
</html>
"""

class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

class StreamingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            # 아두이노 데이터를 HTML 페이지로 전달
            content = PAGE.format(arduino_data, arduino_data).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                logging.warning('Removed streaming client %s: %s', self.client_address, str(e))
        else:
            self.send_error(404)
            self.end_headers()

class StreamingServer(HTTPServer):
    allow_reuse_address = True
    daemon_threads = True

# 카메라 설정
with picamera.PiCamera(resolution='1920x1080', framerate=30) as camera:
    output = StreamingOutput()
    camera.start_recording(output, format='mjpeg')
    try:
        address = ('', 8000)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    finally:
        camera.stop_recording()
