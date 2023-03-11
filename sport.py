# _*_ coding: utf-8 _*_
"""
Spyder 编辑器

这是一个临时脚本文件。
"""


from selenium import webdriver
import datetime
import time  #打开chrome浏览器
from PIL import Image
import ddddocr

import datetime

# import Image
# 记录时间
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
print(now)

    

# 打开chrome 

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)


# def time_Descri():
    

def login():
    # 打开淘宝首页，通过扫码登录
    # a1=input("请输入你的学号：")
    # a2=input("请输入身份证后八位：")
    # a3=input("请输入你的交大邮箱：")

    
    browser.get("https://sports.sjtu.edu.cn/pc/#/")
    time.sleep(5)
    browser.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div[2]/button[1]").click()
    # url_root="https://jaccount.sjtu.edu.cn/jaccount/"
    a1='nikusting'
    a2='991211abc'
    
    # # a3=browser.find_element_by_id('captcha-img').get_attribute("src")
    
    # # print("1")
    # # print(a3)
    # # browser.get(a3)
    
    browser.get_screenshot_as_file('C:/CrawlResult/screenshot.png')

    #获取指定元素位置
    browser.maximize_window()
    time.sleep(1)
    element = browser.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[2]/div[2]/form/div[3]/div/img')
    # left = int(element.location['x'])
    # print(left)
    # top = int(element.location['y'])
    # print(top)
    # right = int(element.location['x'] + element.size['width'])
    # print(right)
    # bottom = int(element.location['y'] + element.size['height'])
    # print(bottom)

    #通过Image处理图像
    im = Image.open('C:/CrawlResult/screenshot.png')
    im = im.crop((1055, 435, 1230, 480))
    im.save('C:/CrawlResult/code.png')
    
    ocr=ddddocr.DdddOcr('C:/CrawlResult/code.png')
    with open('C:/CrawlResult/code.png','rb') as f:
        img_bytes=f.read()
   
    res=ocr.classification(img_bytes)
    
    print(res)
    a3=res

    
    browser.get_screenshot_as_file('D:/CrawlResult/screenshot.png')
    print("2")

    #获取指定元素位置
    
    im = Image.open('D:/CrawlResult/screenshot.png')
    # im = im.crop((left, top, right, bottom))
    im.save('D://CrawlResult/code.png')
    
    # # print("输出a3")
    

    time.sleep(5)
    js="var q=document.documentElement.scrollTop=1000"  
    jd="var q=document.documentElement.scrollTop=200"  
    time.sleep(5)
    # # browser.execute_script(js)
    browser.find_element_by_id('user').send_keys(a1)
    browser.find_element_by_id('pass').send_keys(a2)
    browser.find_element_by_id('captcha').send_keys(a3)
    browser.find_element_by_id('submit-button').click()
    time.sleep(5)
    browser.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/ul/li[3]/div/input').send_keys('羽毛球')
    # browser.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/ul/li[3]/div/input').send_keys('羽毛球')
    browser.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/ul/li[3]/div/div/button').click()
    time.sleep(2)
    
   # time.sleep(2)
    
    
    # 羽毛球场地
    n_time=str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    for i in range(500):
        # print(a)
            
            #显示星期几
        # b= '星期:' + str(datetime.datetime.now().isoweekday())
        # print(b)
            
            # 判断当前时间是否在范围时间内
        a = datetime.datetime.strptime(str(datetime.datetime.now().date())+'11:59:59', '%Y-%m-%d%H:%M:%S')
        print(a)
        b = datetime.datetime.strptime(str(datetime.datetime.now().date())+'23:59:00', '%Y-%m-%d%H:%M:%S')     
            # 获取当前时间
        print(b)
        n_time=datetime.datetime.now()
        print(n_time)
        print(n_time)
        
        if n_time > a and n_time<b:
            #午餐下单时间到了！
            # a=time.time
            # print(a)
            time.sleep(0.9)
            print(datetime.datetime.now())
            
            
            print("进入时间")
            print(datetime.datetime.now())
            browser.find_element_by_xpath('/html/body/div/div[2]/div/div[5]/div[2]/ul/li[1]/div/div/div[1]/img').click()
            #browser.find_element_by_xpath('/html/body/div/div[2]/div/div[5]/div[2]/ul/li/div/div/div[1]').click()
            time.sleep(0.1)
            print(datetime.datetime.now())
            browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div/div[9]').click()
            time.sleep(0.5)
            browser.execute_script(js)
            print(datetime.datetime.now())
                
            for i in range(5,20):
                # s=i+1
                # l=str(s)
                m=str(i)

                n='/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/div[15]/div['+m+']/div/div/img'
                #d='/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/div[14]/div['+m+']/div/div'
                # d='/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/div[15]/div['+l+']/div/div'
                print(n)

                time.sleep(0.2)
                print("选择时间")
                print(datetime.datetime.now())
                time.sleep(0.5)
                browser.find_element_by_xpath(n).click()
                # browser.find_element_by_xpath(d).click()
                print("下单时间")
                print(datetime.datetime.now())
                time.sleep(0.2)
                browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[3]/button').click()
                print("提交时间")
                print(datetime.datetime.now())
                time.sleep(0.2)
                #print(datetime.datetime.now())
                try:
                    #browser.execute_script(js)
                    time.sleep(0.3)
                                                   
                    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div[1]/label/span[1]/span').click()
                    
                
                    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div[2]/button[2]').click()
                    time.sleep(1)
                    browser.execute_script(js)
                    time.sleep(1)
                    browser.find_element_by_xpath('/html/body/div/div[2]/div[5]/div[2]/button').click()
                    time.sleep(1)
                    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[6]/div/div[3]/span/button[2]/span').click()
                    
                except:
                    print('被 zzh 抢了')
                    print(datetime.datetime.now())
            break
        time.sleep(0.1)
        
    # 台球    
    # for i in range(100):
    #     # print(a)
            
    #         #显示星期几
    #     # b= '星期:' + str(datetime.datetime.now().isoweekday())
    #     # print(b)
            
    #         # 判断当前时间是否在范围时间内
    #     a = datetime.datetime.strptime(str(datetime.datetime.now().date())+'11:00:00', '%Y-%m-%d%H:%M:%S')
    #     print(a)
    #     b = datetime.datetime.strptime(str(datetime.datetime.now().date())+'12:00:01', '%Y-%m-%d%H:%M:%S')     
    #         # 获取当前时间
    #     print(b)
    #     n_time=datetime.datetime.now()
    #     print(n_time)
        
    #     if n_time > a and n_time<b:
    #         #午餐下单时间到了！
    #         # a=time.time
    #         # print(a)
            
    #         browser.find_element_by_xpath('/html/body/div/div[2]/div/div[5]/div[2]/ul/li/div/div/div[1]/img').click()
    #         browser.execute_script(js)
    #         time.sleep(1)
    #         browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div/div[8]').click()
    #         # time.sleep(1)
    #         browser.execute_script(js)
                
    #         for i in range(1,20):
    #             m=str(i)
    #             n='/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/div[15]/div['+m+']/div/div'
    #             print(n)
    #             browser.execute_script(js)
    #             time.sleep(2)
    #             c='/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/div[9]/div[1]/div/div'
    #             browser.find_element_by_xpath(n).click()
    #             browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[3]/button').click()
    #             try:
    #                 browser.execute_script(jd)
    #                 time.sleep(0.5)
    #                 a=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div[1]/label/span[1]/span')
    #                 a.click()
    #                 browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div[2]/button[2]').click()
    #             except:
    #                 print('被 zzh 抢了')
                
                    
    #         break
    #     time.sleep(0.1)
        

    # # time.sleep(10)
    # # js="var q=document.documentElement.scro"
    # # time.sleep(1)
    # try:
    #     a=browser.find_element_by_xpath("/html/body/div/div/a")
    #     a.click()
    #     time.sleep(1)
    # except:
    #     print("输入有误")
    # browser.execute_script(js)
    # time.sleep(2)
    # b=browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div[2]/div/div[3]/div[24]/div[1]")
    # b.click()
    
    # browser.execute_script(js)
    # time.sleep(1)
    # b=browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div[2]/div/div[3]/div[24]/div[2]/div[1]/div/div/div[2]/div[1]/div")
    # b.click()
    
    # time.sleep(2)
    # b=browser.find_element_by_xpath("//input[@autocomplete='off']").text()
    # print(b)
    # browser.maximize_window()
    
    # time.sleep(2)
    # b=browser.execute_script(js)
    # b=browser.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div[2]/button[1]")
    # b.click()
    # # time.sleep(3)
    # time.sleep(5)
    # b=browser.find_element_by_xpath("//*[@id='logoin']/div[1]/div/div[2]/button[1]")
    # wait = ui.WebDriverWait(browser,10)
    # wait.until(lambda driver: driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/ul/li[3]/div/input")).send_keys("羽毛球")
    
    # b=browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[2]/div/div/div[1]/ul/li[5]/a/img').click()
    
    # time.sleep(1)         s
    # b=browser.find_element_by_xpath("/html/body/div/div/a")
    # b.click()
    # time.sleep(1)
    # b=browser.find_element_by_xpath("/html/body/div/div/a")
    # b.click()
    # time.sleep(1)
    # for i in range(1000):
    
    #     try:
    #         b1=browser.find_element_by_xpath("/html/body/div/div/form/div[1]/div/div[1]/label/input")
    #     except:
    #         b1=0
            
    #     try:
    #         b2=browser.find_element_by_xpath("/html/body/div/div/form/div[1]/div/div[2]/label/input")
    #     except:
    #         b2=0
        
    #     try: 
    #         b3=browser.find_element_by_xpath("/html/body/div/div/form/div[1]/div/div[3]/label/input")
    #     except:
    #         b3=0
            
    #     try:    
    #         b4=browser.find_element_by_xpath("/html/body/div/div/form/div[1]/div/div[4]/label/input")
    #     except:
    #         b4=0
            
    #     try:
    #         b5=browser.find_element_by_xpath("/html/body/div/div/form/div[1]/div/div[5]/label/input")
    #     except:
    #         b5=0
            
    #     if b5 :
    #         b3.click()
    #         c1=browser.find_element_by_xpath('/html/body/div/div/form/div[2]/div/button')
    #         c1.click()
    #         time.sleep(1)
    #     elif b4 or b3 or b2 or b1:
    #         b2.click()
    #         c1=browser.find_element_by_xpath('/html/body/div/div/form/div[2]/div/button')
    #         c1.click()
    #         time.sleep(1)
    #     else:
    #         browser.find_element_by_id('a1').send_keys('5')
    #         browser.find_element_by_id('a2').send_keys('4')
    #         browser.find_element_by_id('a3').send_keys('7')
    #         browser.find_element_by_id('a4').send_keys('3')
    #         c1=browser.find_element_by_xpath('/html/body/div[2]/form/div[4]/div[3]/div/button')
    #         c1.click()
    #         time.sleep(1)
    #         browser.find_element_by_id('a5').send_keys('5')
    #         browser.find_element_by_id('a6').send_keys('4')
    #         browser.find_element_by_id('a7').send_keys('7')
    #         browser.find_element_by_id('a8').send_keys('3')
    #         c1=browser.find_element_by_xpath('/html/body/div[2]/form/div[4]/div[2]/div/button')
    #         c1.click()
    #         time.sleep(1)
            
login()
# print('job start at:',time.ctime())
# login()
# print('job done at:',time.ctime())
# time.sleep(200)
    
             
        

       
        
            
            
    

    

    
    

