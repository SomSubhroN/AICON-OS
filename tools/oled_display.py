from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from PIL import Image, ImageDraw, ImageFont
import time
import sys

sys.path.append("/home/somsubhro/aicon")
from core.monitor import get_stats

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)
font = ImageFont.load_default()
while True:
	image = Image.new("1", (device.width, device.height))
	draw = ImageDraw.Draw(image)
	stats = get_stats()
	cpu = stats["cpu"]
	mem = stats["memory"]
	temp = stats["temp"]
	draw.text((0, 0), "AICON OS", font=font, fill=255)
	draw.text((0, 15), f"CPU: {cpu}%", font=font, fill=255)
	draw.text((0, 30), f"RAM: {mem}%", font=font, fill=255)
	draw.text((0, 45), temp, font=font, fill=255)

	device.display(image)
	time.sleep(1)
