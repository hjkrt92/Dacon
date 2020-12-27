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
import matplotlib.image as mpimg
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

'''데이터 시각화를 통해 사람들이 
재난지원금 어디에 많이 사용하는지 업소를 선별하는 목적으로
분석하였습니다.
'''
#데이터 불러오기
Jeju1 = r"C:\Users\Administrator\Desktop\data (1)\KRI-DAC_Jeju_data5.txt"
Jeju2 = r"C:\Users\Administrator\Desktop\data (1)\KRI-DAC_Jeju_data6.txt"
Jeju3 = r"C:\Users\Administrator\Desktop\data (1)\KRI-DAC_Jeju_data7.txt"
Jeju4 = r"C:\Users\Administrator\Desktop\data (1)\KRI-DAC_Jeju_data8.txt"
Jeju1 = pd.read_csv(Jeju1, sep=",")
Jeju2 = pd.read_csv(Jeju2, sep=",")
Jeju3 = pd.read_csv(Jeju3, sep=",")
Jeju4 = pd.read_csv(Jeju4, sep=",")

'''
선별대상을 판단하기 전에 업종의 특성을 조사하였습니다.

같은 좌표 업소가 2개 이상일 수 없다고 여겨 

하나라는 가정으로 조사했습니다.
 '''
Jeju_P = pd.concat((Jeju1.loc[:,"POINT_X":"POINT_Y"] , Jeju2.loc[:,"POINT_X":"POINT_Y"] ,
                    Jeju3.loc[:,"POINT_X":"POINT_Y"] , Jeju4.loc[:,"POINT_X":"POINT_Y"]))
Jeju_Type = pd.concat((Jeju1["Type"] , Jeju2["Type"] , Jeju3["Type"] , Jeju4["Type"]))
Jeju_Class = pd.concat((Jeju1["FranClass"] , Jeju2["FranClass"] , Jeju3["FranClass"] , Jeju4["FranClass"]))
Jeju_data = pd.concat((Jeju_P, Jeju_Class, Jeju_Type),axis=1)
Jeju_data = Jeju_data.reset_index(drop=True)
'''
영세 총 25132
중소 총 4333
중소1 총 3630
중소2 총 2190
일반 총 5353
'''
Jeju_Tdict = {}
for i in Jeju_data.values:
    Jeju_Tdict[i[0],i[1],i[2],i[3]]=i[2]
print(Counter(Jeju_Tdict.values()))
Jeju_Cdict = defaultdict(list)
for i in Jeju_Tdict.keys():

    Jeju_Cdict[i[3]].append(i[2])
Type_list = set([i for i in Jeju_Cdict.keys()])

# print(XKCD_COLORS)
'''
각 업종의 소상공인을 계층모형으로 구분하여 균형한지 불균형한지를 분석하였습니다.

역피라미드(/형) : 불균형

피라미드(\형) :불균형

물결형(~형) : 비교적 균형

독점형(-형) : 균형

수평형(--형) : 균형

다이아몬드(/\형)  : 비교적 균형

양극화(\/) : 불균형

이외에도 다양한 모형이 있으나 위와 같은 모형들이 섞여 있는 것으로 판단했습니다.
'''
# for index, (i,v) in enumerate(tqdm(Jeju_Cdict.items())):
#     C = Counter(v)
#     ci_list, cv_list = [], []
#     for Ci, Cv in C.items():
#         ci_list.append(Ci)
#         cv_list.append(Cv)
#     ci, cv = align(ci_list,cv_list)
#     plt.figure(figsize=(3, 3))
#     plt.rc('font', family='Malgun Gothic')
#     plt.rc('axes', unicode_minus=False)
#     plt.title("{}".format(i))
#     plt.bar(ci, cv,color='#8af1fe')
#     plt.plot(ci, cv, color = '#69d84f')
#     plt.savefig("../Images/{}.png".format(i))
#     plt.close()
########################################
# #수평형 예시
# read_imgs = "D:/GAT/Jeju/Images/건강진단.png"
# plt.imshow(mpimg.imread(read_imgs))
#
# #양극화 예시
# read_imgs = "D:/GAT/Jeju/Images/골프경기장.png"
# plt.imshow(mpimg.imread(read_imgs))


########################################
# # 사진합치기
# read_imgs = "../Images/*.png"
# read_imgs = glob(read_imgs)
# print(len(read_imgs))
# img_list = defaultdict(list)
# pic_list = []
# Ax = 0
# for index, img in enumerate(tqdm(read_imgs)):
#     xA = (index // 10)
#     if xA == Ax and index != 205:
#         img = plt.imread(img)
#         img_list[xA].append(img)
#
#     elif xA > Ax:
#         fig = np.concatenate(img_list[xA-1], axis=1)
#         pic_list.append(fig)
#         img = plt.imread(img)
#         img_list[xA].append(img)
#         Ax = xA
#
#     elif index == 205:
#         img = plt.imread(img)
#         img_list[xA].append(img)
#         A = np.zeros((300,1200,4))
#         img_list[xA].append(A)
#         fig = np.concatenate(img_list[xA], axis=1)
#         pic_list.append(fig)
#
# pic=np.concatenate(pic_list,axis=0)
# plt.imsave("../images/picture.png", pic)
##########################################################
'''
재난지원금이 많이 사용되었던 곳이 어디었는지 알기 위해
재난지원금 사용금액/ 총 사용금액으로 조사했습니다.
'''

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

    p = round(sum(Jeju_d)/sum(Jeju_t)*100,0)
    p_list.append(p)

t_list100 = pd.Series(t_list[:100],name="소상공인")
p_list100 = pd.Series(p_list[:100],name="재난지원금 사용금액 / 총 사용금액")
s_list100 = pd.Series(s_list[:100],name="업종")
data = pd.concat((s_list100,t_list100, p_list100),axis=1)

for i,v in Total_Jeju.items():
    s = list(chain(*v))
    Total_Jeju[i] = (sum(s)/len(s)) * (5/10)

'''
100여개의 재난지원금 / 총 사용금액 비율
'''

plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False)
g = sns.catplot(x="업종", y="재난지원금 사용금액 / 총 사용금액", hue="소상공인", data=data)
g.fig.set_figheight(20)
g.fig.set_figwidth(20)
g.savefig("../Graphs/total_dis_spent.jpg")
plt.show()
plt.close()


'''
재난지원금이 자주 쓰였던 곳이 어디었는지 알기 위해
재난지원금 사용횟수/ 총 사용횟수으로 재난지원금 횟수가 높은 업소를 찾아보았습니다.
'''
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

    p = round(sum(Jeju_d)/sum(Jeju_t)*100,0 )
    pn_list.append(p)

t_list100 = pd.Series(t_list[:100],name="소상공인")
pn_list100 = pd.Series(pn_list[:100],name="재난지원금 사용횟수 / 총 사용횟수")
s_list100 = pd.Series(s_list[:100],name="업종")
data = pd.concat((s_list100,t_list100, pn_list100),axis=1)

for i, v in Total_Jeju1.items():
    s = list(chain(*v))
    Total_Jeju1[i] = (sum(s)/len(s)) * (5/10)
'''
100여개의 재난지원금 횟수 / 총 사용횟수 비율
'''
plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False)
g = sns.catplot(x="업종", y="재난지원금 사용횟수 / 총 사용횟수", hue="소상공인", data=data)
g.fig.set_figheight(20)
g.fig.set_figwidth(20)
g.savefig("../Graphs/total_dis_num.jpg")
plt.show()
plt.close()



'''
소상공인에 따른 재난지원금 사용금액의 평균을 조사하여
소상공인에 따라 재난지원금이 비례한지 확인해보았습니다.
'''
colors5 = ['#580f41','#8fff9f','#dbb40c','#a2cffe','#c0fb2d']
Jeju_data = pd.concat((Jeju_Class, Jeju_Type,Jeju_Dspent),axis=1)
Search_spent1 = defaultdict(list)
for i in Jeju_data.values:
    Search_spent1[i[0]].append(i[2])

y1 = sum(Search_spent1["영세"]) / 25132
y2 = sum(Search_spent1["중소"]) / 4333
y3 = sum(Search_spent1["중소1"]) / 3630
y4 = sum(Search_spent1["중소2"]) /2190
y5 = sum(Search_spent1["일반"]) /5353
Search_data1 = {
     "소상공인":["영세", "중소", "중소1", "중소2","일반"],
     "재난지원금 사용금액" : [y1,y2,y3,y4,y5]
}
labels = "영세", "중소", "중소1", "중소2","일반"
sizes = [y1,y2,y3,y4,y5]
fig1, ax1 = plt.subplots()
plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False)
ax1.pie(sizes,  labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90,colors=colors5)
ax1.axis('equal')
plt.savefig("../Graphs/Class_percent.jpg")
plt.show()
plt.close()
'''
기존 소상공인 ( 영세 :3억, 중소 5억, 중소1 10억, 중소2 30억, 일반 30억 초과)
시각화로 확인 후 대체로 비례하나 중소와 중소1이 재난지원금 비율이 높은 것으로 확인됩니다.
이는 중소와 중소1이 평균적으로 재난지원금에 대한 영향이 가장 민감한 것으로 예상됩니다.
'''
'''
업종에 따른 재난지원금 사용금액의 비율을 조사해보았습니다.
'''
Jeju_data = pd.concat((Jeju_Class, Jeju_Type,Jeju_Dspent),axis=1)
Search_i = defaultdict(list)
si= defaultdict(list)
sv =defaultdict(list)
for i in Jeju_data.values:
    Search_i[i[1]].append(i[2])

for i,v in Search_i.items():
    si["업종"].append(i)
    sv["재난지원금 사용금액"].append(sum(v))

a1 = list(chain(*si.values()))
a2 = list(chain(*sv.values()))
labels, sizes = get_five(a2,a1)
fig1, ax1 = plt.subplots()
plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False)
ax1.pie(sizes,  labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90,colors = colors5)
ax1.axis('equal')
plt.savefig("../Graphs/type_percent.jpg")
plt.show()
plt.close()

'''
TOP4가 먹는 것과 관련이 있어 주로 먹는 데에 재난지원금이 소비가 많았음 알 수 있습니다.
'''
'''
1.시간에 따른 월 별 재난지원금 사용금액
2.시간에 따른 월 별 총 사용금액
3.시간에 따른 월 별 재난지원금 사용횟수
4.시간에 따른 월 별 총 사용횟수
재난지원금 사용금액 부분에서 큰 차이를 발견하였는데
5월에서 8월로 갈수록 금액의 양이 줄어드는 것을 확인할 수 있었습니다.
즉, 재난지원금을 빠르게 소비하였습니다.

재난지원금 사용금액과 재난지원금 이용 횟수는 줄어든 반면, 총 사용금액과 횟수는 늘어난 것을 보면
개별적으로는 다르겠지만 재난지원금이 총 사용금액을 전체적으로는 보완해주는 것을 알 수 있었습니다.
재난지원금을 월마다 균등하게 사용할 수 있도록 방법을 고려하는 것이 필요할 수 있다고 여겨집니다.
'''
Jeju_Type = pd.concat((Jeju1["Type"] , Jeju2["Type"] , Jeju3["Type"] , Jeju4["Type"]))
Jeju_Class = pd.concat((Jeju1["FranClass"] , Jeju2["FranClass"] , Jeju3["FranClass"] , Jeju4["FranClass"]))
Jeju_5 = pd.concat((Jeju1["YM"],Jeju1["Time"],Jeju1["Type"],Jeju1["FranClass"],Jeju1["DisSpent"],Jeju1["NumofSpent"],Jeju1["TotalSpent"],Jeju1["NumofDisSpent"] ),axis=1)
Jeju_6 = pd.concat((Jeju2["YM"],Jeju2["Time"],Jeju2["Type"],Jeju2["FranClass"],Jeju2["DisSpent"],Jeju2["NumofSpent"],Jeju2["TotalSpent"],Jeju2["NumofDisSpent"] ),axis=1)
Jeju_7 = pd.concat((Jeju3["YM"],Jeju3["Time"],Jeju3["Type"],Jeju3["FranClass"],Jeju3["DisSpent"],Jeju3["NumofSpent"],Jeju3["TotalSpent"],Jeju3["NumofDisSpent"] ),axis=1)
Jeju_8 = pd.concat((Jeju4["YM"],Jeju4["Time"],Jeju4["Type"],Jeju4["FranClass"],Jeju4["DisSpent"],Jeju4["NumofSpent"],Jeju4["TotalSpent"],Jeju4["NumofDisSpent"] ),axis=1)
Jeju_data = pd.concat((Jeju_5,Jeju_6,Jeju_7,Jeju_8))

plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False)
fig, axs = plt.subplots(2, 2,figsize=(20,20))

sns.lineplot(data=Jeju_data, x="Time", y="DisSpent", hue="YM",ax=axs[0, 0])
axs[0,0].set_title("재난지원금 사용금액")
sns.lineplot(data=Jeju_data, x="Time", y="TotalSpent", hue="YM",ax=axs[0, 1])
axs[0,1].set_title("총 사용금액")
sns.lineplot(data=Jeju_data, x="Time", y="NumofDisSpent", hue="YM",ax=axs[1, 0])
axs[1,0].set_title("재난지원금 사용횟수")
sns.lineplot(data=Jeju_data, x="Time", y="NumofSpent", hue="YM",ax=axs[1, 1])
axs[1,1].set_title("총 사용횟수")
plt.savefig("../Graphs/total_percent.jpg")
plt.show()
plt.close()


'''
x시 사용조사
'''
x5 = defaultdict(list)
x6 = defaultdict(list)
x7 = defaultdict(list)
x8 = defaultdict(list)
x5t=[]
x6t=[]
x7t=[]
x8t=[]
for i in Jeju_data.values:
    if i[1] == "x시":

        if i[0] == 202005:
            x5[i[2]].append(i[6])
            x5t.append(i[6])
        elif i[0] == 202006:
            x6[i[2]].append(i[6])
            x6t.append(i[6])
        elif i[0] == 202007:
            x7[i[2]].append(i[6])
            x7t.append(i[6])
        elif i[0] == 202008:
            x8[i[2]].append(i[6])
            x8t.append(i[6])
print("5월",sum(x5t),len(x5))
print("6월",sum(x6t),len(x6))
print("7월",sum(x7t),len(x7))
print("8월",sum(x8t),len(x8))
X5= {}
X6= {}
X7= {}
X8= {}
for i,v in x5.items():
    X5[i] = sum(v)
for i,v in x6.items():
    X6[i] = sum(v)
for i,v in x7.items():
    X7[i] = sum(v)
for i,v in x8.items():
    X8[i] = sum(v)
x5lavel = []
x5data= []
x6lavel = []
x6data= []
x7lavel = []
x7data= []
x8lavel = []
x8data= []
for i,v in X5.items():
    x5lavel.append(i)
    x5data.append(v)
for i,v in X6.items():
    x6lavel.append(i)
    x6data.append(v)
for i,v in X7.items():
    x7lavel.append(i)
    x7data.append(v)
for i,v in X8.items():
    x8lavel.append(i)
    x8data.append(v)
x5l,x5d = get_five(x5data,x5lavel)
x6l,x6d = get_five(x6data,x6lavel)
x7l,x7d = get_five(x7data,x7lavel)
x8l,x8d = get_five(x8data,x8lavel)
plt.rcParams["font.size"] = "10"

plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False)
fig, axs = plt.subplots(2, 2,figsize=(20,20))

axs[0,0].bar(x5l,x5d,color = '#98eff9')
axs[0,0].set_title("5월 x시")
axs[0,1].bar(x6l,x6d,color = '#516572')
axs[0,1].set_title("6월 x시")
axs[1,0].bar(x5l,x5d,color = '#029386')
axs[1,0].set_title("7월 x시")
axs[1,1].bar(x6l,x6d,color = '#13eac9')
axs[1,1].set_title("8월 x시")
plt.show()
plt.close()


colors20 = ['#a2bffe','#10a674','#06b48b','#af884a','#0b8b87','#ffa756','#a2a415','#154406','#856798','#34013f','#632de9','#0a888a',
            '#6f7632','#d46a7e','#1e488f','#bc13fe','#7ef4cc','#76cd26','#74a662','#80013f']
Jeju_P = pd.concat((Jeju1.loc[:,"POINT_X":"POINT_Y"] , Jeju2.loc[:,"POINT_X":"POINT_Y"] ,
                    Jeju3.loc[:,"POINT_X":"POINT_Y"] , Jeju4.loc[:,"POINT_X":"POINT_Y"]))

Jeju_YM = pd.concat((Jeju1["YM"],Jeju2["YM"],Jeju3["YM"],Jeju4["YM"]))
Jeju_data = pd.concat((Jeju_P, Jeju_Class,Jeju_Type,Jeju_Tspent, Jeju_Dspent,Jeju_YM),axis=1)
Jeju_data = Jeju_data.reset_index(drop=True)
Jeju_6 = defaultdict(list)
Jeju_8 = defaultdict(list)

'''
8월 23일부터 전국적으로 코로나 2단계였기에 그 영향과 그 동안의 악화로 인해
5월대비 8월 재난지원금/사용금액이 증가한 곳을 조사했습니다.
20개를 시각화하였는데 복합적인 원인으로 보이나 일부는 코로나로 인해 소비가 줄어들으면서 먼저 피해를 본 곳으로 예상해 볼 수 있었습니다.
피부미용실이 가장 높고 맞춤복점 제약회사 순이었습니다.
'''
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

for k,i in Jeju_6.items():
    for k1,i1 in Jeju_8.items():
        if k == k1:
            if i !=0:
                d = round(i1/i * 100,0)
                Jeju_c[k] =d

            else:
                Jeju_none.append(k)
Jeju_a = defaultdict(list)
for i,v in Jeju_c.items():
    if v != 0.0:
        Jeju_a[i].append(v)
Jeju_k = defaultdict(list)
for i,v in Jeju_a.items():
    Jeju_k[i[3]].append(v)
Jeju_kc = {}

for i, v in Jeju_k.items():
    s = list(chain(*v))
    Jeju_kc[i] = sum(s) / len(s)
del Jeju_kc["내의판매점"]
labels= [i for i in Jeju_kc.keys()]
ratio = [i for i in Jeju_kc.values()]
labels,ratio = get_twenty(ratio, labels)
plt.figure(figsize=(10,10))
plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False)
plt.pie(ratio, labels=labels, autopct='%.1f%%',colors = colors20)
plt.savefig("../Graphs/8_5.jpg")
plt.show()
plt.close()

'''
조사한 시각화 토대로 여러방법이 있겠지만 사람들이 주로 재난지원금을 쓰는 업소를 정하는 기준을
재난지원금 사용금액/총 사용금액과 재난지원금 사용횟수 / 총 사용횟수 5대5로 합산하여 선정하였습니다.
다음은 해당기준으로 상위 20개 업소를 시각화하였습니다.
'''
Total_Jeju3 = {}
for i,v in Total_Jeju.items():
    for i1, v1 in Total_Jeju1.items():
        if i == i1:
            a=(v+v1)*100
            Total_Jeju3[i] = '%.1d' % a

Total_Jeju3s = [str(i[2])+"_"+str(i[3])+"\n"+"("+str(i[0])+str(i[1])+")" for i in Total_Jeju3.keys()]
names = Total_Jeju3s
data =  list(Total_Jeju3.values())
names,data = get_twenty(data,names)
names.reverse()
data.reverse()
plt.rcParams["font.size"] = "6"
plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False)
fig, ax = plt.subplots(figsize=(20,20))
ax.barh(names, data)
plt.savefig("../Graphs/top20.jpg")
plt.show()
plt.close()

'''
위 내용을 토대로 시각화한 gui를 만들었습니다.
'''

