from bs4 import BeautifulSoup
import requests


url = 'https://www.airbnb.com/s/Rawalpindi-Cantt/homes?refinement_paths%5B%5D=%2Fhomes&search_type=filter_change&tab_id=home_tab&place_id=ChIJy5pBdImU3zgRD9MyFn41hAk&date_picker_type=calendar&checkin=2021-02-11&checkout=2021-02-13&source=structured_search_input_header'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

images = soup.find_all('img')

for image in images:
	link = image['src']
	name = image['alt']
	# with open(name.replace(' ', '-').replace('/', '').replace('!','').replace('|','-')+'.jpg', 'wb') as f:
	# 	im = requests.get(link)
	# 	f.write(im.content)
	print(f"{name} and the link is {link}\n")