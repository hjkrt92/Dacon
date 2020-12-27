import pandas as pd #pandas로 데이터 읽기
from Arrangement.Preproicessing1 import *
from Arrangement.Colors import XKCD_COLORS
from tqdm import tqdm
pd.options.plotting.backend = 'plotly'
import plotly.io as pio
from itertools import chain
from glob import glob
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from collections import defaultdict
pio.renderers.default = 'notebook_connected'
import plotly.express as px
from IPython.display import display
import webbrowser
import seaborn as sns
from selenium import webdriver
from Codes.coordinate2 import *
import imgkit
import io
from PIL import Image
from ipywebrtc import WidgetStream, ImageRecorder
import folium
from folium.plugins import HeatMap
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

Jeju1 = r"C:\Users\Administrator\Desktop\data (1)\KRI-DAC_Jeju_data5.txt"
Jeju2 = r"C:\Users\Administrator\Desktop\data (1)\KRI-DAC_Jeju_data6.txt"
Jeju3 = r"C:\Users\Administrator\Desktop\data (1)\KRI-DAC_Jeju_data7.txt"
Jeju4 = r"C:\Users\Administrator\Desktop\data (1)\KRI-DAC_Jeju_data8.txt"
Jeju1 = pd.read_csv(Jeju1, sep=",")
Jeju2 = pd.read_csv(Jeju2, sep=",")
Jeju3 = pd.read_csv(Jeju3, sep=",")
Jeju4 = pd.read_csv(Jeju4, sep=",")

Jeju_P = pd.concat((Jeju1.loc[:,"POINT_X":"POINT_Y"] , Jeju2.loc[:,"POINT_X":"POINT_Y"] ,
                    Jeju3.loc[:,"POINT_X":"POINT_Y"] , Jeju4.loc[:,"POINT_X":"POINT_Y"]))
Jeju_Type = pd.concat((Jeju1["Type"] , Jeju2["Type"] , Jeju3["Type"] , Jeju4["Type"]))
Jeju_Class = pd.concat((Jeju1["FranClass"] , Jeju2["FranClass"] , Jeju3["FranClass"] , Jeju4["FranClass"]))
Jeju_data = pd.concat((Jeju_P, Jeju_Class, Jeju_Type),axis=1)
Jeju_data = Jeju_data.reset_index(drop=True)

Jeju_Tdict = {}
for i in Jeju_data.values:
    Jeju_Tdict[i[0],i[1],i[2],i[3]]=i[3]
Jeju_Cdict = defaultdict(list)
for i in Jeju_Tdict.keys():

    Jeju_Cdict[i[3]].append(i[2])
Type_list = list(set([i for i in Jeju_Cdict.keys()]))

##########################################################
Total_Jeju = defaultdict(list)
Jeju_Tspent = pd.concat((Jeju1["TotalSpent"] , Jeju2["TotalSpent"] , Jeju3["TotalSpent"] , Jeju4["TotalSpent"]))
Jeju_Dspent = pd.concat((Jeju1["DisSpent"] , Jeju2["DisSpent"] , Jeju3["DisSpent"] , Jeju4["DisSpent"]))
Jeju_data = pd.concat((Jeju_P, Jeju_Class, Jeju_Type,Jeju_Tspent,Jeju_Dspent),axis=1)
Jeju_data = Jeju_data.reset_index(drop=True)
Jeju_Tdict = defaultdict(list)
for i in Jeju_data.values:
    Jeju_Tdict[i[0],i[1],i[2],i[3]].append([i[4],i[5]])
    Total_Jeju[i[0],i[1],i[2],i[3]].append([i[5]/i[4]])
p_list= []
s_list = []
t_list =[]
for k,i in Jeju_Tdict.items():
    Jeju_t = []
    Jeju_d = []
    t_list.append(k[2])
    s_list.append(k[3])
    for j in i:

        Jeju_t.append(int(j[0]))
        Jeju_d.append(int(j[1]))

    p = str(round(sum(Jeju_d)/sum(Jeju_t) * 100,0))+"%"
    p_list.append(p)

t_list100 = pd.Series(t_list[:100],name="소상공인")
p_list100 = pd.Series(p_list[:100],name="재난지원금 사용금액 / 총 사용금액")
s_list100 = pd.Series(s_list[:100],name="업종")
data = pd.concat((s_list100,t_list100, p_list100),axis=1)

for i,v in Total_Jeju.items():
    s = list(chain(*v))
    Total_Jeju[i] = (sum(s)/len(s)) * (5/10)

Jeju_NoS = pd.concat((Jeju1["NumofSpent"] , Jeju2["NumofSpent"] , Jeju3["NumofSpent"] , Jeju4["NumofSpent"]))
Jeju_NoDs = pd.concat((Jeju1["NumofDisSpent"] , Jeju2["NumofDisSpent"] , Jeju3["NumofDisSpent"] , Jeju4["NumofDisSpent"]))

Jeju_data = pd.concat((Jeju_P, Jeju_Class, Jeju_Type,Jeju_NoS,Jeju_NoDs),axis=1)
Jeju_data = Jeju_data.reset_index(drop=True)
Total_Jeju1 = defaultdict(list)
Jeju_Tdict = defaultdict(list)
for i in Jeju_data.values:
    Jeju_Tdict[i[0],i[1],i[2],i[3]].append([i[4],i[5]])
    Total_Jeju1[i[0],i[1],i[2],i[3]].append([i[5]/i[4]])
pn_list= []
s_list = []
t_list =[]
for k,i in Jeju_Tdict.items():
    Jeju_t = []
    Jeju_d = []
    t_list.append(k[2])
    s_list.append(k[3])
    for j in i:

        Jeju_t.append(int(j[0]))
        Jeju_d.append(int(j[1]))

    p = str(round(sum(Jeju_d)/sum(Jeju_t) * 100,0))+"%"
    pn_list.append(p)

t_list100 = pd.Series(t_list[:100],name="소상공인")
pn_list100 = pd.Series(pn_list[:100],name="재난지원금 사용횟수 / 총 사용횟수")
s_list100 = pd.Series(s_list[:100],name="업종")
data = pd.concat((s_list100,t_list100, pn_list100),axis=1)

for i, v in Total_Jeju1.items():
    s = list(chain(*v))
    Total_Jeju1[i] = (sum(s)/len(s)) * (5/10)

Jeju_Type = pd.concat((Jeju1["Type"] , Jeju2["Type"] , Jeju3["Type"] , Jeju4["Type"]))
Jeju_Class = pd.concat((Jeju1["FranClass"] , Jeju2["FranClass"] , Jeju3["FranClass"] , Jeju4["FranClass"]))

Dspent = defaultdict(list)
YM = defaultdict(list)
Time =defaultdict(list)

Jeju_P = pd.concat((Jeju1.loc[:,"POINT_X":"POINT_Y"] , Jeju2.loc[:,"POINT_X":"POINT_Y"] ,
                    Jeju3.loc[:,"POINT_X":"POINT_Y"] , Jeju4.loc[:,"POINT_X":"POINT_Y"]))

Jeju_YM = pd.concat((Jeju1["YM"],Jeju2["YM"],Jeju3["YM"],Jeju4["YM"]))
Jeju_Time = pd.concat((Jeju1["Time"],Jeju2["Time"],Jeju3["Time"],Jeju4["Time"]))
Jeju_data = pd.concat((Jeju_P, Jeju_Class,Jeju_Type,Jeju_Tspent, Jeju_Dspent,Jeju_YM,Jeju_Time),axis=1)
Jeju_data = Jeju_data.reset_index(drop=True)

for i in Jeju_data.values:
    Dspent[i[0],i[1],i[2],i[3]].append(i[5])
    YM[i[0],i[1],i[2],i[3]].append(i[6])
    Time[i[0],i[1],i[2],i[3]].append(i[7])
dspent = {}
for i,v in tqdm(Dspent.items()):
    s = sum(v)
    dspent[i] = s
ym=defaultdict(list)
for i,v in tqdm(YM.items()):
    s = list(set(v))
    for j in s:
        if j == 202005:
            a = "5월"
            ym[i].append(a)
        elif j == 202006:
            a = "6월"
            ym[i].append(a)
        elif j == 202007:
            a = "7월"
            ym[i].append(a)
        elif j == 202008:
            a = "8월"
            ym[i].append(a)
    ym[i] = sorted(ym[i])


from collections import Counter
time = {}
for i,v in tqdm(Time.items()):
    s = Counter(v)
    s = s.most_common(2)
    a =[j[0] for j in s]
    time[i] = a

Jeju_6 = defaultdict(list)
Jeju_8 = defaultdict(list)

for i in Jeju_data.values:
    if i[6] == 202005:
        d = int(i[5])/int(i[4])
        Jeju_6[i[0],i[1],i[2],i[3]].append(d)

    if i[6] == 202008:
        d = int(i[5])/int(i[4])
        Jeju_8[i[0],i[1],i[2],i[3]].append(d)
for k,i in Jeju_6.items():
    Jeju_6[k]=sum(i)/len(i)
for k,i in Jeju_8.items():
    Jeju_8[k]=sum(i)/len(i)
Jeju_c = {}
Jeju_none = []
Total_Jeju2 = defaultdict(list)

Total_Jeju3 = {}
for i,v in Total_Jeju.items():
    for i1, v1 in Total_Jeju1.items():
        if i == i1:
            a=(v+v1)*100
            Total_Jeju3[i] = '%.1d' % a

'''
등급
1등급 : 50~100
2등급 : 20~50
3등급 : 10~20
4등급 : 0~10
5등급 : 0
'''

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="https://www.google.co.kr/maps/@37.053745,125.6553969,5z?hl=ko")

'''
부분
'''
from string import Template


for i in tqdm(Type_list):
    m = folium.Map(location=[33.379894, 126.545211],
                   tiles="OpenStreetMap",
                   zoom_start=11)
    for k, v in Total_Jeju3.items():
        idspent = []
        idym = []
        idtime = []
        if k[3] == i:
            for index1, value1 in dspent.items():
                if k == index1:
                    idspent.append(value1)
            for index1, value1 in ym.items():
                if k == index1:
                    idym.append(value1)
            for index1, value1 in time.items():
                if k == index1:
                    idtime.append(value1)
            idspent = str(idspent)
            idspent = idspent.strip("[")
            idspent = idspent.strip("]")
            idym = str(idym)
            idym = idym.strip("[")
            idym = idym.strip("]")
            idym = idym.strip("'")
            idtime = str(idtime)
            idtime = idtime.strip("[")
            idtime = idtime.strip("]")
            idtime = idtime.strip("'")


            n1, n2 = U_W(k[1], k[0])
            html = """
                <h1>$code1<br>
                $code0</h1><br>
                주소 : $code2<br>
                우편번호 : $code3<br>
                재난지원금 선별대상 : $code4<br>
                총 재난지원금 사용금액 : $code5<br>
                금액 사용한 달 : $code6<br>
                주요 사용시간 : $code7

                """
            location = geolocator.reverse("{}, {}".format(n1,n2))
            la = location.address
            c3 = la.split(',')[-2]
            ad1 = la.split(',')[-1]
            ad2 = la.split(',')[:-2]
            ad2.reverse()
            ad2 = (',').join(ad2)
            ad2 = ad2.replace(',','')
            ad = ad1 + ad2

            if int(v) == 0:
                level = "5등급"
                colors = "green"
                s = Template(html).safe_substitute(code1="{}".format(i), code2="{}".format(ad),
                                                   code0="({})".format(k[2]),
                                                   code3="{}".format(c3), code4="{}".format(level),
                                                   code5=idspent + "원", code6=idym, code7=idtime)
                iframe = folium.IFrame(html=s, width=500, height=300)
                popup = folium.Popup(iframe, max_width=2650)
                folium.CircleMarker(location=[n1, n2], radius=10, popup=popup, fill=True, color=colors,
                                    fillcolor=colors).add_to(m)

            elif 0 < int(v) <= 10:
                level = "4등급"
                colors = "blue"
                s = Template(html).safe_substitute(code1="{}".format(i), code2="{}".format(ad),
                                                   code0="({})".format(k[2]),
                                                   code3="{}".format(c3), code4="{}".format(level),
                                                   code5=idspent + "원", code6=idym, code7=idtime)
                iframe = folium.IFrame(html=s, width=500, height=300)
                popup = folium.Popup(iframe, max_width=2650)
                folium.CircleMarker(location=[n1, n2], radius=10, popup=popup, fill=True, color=colors,
                                    fillcolor=colors).add_to(m)

            elif 10 < int(v) <= 20:
                level = "3등급"
                colors = "beige"
                s = Template(html).safe_substitute(code1="{}".format(i), code2="{}".format(ad),
                                                   code0="({})".format(k[2]),
                                                   code3="{}".format(c3), code4="{}".format(level),
                                                   code5=idspent + "원", code6=idym, code7=idtime)
                iframe = folium.IFrame(html=s, width=500, height=300)
                popup = folium.Popup(iframe, max_width=2650)
                folium.CircleMarker(location=[n1, n2], radius=10, popup=popup, fill=True, color=colors,
                                    fillcolor=colors).add_to(m)

            elif 20 < int(v) <= 50:
                level = "2등급"
                colors = "yellow"
                s = Template(html).safe_substitute(code1="{}".format(i), code2="{}".format(ad),
                                                   code0="({})".format(k[2]),
                                                   code3="{}".format(c3), code4="{}".format(level),
                                                   code5=idspent + "원", code6=idym, code7=idtime)
                iframe = folium.IFrame(html=s, width=500, height=300)
                popup = folium.Popup(iframe, max_width=2650)
                folium.CircleMarker(location=[n1, n2], radius=10, popup=popup, fill=True, color=colors,
                                    fillcolor=colors).add_to(m)

            elif 50 < int(v) <= 100:
                level = "1등급"
                colors = "red"
                s = Template(html).safe_substitute(code1="{}".format(i), code2="{}".format(ad),
                                                   code0="({})".format(k[2]),
                                                   code3="{}".format(c3), code4="{}".format(level),
                                                   code5=idspent + "원", code6=idym, code7=idtime)
                iframe = folium.IFrame(html=s, width=500, height=300)
                popup = folium.Popup(iframe, max_width=2650)
                folium.CircleMarker(location=[n1, n2], radius=10, popup=popup, fill=True, color=colors,
                                    fillcolor=colors).add_to(m)







    m = title(m, i)
    m.save('../MAP/{}.html'.format(i))
'''
전체
'''
m = folium.Map(location=[33.379894, 126.545211],
                   tiles="OpenStreetMap",
                   zoom_start=11)
for k, v in tqdm(Total_Jeju3.items()):
    idspent = []
    idym = []
    idtime = []
    for index1, value1 in dspent.items():
        if k == index1:
            idspent.append(value1)
    for index1, value1 in ym.items():
        if k == index1:
            idym.append(value1)
    for index1, value1 in time.items():
        if k == index1:
            idtime.append(value1)
    idspent = str(idspent)
    idspent = idspent.strip("[")
    idspent = idspent.strip("]")
    idym = str(idym)
    idym = idym.strip("[")
    idym = idym.strip("]")
    idym = idym.strip("'")
    idtime = str(idtime)
    idtime = idtime.strip("[")
    idtime = idtime.strip("]")
    idtime = idtime.strip("'")

    n1, n2 = U_W(k[1], k[0])
    html = """
        <h1>$code1<br>
        $code0</h1><br>
        주소 : $code2<br>
        우편번호 : $code3<br>
        재난지원금 선별대상 : $code4<br>
        총 재난지원금 사용금액 : $code5<br>
        금액 사용한 달 : $code6<br>
        주요 사용시간 : $code7

        """
    location = geolocator.reverse("{}, {}".format(n1, n2))
    la = location.address
    c3 = la.split(',')[-2]
    ad1 = la.split(',')[-1]
    ad2 = la.split(',')[:-2]
    ad2.reverse()
    ad2 = (',').join(ad2)
    ad2 = ad2.replace(',', '')
    ad = ad1 + ad2
    global levels
    global colors2
    if int(v) == 0:
        levels = "5등급"

    elif 0 < int(v) <= 10:
        levels = "4등급"

    elif 10 < int(v) <= 20:
        levels = "3등급"

    elif 20 < int(v) <= 50:
        levels = "2등급"

    elif 50 < int(v) <= 100:
        levels = "1등급"

    if levels == " 1등급":
        colors2 = "red"
    elif levels == "2등급":
        colors2 = "yellow"
    elif levels == "3등급":
        colors2 = "beige"
    elif levels == "4등급":
        colors2 = "blue"
    elif levels == "5등급":
        colors2 = "green"

    s = Template(html).safe_substitute(code1="{}".format(k[3]), code2="{}".format(ad), code0="({})".format(k[2]),
                                       code3="{}".format(c3), code4="{}".format(levels),
                                       code5=idspent + "원", code6=idym, code7=idtime)
    iframe = folium.IFrame(html=s, width=500, height=300)
    popup = folium.Popup(iframe, max_width=2650)
    folium.CircleMarker(location=[n1, n2], radius=10, popup=popup, fill=True, color=colors2,
                        fillcolor=colors2).add_to(m)
m.save('../MAP/Total.html')
