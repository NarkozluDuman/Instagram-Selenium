from instagramUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class Instagram:
    def __init__(self,username,password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en, en_USA'})
        self.browser = webdriver.Chrome('chromedriver.exe', options=self.browserProfile)
        self.username = username
        self.password = password
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        usernameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)
    def getFollowers(self, max):
        
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(2)
        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followerCount = len(dialog.find_elements_by_css_selector("li"))
        print(f"first count: {followerCount}")
        action = webdriver.ActionChains(self.browser)
        while followerCount < max:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            newCount = len(dialog.find_elements_by_css_selector("li"))
            if followerCount != newCount:
                followerCount = newCount
                print(f"second count: {newCount}")
                time.sleep(1)
            else:
                break
        followers = dialog.find_elements_by_css_selector("li")
        followerList = []
        i = 0
        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            i += 1
            if i == max:
                break
            

            followerList.append(link)
        with open("followers.txt", "w", encoding="UTF-8") as file:
            for item in followerList:
                file.write(item + "\n")
            
    #def followUser(self,username):
        #self.browser.get("https://www.instagram.com/" + username)
        #time.sleep(2)
        #followButon = self.browser.find_element_by_tag_name("button")
        #if followButon.text != "Following":
            #followButon.click()
            #time.sleep(2)
        #else:
            #print("Zaten takiptesiniz")
    #def unFollowUser(self, username):
        #self.browser.get("https://www.instagram.com/" + username)
        #time.sleep(2)
        #followButon = self.browser.find_element_by_tag_name("button")
        #if followButon.text == "Following":
            #followButon.click()
            #time.sleep(2)
            #self.browser.find_element_by_xpath('//button[text()="Unfollow"]').click()
        #else:
            #print("Zaten takipte de??ilsiniz")


 


        

instagram =Instagram(username,password)
instagram.signIn()
#instagram.unFollowUser("kod_evreni")
#instagram.followUser("kod_evreni")
instagram.getFollowers(50)
#list = ['kod_evreni', '']
# for user in list:
    # instagram.followUser(user)
    # time.sleep(2)
