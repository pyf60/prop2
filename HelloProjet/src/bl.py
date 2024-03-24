import requests
import chardet
from lxml import html


for i in range(81000, 90000):
    url = f'http://htvzj.com/gxdz/202012/{i}.html'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/121.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        encoding = chardet.detect(response.content)['encoding']
        response.encoding = encoding
        html_content = html.fromstring(response.text)
        elements = html_content.xpath('//*[@id="fontzoom"]')



        for element in elements:
            # 将内容保存到文件
            file_path = './duanzi/'+ str(i) + '.txt'
            with open(file_path, 'w', encoding='utf-8') as file:
                web_content_lines = element.text_content().splitlines()
                web_content = '\n'.join(line for line in web_content_lines if line.strip())
                file.write(web_content)
                print(f'访问网页: {url}')
    else:
        print(f'无法访问----------------------------------------》: {url}')
print('任务完成')