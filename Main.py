from selenium import webdriver
path = "c:\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(path)
url = "https://www.youtube.com/channel/UCKQdc0-Targ4nDIAUrlfKiA"
driver.get(url)

videos = driver.find_elements_by_class_name ('style-scope ytd-grid-video-renderer')
for video in videos:
    title = video.find_element_by_xpath('.//*[@id="video-title"]').text
    views = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text
    date = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text
    print(f'{title}{views}{date}')
