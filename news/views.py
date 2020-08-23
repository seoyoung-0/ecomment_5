import requests, json, cssutils
from bs4 import BeautifulSoup
from django.db import IntegrityError
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Ecomment.settings")
# import django
# django.setup()
## BlogData를 import해옵니다
from news.models import SearchNews

class GetPolicyView(View):
    def get(self, request):
        policy_url = 'http://www.chemicalnews.co.kr/news/articleList.html?sc_section_code=S1N1&view_type=sm'
        req = requests.get(policy_url)
        req.encoding = 'utf-8'
        html = req.text

        soup = BeautifulSoup(html, 'html.parser')
        list_items = soup.find_all('div', class_='list-block')

        policy_data = []
        chemical = 'http://www.chemicalnews.co.kr/'

        for item in list_items:
            
            title = item.find('div',class_='list-titles').text

            link = item.find('div',class_='list-image').find('a')
            if 'href' in link.attrs:
                conn = link.attrs['href']

            image= item.find('div',class_='list-image')['style']
            
            style = cssutils.parseStyle(image)
            url = style['background-image']
            url = url.replace('url(.','').replace(')','')

            content = item.find('p',class_='list-summary').text

            etc = item.find('div',class_='list-dated').text
            
            policy_data.append(
                {
                'title': title,
                'link': chemical + conn,
                'img': chemical + 'news/'+ url,
                'content': content[0:150],
                'etc': etc
                }
            )
        return render(request, 'news/policy.html',{'policy_data' : policy_data})
        # return JsonResponse({'policy_data' : policy_data}, status = 200, json_dumps_params={'ensure_ascii': False})  
        # 결과를 JsonResponse 규격에 맞는 dictionary형태로 return해준다.
