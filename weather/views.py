from django.shortcuts import render
import requests
import json
# from .forms import CityForm
# from .models import City

# Create your views here.
def index(request):
    city_data = request.get("")
    context = {
        "message":"Hello World",
        # "form":form,
        # "city":city
    }
    return render(request,'weather/index.html',context)

def get_weather(city):
    # 一個前のweatherAPIの時に使ったやつの流用
    cities = {
        "北海道":"016010",
        "青森県":"020010",
        "岩手県":"030010",
        "宮城県":"040010",
        "秋田県":"050010",
        "山形県":"060010",
        "福島県":"070010",
        "茨城県":"080010",
        "栃木県":"090010",
        "群馬県":"100010",
        "埼玉県":"110010",
        "千葉県":"120010",
        "東京都":"130010",
        "神奈川県":"1440010",
        "新潟県":"150010",
        "富山県":"160010",
        "石川県":"170010",
        "福井県":"180010",
        "山梨県":"190010",
        "長野県":"200010",
        "岐阜県":"210010",
        "静岡県":"220010",
        "愛知県":"230010",
        "三重県":"240010",
        "滋賀県":"250010",
        "京都府":"260010",
        "大阪府":"270000",
        "兵庫県":"280010",
        "奈良県":"290010",
        "和歌山県":"300010",
        "鳥取県":"310010",
        "島根県":"320010",
        "岡山県":"330010",
        "広島県":"340010",
        "山口県":"350010",
        "徳島県":"360010",
        "香川県":"370010",
        "愛媛県":"380010",
        "高知県":"390010",
        "福岡県":"400010",
        "佐賀県":"410010",
        "長崎県":"420010",
        "熊本県":"430010",
        "大分県":"440010",
        "宮崎県":"450010",
        "鹿児島県":"460010",
        "沖縄県":"470010",
    }
    params = cities[city]
    url = f"https://weather.tsukumijima.net/api/forecast?city={params}"
    response = requests.get(url,verify=False)
    data = response.json()
    return data

def wether(request):
    if request.method == "POST":
        city = request.POST["address"]
    data = get_weather(city)["forecasts"][0]
    context = {
        "weather":{
            "date":data["date"],
            "telop":data["telop"],
            "temperature":{
                "max":data["temperature"]["max"]["celsius"] or "情報がありませんでした。",
                "min":data["temperature"]["min"]["celsius"] or "情報がありませんでした。",
            },
        },
        "weathers":data,
        "city":city,
        "image":{
            "tag":data["image"]["title"],
            "url":data["image"]["url"],
        },
    }
    return render(request,'weather/weather.html',context)