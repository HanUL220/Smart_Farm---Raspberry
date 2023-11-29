import time
import board
import busio
import digitalio
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# SPI 버스 및 MCP3008 설정
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)  # MCP3008의 CS/CE 핀 번호에 맞게 설정
mcp = MCP.MCP3008(spi, cs)

# 아날로그 입력 채널 설정 (0부터 7까지)
channel = AnalogIn(mcp, MCP.P0)

while True:
    # 조도 값을 읽고 출력
    print("조도 값: {:.2f}".format(channel.voltage))
    time.sleep(1)
