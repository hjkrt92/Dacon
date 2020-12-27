from PyQt5.QtCore import QUrl, QRect
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEngineView, QWebEnginePage
from PyQt5.Qt import QApplication, QUrl, QDesktopServices
from PyQt5.QtGui import QIcon
import PyQt5
import sys
from functools import partial
label = "일반한식", "단란주점", "편의점", "주점", "스넥", "서양음식", "일식회집", "기타음료식품", "노래방", "중국음식", "슈퍼마켓", "유흥주점", "기타숙박업", \
         "기타레져업", "당구장", "농축수산품", "유아원", "골프경기장", "세탁소", "가방", "콘도", "주차장", "문화취미기타", "주유소", "사무서비스", \
         "자동차정비", "특급호텔", "볼링장", "화장품", "기타회원제형태업소", "주류판매점", "제과점", "피부미용실", "약국", "칵테일바", "정육점", "독서실", "스포츠레져용품",\
         "골프용품", "LPG", "종합병원", "사우나", "화원", "의원", "안마스포츠마사지", "골프연습장", "2급호텔", "기타대인서비스", "보습학원", "부동산분양", "화물운송", "애완동물", \
         "동물병원", "대형할인점", "인터넷Mall", "항공사", "헬스크럽", "기타유통업", "레져용품수리", "정장", "레져업소(회원제형태)", "관광여행", "1급호텔", "침구수예점", \
         "사진관", "악세사리", "보관창고업", "기념품점", "미용원", "영화관", "의료용품", "세차장", "인터넷종합Mall", "기타잡화", "성인용품점", "상품권", "종합용역",\
         "기계공구", "조세서비스", "택시", "기타의료기관및기기", "가례서비스", "구내매점", "수영장", "목재석재철물", "건축요업품", "기타업종", "렌트카", "종합레져타운", "유류판매",\
         "농축협직영매장", "기타건축자재", "비료농약사료종자", "농기계", "보일러펌프", "가전제품", "스포츠의류", "페인트", "미곡상", "기타농업관련", "기타가구", "공공요금", "기능학원", \
         "면세점", "기타교육", "위탁급식업", "이용원", "조명기구", "문구용품", "인테리어", "민예공예품", "기타연료", "자동차부품", "기타용역서비스", "기타운송", "연쇄점", "옷감직물",\
         "한의원", "주방용식기", "카인테리어", "기타수리서비스", "농협하나로클럽", "기타건강식","티켓", "기타전기제품", "일반서적", "외국어학원", "건강진단", "냉열기기", "소프트웨어",\
         "내의판매점", "주방용구", "완구점", "유리", "자동차시트타이어", "카페트커텐천막", "기타교통수단", "테니스장", "치과의원", "신발", "기타의류", "컴퓨터", "병원", "가정용품수리",\
         "단체복", "아동의류", "일반가구", "출판인쇄물", "치과병원", "서적출판(회원제형태)", "카메라", "정수기", "CATV", "기타사무용", "학원(회원제형태)", "이륜차판매", "철제가구",\
         "산후조리원", "견인서비스", "수족관", "양품점", "시계", "안경", "인삼제품", "홍삼제품", "한약방", "중장비수리", "캐쥬얼의류", "과학기자재", "윤활유전문판매", "부동산중개임대",\
         "여객선", "통신기기", "귀금속", "건강식품(회원제형태)", "사무기기", "신변잡화수리", "미용재료", "예체능학원", "기타보험", "사무통신기기수리", "법률회계서비스", "맞춤복점",\
         "전문서적", "화방표구점", "손해보험", "악기점", "기타자동차서비스", "정기간행물", "기타비영리유통", "화랑", "컴퓨터학원", "중고자동차", "제화점", "대학등록금", "기타서적문구",\
         "학습지교육", "수입자동차", "기타직물", "DVD음반테이프판매", "기타광학품", "제약회사", "초중고교육기관", "사무서비스(회원제형태)", "골동품점", "정보서비스"
label= sorted(label)

class display_Web(QWebEngineView):
    def load(self,url):
        self.setUrl(QUrl.fromLocalFile(url))

class Main2(QWebEngineView):
    def __init__(self,url):
        super().__init__()
        self.url = QUrl.fromLocalFile("D:/GAT/Jeju/MAP/{}.html".format(url))
        self.load(self.url)

class Main(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def window2(self,url):
        self.w = Main2(url)
        self.w.show()

    def initUI(self):
        self.setWindowTitle("제주도 재난지원금 선별대상")
        self.setWindowIcon(QIcon('icon.png'))
        self.top = 150
        self.left = 500
        self.width = 1600
        self.height = 800
        self.setGeometry(self.left, self.top, self.width, self.height)

        formLayout = QFormLayout()
        groupBox = QGroupBox("        업종")
        labelLis = []
        comboList = []
        for i,v in enumerate(label):
            button = QPushButton("{}".format(v))
            button.clicked.connect(partial(self.window2,"{}".format(v)))
            comboList.append(button)
            formLayout.addRow(comboList[i])
        groupBox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(780)
        layout = QVBoxLayout()
        layout.addWidget(scroll)

        web = display_Web()
        web.load("D:/GAT/Jeju/MAP/Total.html")
        lay = QHBoxLayout(self)
        lay.addWidget(web,8)
        lay.addLayout(layout,1)


app = QApplication(sys.argv)
main = Main()
main.show()
app.exec_()