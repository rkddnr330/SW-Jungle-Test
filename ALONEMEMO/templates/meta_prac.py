import requests
from bs4 import BeautifulSoup

url='https://platum.kr/archives/120958'
# 우리가 스크랩핑할 url 설정

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)
# 설정한 url에 requests.get 형식으로 가져와서 data에 담아준다.

soup = BeautifulSoup(data.text,'html.parser')   
# html 파일(data.text 형식으로 가져옴)을 soup에 담음. 왜냐하면 태그를 이용해 자유롭게 우리가 원하는 데이터들을 스크래핑하기 위해!

og_image = soup.select_one('meta[property="og:image"]')
# <meta content="https://platum.kr/wp-content/uploads/2019/04/DSC_7745-640x427.jpg" property="og:image"/>

og_title = soup.select_one('meta[property="og:title"]')
# <meta content="[Startup’s Story #449] 중국서 공유주택 열기 일으킨 창업가, 한국서 이어간다" property="og:title"/>

og_description = soup.select_one('meta[property="og:description"]')
# <meta content="" property="og:description"/>

url_image = og_image['content']
url_title = og_title['content']
url_description = og_description['content']

print(url_image)
print(url_title)
print(url_description)

