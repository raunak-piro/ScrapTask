from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
email=input('Enter Your Linkdin Email')
password = input("Enter Your Password")
webdriver =webdriver.Chrome()
#Open Carrer Guid
webdriver.get("https://www.careerguide.com/career-options")
time.sleep(7)
#Scrap the Requirement
tex = webdriver.find_element_by_xpath("""/html/body/form/div[6]/div[3]/div/div[2]/div/div[4]/div[3]/ul/li[12]/a""").text
print(tex)


#Open Linkdin
webdriver.get("https://www.linkedin.com/home")
time.sleep(8)
#Login
webdriver.find_element_by_name("session_key").send_keys(email)
webdriver.find_element_by_name("session_password").send_keys(password)
webdriver.find_element_by_xpath("""/html/body/main/section[1]/div/div/form/button""").click()
webdriver.find_element_by_xpath("""/html/body/div[5]/header/div/div/div/div[1]/input""").send_keys(tex)
webdriver.find_element_by_xpath("""/html/body/div[5]/header/div/div/div/div[1]/input""").send_keys(Keys.ENTER)
time.sleep(8)
webdriver.find_element_by_xpath("""/html/body/div[5]/div[3]/div[2]/section/div/nav/div/div/div/button""").click()
time.sleep(5)
webdriver.find_element_by_xpath("""/html/body/div[3]/div/div/div[2]/ul/li[9]/fieldset/div/ul/li[13]/label/p/span[1]""").click()
time.sleep(5)
webdriver.find_element_by_xpath("""/html/body/div[3]/div/div/div[2]/ul/li[9]/fieldset/div/ul/li[2]/label/p/span[1]""").click()

webdriver.find_element_by_xpath("""/html/body/div[3]/div/div/div[3]/div/button[2]/span""").click()
time.sleep(5)
name=webdriver.find_elements_by_class_name("""job-card-container__primary-description """)
loc = webdriver.find_elements_by_class_name("""job-card-container__metadata-item""")
des = webdriver.find_elements_by_class_name("""break-words white-space-pre-wrap mb5 text-body-small t-black--light""")

li=[]
ui=[]
for i in name:
    li.append(i.text)
for j in loc:
    ui.append(j.text)
print(len(li))
for res in range (len(li)):
    print("Company Name = ",li[res],'\n',"Location = ",ui[res])
