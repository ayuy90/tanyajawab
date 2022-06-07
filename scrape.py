from lxml import html
import requests
import json
import base64
import time
file = open("nomor-brainly-id.txt","r")
startnum = file.readlines()[0]
j = startnum
n = 8000000
for i in range(int(j), n):
    link = ("https://brainly.co.id/tugas/" + str(i))
    fetch = requests.get(link)
    status = fetch.status_code
    if status == 200:
        file1 = open("nomor-brainly-id.txt","w")
        file1.writelines(str(i))
        file1.close()
        print (link)
        tree = html.fromstring(fetch.content) 
        title = tree.xpath('//h1[@data-testid="question_box_text"]/span/text()')
        questiontree = tree.xpath('//div[@data-testid="question_container"]/div[2]/div[1]')[0]
        try:
            isi = tree.xpath('//div[contains(concat (" ", normalize-space(@data-testid), " "), "answer_box_text")]')[0]
            isii = str(html.tostring(isi))
        except IndexError:
            isi = ''
            isii = isi
        isiii = str(title)
        br = "</br>"
        question = str(html.tostring(questiontree)).replace("\\n",  br).replace("\\xa0", "").replace("\\u", "").replace("u'", "'").replace("'", "").replace("u\xa0,", "").replace("u'", "").replace("[", "").replace("]", "").replace("b<", "<")
        mytext = isii.replace("\\n",  br).replace("\\xa0", "").replace("\\u", "").replace("u'", "'").replace("'", "").replace("u\xa0,", "").replace("u'", "").replace("[", "").replace("]", "")
        juduls = isiii.replace("\\n",  '').replace("\\xa0", "").replace("\\u", "").replace("u'", "'").replace("'", "").replace("u\xa0,", "").replace("u'", "").replace("[", "").replace("]", "")
        description = '<h1>Pertanyaan :</h1>'+ question + '&ensp;' + '<h2>Jawaban :</h2>'+ mytext
        url = "https://edubrain.digital/wp-json/wp/v2/posts"
        user = "Administrator"
        password = "ua5y Yulo Cjz7 iFt9 LXL4 Z2qC"
        credentials = user + ':' + password
        token = base64.b64encode(credentials.encode())
        header = {'Authorization': 'Basic ' + token.decode('utf-8')}
        post = {
            'title'    : title,
            'status'   : 'publish', 
            'content'  : description,
            'slugs': 'tanya-jawab'
        }
        responce = requests.post(url , headers=header, data=post)
        resp = responce.status_code
        if resp == 201:
            print (resp)
            time.sleep(2)
file.close()
