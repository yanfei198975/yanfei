# coding=utf-8
import time
import unittest
import  htmltestrunner
from appium.webdriver.common.touch_action import TouchAction


from appium import webdriver

from demo.LogPage import LogPage
from demo.MainPage import MainPage
from demo.My import My
from demo.LoginText import login_success_page
from demo.Longpress import Longpress
from demo.IF import Judge_interface
from demo.Updown import Updown

from demo.Security import Modify
from demo.Oldpassword import Oldpassword
from demo.Newpassword import Newpassword

from demo.SettingPage import Setting_page
from demo.ExitAccount import ExitAccount
from demo.Exit import Exit
from demo.Sure import Sure

from demo.Home import Home
from demo.Head import Head
from demo.For_com_agr import For_com_agr
from demo.Written_Forword import Written_Forword
from demo.Commentback import Commentback

from demo.Written_comment import Written_comment

from demo.Follow import Follow
from demo.Group import  Group

from demo.Anyone import Anyone

from demo.Plus_go_to import Plus_go_to
from demo.Written_words import Written_words
from demo.Send_words import Send

class weiBo(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0.2'
        desired_caps['deviceName'] = 'f246defa'
        desired_caps['appPackage'] = 'com.sina.weibo'
        desired_caps['appActivity'] = 'com.sina.weibo.SplashActivity'
        desired_caps['unicodeKeyboard'] = True   #输入中文识别
        desired_caps['restKeyboard'] = True ##输入中文识别
        # self.camera1 =self.driver.find_elements(by=id,value=u'我的想的')[0].click()##输入中文识别
        remote_url = 'http://127.0.0.1:4723/wd/hub'
        self.driver = webdriver.Remote(remote_url, desired_caps)
        time.sleep(10)
        # self.driver.find_element_by_id('titleSave').click()
        # self.driver.find_element_by_id('etLoginUsername').send_keys('15344550901')
        # self.driver.find_element_by_id('etPwd').send_keys('yanfei1989')
        # self.driver.find_element_by_id('rlLogin').click()


     #登陆
    # def test_login(self):
    #  MainPage(self.driver).click_go_to()
    #  LogPage(self.driver).login_go_to()
    #  time.sleep(5)
    #  My(self.driver).my_go()
    #  self.assertEqual(login_success_page(self.driver).get_text('id', 'tvNick'), u'果果20141214')

    # 发送文字
    # def test_sentword(self):
    #     Plus_go_to(self.driver).plus_go()
    #     Written_words(self.driver).written_go()
    #     Send(self.driver).send()

    # 滑动
    # def test_Updown(self):
    #     Home(self.driver).home_go()
    #     Updown(self.driver).slide()
        # self.home = self.driver.find_element(by='name', value='微博').click()
        # self.driver.swipe(500, 1000, 500, 500, 200)

    # 判断界面出现
    # def test_judge(self):
    #     Judge_interface(self.driver).judge_go()

    #长按
    def test_longpress(self):
        action1 = TouchAction(self.driver)
        el = self.driver.find_element_by_class_name('android.widget.LinearLayout')
        action1.long_press(el,duration=5000).perform()

        # action1 = TouchAction(self.driver)
        # el = self.driver.find_element_by_id('XXXXX1')
        # action1.long_press(el).wait(10000).perform()
        #
        # action2 = TouchAction(self.driver)
        # el = self.driver.find_element_by_id('XXXXX2')
        # action2.moveTo(el).release().perform()


    #修改密码
    # def test_modify(self):
    #    pass
    #  My(self.driver).my_go()
    #     Setting_page(self.driver).set()
    #     ExitAccount(self.driver).security_go()
    #     Modify(self.driver).modify_go()
    #     Oldpassword(self.driver).oldpassword_go()
    #     Newpassword(self.driver).newpassword_go()

    #转发
    # def test_forword(self):
    #     Home(self.driver).home_go()
    #     Head(self.driver).head_go()
    #     time.sleep(5)
    #     For_com_agr(self.driver).forwordpage_go()
    #     # #id 和文字不识别
    #     Written_Forword(self.driver).written_forword_go()
    #     Commentback(self.driver).commentback_go()

    #评论
    # def test_comment(self):
    #    Home(self.driver).home_go()
    #    Head(self.driver).head_go()
    #    time.sleep(5)
    #    For_com_agr(self.driver).comment_go()
    #    Written_comment(self.driver).written_comment_go()
    #    Commentback(self.driver).commentback_go()

    #点赞
    # def test_agreen(self):
    #     Home(self.driver).home_go()
    #     Head(self.driver).head_go()
    #     time.sleep(5)
    #     For_com_agr(self.driver).agreen_go()
    #     Commentback(self.driver).commentback_go()
    #关注
    # def test_follow(self):
    #     Home(self.driver).home_go()
    #     Head(self.driver).head_go()
    #     time.sleep(5)
    #     Follow(self.driver).follow_go()
    #     Group(self.driver).group_go()
    #     Commentback(self.driver).commentback_go()

    #任意点赞
    # def test_anyagreen(self):
    #     Home(self.driver).home_go()
    #     Head(self.driver).head_go()
    #     time.sleep(5)
    #     Updown(self.driver).slide()
    #     Updown(self.driver).slide()
    #     Anyone(self.driver).anyagreen_go()

    #任意评论
    # def test_comment(self):
    #     Home(self.driver).home_go()
    #     Head(self.driver).head_go()
    #     time.sleep(5)
    #     Updown(self.driver).slide()
    #     Updown(self.driver).slide()
    #     Anyone(self.driver).anycomment_go()
    #     Written_comment(self.driver).written_comment_go()
    #     Commentback(self.driver).commentback_go()

    #退出
    # def test_Exit_account(self):
    #     My(self.driver).my_go()
    #     Setting_page(self.driver).set()
    #     ExitAccount(self.driver).account_go()
    #     Exit(self.driver).Exit_account()
    #     Sure(self.driver).sure_go()
         #退出确定按键不成功


    def tearDown(self):
        self.driver.quit()
#
if __name__ == "__main__":
    unittest.main()
    # htmltestrunner.main()

    suite = unittest.TestSuite(unittest.makeSuite(weiBo))

    filename = "D:/Selenium/jiekouceshi/123.html"
    print (filename)
    fp = open(filename, 'wb')
    runner = htmltestrunner.HTMLTestRunner(
    stream=fp,
    title="testresult",
    description="testreport"
    )
    runner.run(suite)
    fp.close()



