import traceback, bs4, requests

baseUrl = 'http://23.225.154.235'
url = baseUrl + '/6_6703/9740792.html'

def writeFile(text):
  try:
    write_to_file = open("九玄之王.txt", "a")
    print("The variable, text is of type:", type(text))
    write_to_file.writelines(text)
    write_to_file.close()
  except Exception as e:
    print(e)
    write_to_file.close()

def parseText(url):
  novel = requests.get(url)
  novel.encoding = "GBK"
  return bs4.BeautifulSoup(novel.text, "html.parser")

def saveTextFrom(url):
  soup = parseText(url)
  text = soup.get_text()
  writeFile(text)
  child_soup = soup.find_all('a', string="下一章", href=True)
  print(child_soup)
  for i in child_soup:
      print(i.string)
      if(i.string == "下一章"):
        href = i['href']
        if(href == "/6_6703/"):
          return
        else:
          saveTextFrom(baseUrl + href)
          print(href)
        return
  return

try:
  saveTextFrom(url)
except Exception as e:
  print(e)