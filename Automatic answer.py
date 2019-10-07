from selenium import webdriver
import json, time
url = 'https://zhidao.baidu.com/list?cid=110'
driver = webdriver.Chrome()
driver.get(url)

a = input('\n\n\n\n\n\n****\n\n\n\n\nsign in and input anything like ‘ok’ \n\n\n\n****\n\n\n\n')
a = input('sign in and input anything like ‘ok’ ')
kkk = 0

while(1):
    all_handles = driver.window_handles
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    kkk=0
    
    title_link = driver.find_elements_by_class_name('title-link')
    for i in title_link:
        try:
            all_handles = driver.window_handles
            for ii, v in enumerate(all_handles):
                    if ii != 0:
                        driver.switch_to.window(v)
                        driver.close()
            kkk = kkk+1
        except:
            pass
        if kkk == 10:
            break
        driver.switch_to.window(driver.window_handles[0])
        href = i.get_attribute('href')
        driver.execute_script('window.open("%s");' % (href))
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        try:
            driver.find_element_by_id('ueditor_0')
            title = driver.find_element_by_class_name('ask-title ').text
            title_url = 'https://zhidao.baidu.com/search?&word=' + title
            js = 'window.open("%s");' % (title_url)
            driver.execute_script(js)
            time.sleep(5)
            driver.switch_to.window(driver.window_handles[2])
            answer_list = driver.find_elements_by_class_name('dt,mb-4,line')
            for k in answer_list:
                href = k.find_element_by_tag_name('a').get_attribute('href')
                driver.execute_script('window.open("%s");' % (href))
                time.sleep(5)
                driver.switch_to.window(driver.window_handles[3])
                try:
                    text = driver.find_element_by_class_name('best-text,mb-10').text
                except:
                    text = ''
                finally:
                    driver.close()
                if text:
                    driver.switch_to.window(driver.window_handles[2])
                    driver.close()
                    driver.switch_to.window(driver.window_handles[1])
                    driver.switch_to.frame('ueditor_0')
                    driver.find_element_by_xpath('/html/body').click()
                    driver.find_element_by_xpath('/html/body').send_keys(text)
                    driver.switch_to.default_content()
                    driver.find_element_by_xpath('//*[@id="answer-editor"]/div[2]/a').click()
                    time.sleep(5)
                    driver.switch_to.window(driver.window_handles[1])
                    driver.close()
                    break

        except Exception as err:
            all_handles = driver.window_handles
            for i, v in enumerate(all_handles):
                if i != 0:
                    driver.switch_to.window(v)
                    driver.close()
            driver.switch_to.window(driver.window_handles[0])
            print(err)


