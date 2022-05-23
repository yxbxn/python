# 이미지 클릭 함수
import time
import pyautogui
import pyperclip
import cv2

def imgClick(filename,t):
    '''
    이미지 파일 클릭 후 대기하는 함수
    '''
    
    imgfile = pyautogui.locateOnScreen(filename, confidence=0.9)
    center = pyautogui.center(imgfile)
    pyautogui.moveTo(center)
    time.sleep(0.5)
    pyautogui.click(center)
    time.sleep(t)

def scroll(line):
    '''
    스크롤 하는 함수
    아래로 스크롤 -
    위로 스크롤 +
    '''
    time.sleep(0.5)
    pyautogui.scroll(line)
    time.sleep(0.5)

def get_news(start_date,end_date):
    
    news_dict = {"동아일보":"donga.png",
                 "조선일보":"chosun.png",
                "중앙일보":"joongang.png"}

    time.sleep(1)

    imgClick("news_lst.png", 0.2)

    #2. 스크롤을 내려서 검색 버튼 클릭
    for key in news_dict.values():
        while True:
            try:
                imgClick(key,1)
                break
            except:
                scroll(-300)

    imgClick("seperate.png", 0.2)
    imgClick("politics.png", 0.2)    


    #1. 신문사 선택 이전에 기간 설정
    imgClick("date.png", 0.5)

    # 시작일 설정
    imgClick("start_date.png", 0.2)
    pyautogui.hotkey("ctrl","a")
    pyautogui.press("delete")
    pyperclip.copy(start_date)
    pyautogui.hotkey("ctrl","v")


    # 종료일 설정
    imgClick("end_date.png", 0.2)
    pyautogui.hotkey("ctrl","a")
    pyautogui.press("delete")
    pyperclip.copy(end_date)
    pyautogui.hotkey("ctrl","v")

    #2. 스크롤을 내려서 적용 버튼 클릭
    while True:
        try:
            imgClick("search_btn.png",5)
            break
        except:
            scroll(-300)

    #3. 검색 후 스크롤 내려서 스탭3 탭을 클릭
    while True:
        try:
            imgClick("step3.png", 3)
            break
        except:
            scroll(-300)

    #4. 엑셀 다운로드 버튼
    while True:
        try:
            imgClick("excel.png", 3)
            break
        except:
            scroll(-400)

    #5. 다운로드 창 닫고 브라우저 초기화
    while True:
        try:
            scroll(100)
            imgClick("x.png",0.1)
            break
        except:
            time.sleep(1)
    time.sleep(15)

    #6. 다시 돌아가기
    while True:
        try:
            scroll(100)
            imgClick("home_btn.png",0.2)
            break
        except:
            time.sleep(1)

    time.sleep(5)
    print("Success")

def get_opp_news(start_date,end_date):
    
    opp_news_dict = {"경향신문":"kyunghyang.png",
             "한겨례":"han.png"}
    
    time.sleep(1)

    imgClick("news_lst.png", 0.2)

    #2. 스크롤을 내려서 검색 버튼 클릭
    for key in opp_news_dict.values():
        while True:
            try:
                imgClick(key,1)
                break
            except:
                scroll(-300)

    imgClick("seperate.png", 0.2)
    imgClick("politics.png", 0.2)    


    #1. 신문사 선택 이전에 기간 설정
    imgClick("date.png", 0.5)

    # 시작일 설정
    imgClick("start_date.png", 0.2)
    pyautogui.hotkey("ctrl","a")
    pyautogui.press("delete")
    pyperclip.copy(start_date)
    pyautogui.hotkey("ctrl","v")


    # 종료일 설정
    imgClick("end_date.png", 0.2)
    pyautogui.hotkey("ctrl","a")
    pyautogui.press("delete")
    pyperclip.copy(end_date)
    pyautogui.hotkey("ctrl","v")

    #2. 스크롤을 내려서 적용 버튼 클릭
    while True:
        try:
            imgClick("search_btn.png",5)
            break
        except:
            scroll(-300)

    #3. 검색 후 스크롤 내려서 스탭3 탭을 클릭
    while True:
        try:
            imgClick("step3.png", 3)
            break
        except:
            scroll(-300)

    #4. 엑셀 다운로드 버튼
    while True:
        try:
            imgClick("excel.png", 3)
            break
        except:
            scroll(-400)

    #5. 다운로드 창 닫고 브라우저 초기화
    while True:
        try:
            scroll(100)
            imgClick("x.png",0.1)
            time.sleep(15)
            break
        except:
            time.sleep(1)
    

    #6. 다시 돌아가기
    while True:
        try:
            scroll(100)
            imgClick("home_btn.png",0.2)
            break
        except:
            time.sleep(1)

    time.sleep(5)
    print("Success")