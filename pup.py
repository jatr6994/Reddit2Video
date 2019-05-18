import asyncio
from pyppeteer import launch
import time
import imageio
import os

async def main():
	browser = await launch(headless=False)
	page = await browser.newPage()
	await page.setViewport({'width': 1920, 'height': 1080 })
	await page.goto('file:///C:/Users/Jacob/Desktop/Reddit2Video/cssAnim.html')
	audio_len = 1 # 10 sec
	time = 0
	frame = 0
	while time < audio_len:
		frame_num = str(frame).zfill(4)
		frame += 1
		time += (1/60)
		print(time)
		try:
			await page.screenshot({'path': f'frames/example_{frame_num}.png'})
		except:
			break
	await browser.close()


asyncio.get_event_loop().run_until_complete(main())

filenames = [ "frames/" + img for img in os.listdir( "frames" ) if img.endswith( ".png" ) ]
with imageio.get_writer('movie.mp4', mode='I', fps=60) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)