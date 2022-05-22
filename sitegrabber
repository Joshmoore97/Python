from multiprocessing.connection import wait
from selenium import webdriver
import webbrowser

driver = webdriver.Chrome("C:/tmp/chromedriver.exe")
urls = ["https://youtube.com", "https://cmcmarkets.com", "https://bbc.com", "https://urlscan.io", "https://itv.com", "https://twitch.tv", "https://linkedin.com"]
html = '<table style="border-collapse: collapse; width: 100%; height: 54px;" border="1"><tbody><tr style="height: 18px;"><td style="width: 50%; height: 18px;">Site</td><td style="width: 50%; height: 18px;">Image</td></tr><tr style="height: 18px;">'
filepath = "C:/Users/ox_jo/OneDrive/Documents/Visual Studio/Python/"
filename = "sites.html"
file = open(f"{filename}", "w")

for url in urls:
    name = url.split("//")[1]
    driver.get(url)
    driver.get_screenshot_as_file(f"{name}.png")
    html += f'<td style="width: 50%; height: 18px;">{name}</td> <td style="width: 50%; height: 18px;"><img src="pc" alt="" /><img src="{filepath}{name}.png" alt="" width=1000 /></td> </tr>'
driver.close()

html += "</tbody> </table>"

file.write(html)
webbrowser.open_new_tab(filename)
