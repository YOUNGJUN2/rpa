# -*- coding: utf-8 -*-
import os
import time
import datetime
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
from tzlocal import get_localzone
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException, NoAlertPresentException, UnexpectedAlertPresentException
from selenium.webdriver.common.alert import Alert
from operator import eq
from datetime import datetime
import getpass

#크롬 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument('window-size=1920x1080')
options.add_argument('headless') #크롬창 숨기기
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-setuid-sandbox')
options.add_argument('--incognito')
options.add_argument('disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--log-level=3')
options.add_argument('--ignore-certificate-errors')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36")

#드라이버 위치 경로 입력(크롬 버전에 맞는 드라이버 사용)
driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=options)

wait = WebDriverWait(driver, 2)

# 티켓 오탐 처리 자동화
def False_Positive(options, i, t1, t2, t3):
	FP_Ment = ''  # 처리 사유
	ACG_Ment = ''  # 처리 
	if options == 2:  # 오탐 - 정상통신
		FP='//*[@id="check' + str(i) + '"]'
		driver.find_element_by_xpath(FP).click()
		time.sleep(1)
		FP_Button='/html/body/div[1]/div[1]/table/tbody/tr/td/div[3]/div[1]/div[1]/a[1]'
		driver.find_element_by_xpath(FP_Button).click()
		time.sleep(1)
		FP_Combo='/html/body/div[1]/div[3]/div/div[2]/div/table/tbody/tr[1]/td/select/option[2]'
		driver.find_element_by_xpath(FP_Combo).click()
		time.sleep(1)
		FP_End='/html/body/div[1]/div[3]/div/div[2]/div/table/tbody/tr[2]/td/a'
		driver.find_element_by_xpath(FP_End).click()
		print("False Positive Complete! -> " + str(t1) + " " + str(t2) + " " + str(t3))
		time.sleep(1)
	elif options == 3:  # 오탐 - 테스트
                FP='//*[@id="check' + str(i) + '"]'
                driver.find_element_by_xpath(FP).click()
                time.sleep(1)
                FP_Button='/html/body/div[1]/div[1]/table/tbody/tr/td/div[3]/div[1]/div[1]/a[1]'
                driver.find_element_by_xpath(FP_Button).click()
                time.sleep(1)
                FP_Combo='/html/body/div[1]/div[3]/div/div[2]/div/table/tbody/tr[1]/td/select/option[4]'
                driver.find_element_by_xpath(FP_Combo).click()
                time.sleep(1)
                FP_End='/html/body/div[1]/div[3]/div/div[2]/div/table/tbody/tr[2]/td/a'
                driver.find_element_by_xpath(FP_End).click()
                print("False Positive Complete! -> " + str(t1) + " " + str(t2) + " " + str(t3))
                time.sleep(1)
	elif options == 4:  # 오탐 - 특이사항 없음
                FP='//*[@id="check' + str(i) + '"]'
                driver.find_element_by_xpath(FP).click()
                time.sleep(1)
                FP_Button='/html/body/div[1]/div[1]/table/tbody/tr/td/div[3]/div[1]/div[1]/a[1]' 
                driver.find_element_by_xpath(FP_Button).click()
                time.sleep(1)
                FP_Combo='/html/body/div[1]/div[3]/div/div[2]/div/table/tbody/tr[1]/td/select/option[8]'
                driver.find_element_by_xpath(FP_Combo).click()
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/table/tbody/tr[2]/td/input').send_keys(FP_Ment)
                time.sleep(1)
                FP_End='/html/body/div[1]/div[3]/div/div[2]/div/table/tbody/tr[2]/td/a'
                driver.find_element_by_xpath(FP_End).click()
                print("False Positive Complete! -> " + str(t1) + " " + str(t2) + " " + str(t3))
                time.sleep(1)
	    elif options == 5:  # 오탐 - 정상통신, ACG 확인 멘트 
		FP='//*[@id="check' + str(i) + '"]'
		driver.find_element_by_xpath(FP).click()
		wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[1]/table/tbody/tr/td/div[3]/div[1]/div[1]/a[1]")))
		FP_Button='/html/body/div[1]/div[1]/table/tbody/tr/td/div[3]/div[1]/div[1]/a[1]' #오탐 버튼 클릭
		driver.find_element_by_xpath(FP_Button).click()
		wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div/table/tbody/tr[1]/td/select/option[2]")))
		FP_Combo='/html/body/div[1]/div[3]/div/div[2]/div/table/tbody/tr[1]/td/select/option[2]' # 정상통신
		driver.find_element_by_xpath(FP_Combo).click()
		wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div/table/tbody/tr[2]/td/input")))
		driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/table/tbody/tr[2]/td/input').send_keys(ACG_Ment)
		wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div/table/tbody/tr[2]/td/a")))
		FP_End='/html/body/div[1]/div[3]/div/div[2]/div/table/tbody/tr[2]/td/a' # 적용
		driver.find_element_by_xpath(FP_End).click()
		print("False Positive Complete! -> " + str(t1) + " " + str(t2) + " " + str(t3))
		time.sleep(1)
	    elif options == 6:  # 오탐 - 특이사항 없음, 멘트
		FP='//*[@id="check' + str(i) + '"]'
		driver.find_element_by_xpath(FP).click()
		wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[1]/table/tbody/tr/td/div[3]/div[1]/div[1]/a[1]")))
		FP_Button='/html/body/div[1]/div[1]/table/tbody/tr/td/div[3]/div[1]/div[1]/a[1]'
		driver.find_element_by_xpath(FP_Button).click()
		wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div/table/tbody/tr[1]/td/select/option[8]")))
		FP_Combo='/html/body/div[1]/div[3]/div/div[2]/div/table/tbody/tr[1]/td/select/option[8]'
		driver.find_element_by_xpath(FP_Combo).click()
		driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/table/tbody/tr[2]/td/input').send_keys(FP_Ment)  # 특이사항 없음 멘트
		time.sleep(1)
		wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div/table/tbody/tr[2]/td/a")))
		FP_End='/html/body/div[1]/div[3]/div/div[2]/div/table/tbody/tr[2]/td/a'
		driver.find_element_by_xpath(FP_End).click()
		print("False Positive Complete! -> " + str(t1) + " " + str(t2) + " " + str(t3))
		time.sleep(1)
		
# 자동화 대상 티켓에 대한 조건값
def Procees():
    driver.switch_to.window(driver.window_handles[0])
    try:
        table = driver.find_element_by_xpath("//*[@id='waitingListInfo']/div[1]/table/tbody")   
    except NoSuchElementException:
        print("Ticket Zero!")
    else:
        i = 0
        for tr in table.find_elements_by_tag_name("tr"):
            td = tr.find_elements_by_tag_name("td")
            s = "{}, {}, {}, {}, {}, {}".format(td[2].text, td[3].text, td[4].text, td[5].text, td[6].text, td[7].text)
            #td[2]: 유형, td[3]: 법인명, td[4]: IDC, td[5]: 티켓명, td[6]: 공격지, td[7]: 목적지
            print (s)
            if td[4].text == "IDC" and td[5].text == "EventName" and td[6].text == "Src_ip" and td[7].text == "Dst_ip":
                False_Positive(2, str(i), str(td[4].text), str(td[5].text), str(td[6].text))
                break
            elif td[6].text == "Src_ip" or td[7].text == "Dst_ip":
                False_Positive(3, str(i), str(td[4].text), str(td[5].text), str(td[6].text))
                break
            elif td[4].text == "IDC" and td[5].text == "EventName" and td[6].text == "Src_ip":
                False_Positive(4, str(i), str(td[4].text), str(td[5].text), str(td[6].text)) 
                break
            # ...
	
	    i = i + 1
    except NoSuchElementException:
        print("Ticket Zero!")

# SOC 체크박스 선택 및 새로고침 자동화
def new_check():
    now = datetime.now()
    print()
    print(now)
    driver.switch_to.window(driver.window_handles[0])
    driver.get('')  # SOC 주소
    wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[1]/table/tbody/tr/td/div[2]/form/fieldset/div[2]/fieldset/table/tbody/tr/td[1]/table/tbody/tr[1]/td/input[3]")))
    check_NCP_PM=driver.find_element_by_xpath('/html/body/div[1]/div[1]/table/tbody/tr/td/div[2]/form/fieldset/div[2]/fieldset/table/tbody/tr/td[1]/table/tbody/tr[1]/td/input[4]')
    check_NCP_PM=check_NCP_PM.get_attribute('value')
    if check_NCP_PM == "":
        chk_NCP_PM='/html/body/div[1]/div[1]/table/tbody/tr/td/div[2]/form/fieldset/div[2]/fieldset/table/tbody/tr/td[1]/table/tbody/tr[1]/td/input[3]'
        driver.find_element_by_xpath(chk_NCP_PM).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[1]/table/tbody/tr/td/div[2]/form/fieldset/div[2]/fieldset/table/tbody/tr/td[1]/table/tbody/tr[4]/td/input")))
    chk_Time='/html/body/div[1]/div[1]/table/tbody/tr/td/div[2]/form/fieldset/div[2]/fieldset/table/tbody/tr/td[1]/table/tbody/tr[4]/td/input'
    driver.find_element_by_xpath(chk_Time).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[1]/table/tbody/tr/td/div[2]/form/fieldset/div[2]/fieldset/table/tbody/tr/td[2]/a/strong")))
    chk_Search='/html/body/div[1]/div[1]/table/tbody/tr/td/div[2]/form/fieldset/div[2]/fieldset/table/tbody/tr/td[2]/a/strong'
    driver.find_element_by_xpath(chk_Search).click()
    time.sleep(0.5)
    Procees()

# SOC 접근 계정 인증
def main():
    driver.get('')  # TESS TMS 장비 주소
    user_id = input("ID 입력: ")
    user_id = str(user_id)
    user_pw = getpass.getpass("PW 입력: ")
    user_pw = str(user_pw)
    driver.find_element_by_xpath('/html/body/div/form/div[2]/div/fieldset/div[1]/div[1]/input').send_keys(user_id)
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('/html/body/div/form/div[2]/div/fieldset/div[1]/div[2]/input').send_keys(user_pw)
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('/html/body/div/form/div[2]/div/fieldset/div[2]/a[1]').click()
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/button[2]")))
        driver.find_element_by_xpath('/html/body/div/div[2]/button[2]').click()
    except:
        pass

if __name__ == "__main__":
    main()
    sched = BlockingScheduler()  #스케쥴러 생성
    sched.add_job(new_check, 'interval', seconds=7)  #스케쥴러 옵션 설정
    sched.start()
