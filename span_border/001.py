'''
Created on 2017年6月28日
跨境：先连接VPN
兼容性：在chrome和firefox上都有问题
IE设置：关闭保护模式（all zones)
@author: wei.wang7
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime

class SpanBorderTest(unittest.TestCase):
    
    def setUp(self):
        self.driver=webdriver.Ie()
    
    def test_xxx(self):
        driver=self.driver
        driver.get("http://10.6.102.40:18610/CBE_Service/")
        assert "欢迎登录跨境交易系统" in driver.page_source
        driver.find_element_by_id("loginname").send_keys("zhy")
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("butLogin").click()
        assert "退出登录" in driver.page_source
        
        driver.find_element_by_xpath(".//*[@id='slider']/ul/li[1]/div").click()
        driver.find_element_by_link_text("用户信息管理").click()
        driver.find_element_by_link_text("用户管理").click()
        
        #http://10.6.102.40:18610/CBE_Service/systemmanage/user/v001.jsp
        #<input id="butQuery" class="button" name="butQuery" value="查 询" type="button">
        
        '''查询操作'''
        #空值查询 ——点击查询按钮
        driver.get("http://10.6.102.40:18610/CBE_Service/systemmanage/user/v001.jsp")
        driver.find_element_by_id("butQuery").click()
        #单值查询——用户名称输入zhouhaiyan，点击查询按钮
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys("zhouhaiyan")
        driver.find_element_by_id("butQuery").click()
        #组合查询——用户名称输入zhouhaiyan，用户状态选择已启用，点击放大镜，选择易生支付有限公司，点击查询按钮
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys("zhouhaiyan")
        driver.find_element_by_xpath(".//*[@id='form1']/div/div[2]/table[1]/tbody/tr[2]/td[3]/table/tbody/tr/td[2]/a").click()
        driver.find_element_by_link_text("易生支付有限公司").click()
        driver.find_element_by_id("butQuery").click()
        
        '''新增用户'''
        #点击新增按钮，
        driver.find_element_by_id("butAdd").click()
        #1. 直接点击保存，提示：用户登录名值不能为空    用户名称值不能为空，点击确定
        driver.find_element_by_id("butSave").click()
        #todo: assert "用户登录名值不能为空" in driver.find_element_by_xpath("html/body/div[3]/div[2]/div[1]")
        driver.find_element_by_xpath("html/body/div[3]/div[2]/div[3]/a/span/span").click()
        #2. 用户登录名输入user2017xxxx，点击保存，提示：用户名称值不能为空，点击确定
        driver.find_element_by_id("loginName").send_keys("user"+datetime.datetime.now().strftime('%Y%m%d'))
        driver.find_element_by_id("butSave").click()
        driver.find_element_by_xpath("html/body/div[3]/div[2]/div[3]/a/span/span").click()
        #3. 用户名称输入user2017xxxx，点击保存，提示：确定保存?点击确定
        driver.find_element_by_id("userName").send_keys("user"+datetime.datetime.now().strftime('%Y%m%d'))
        driver.find_element_by_id("butSave").click()
        '''Modal dialog; Alert Text'''
#         following methods to switch to modelframe
# 
# driver.switchTo().frame("ModelFrameTitle");
# or
# 
# driver.switchTo().activeElement()
        print(driver.page_source)        
        
        '''修改用户'''
        #1. 用户名称输入user2017xxxx，点击查询
        #2. 点击用户编号，进入用户修改界面
        #3. 点击放大镜，选择易生支付有限公司
        #4. 用户有效期结束日输入now+2年
        #5. 登录证书SN输入123，登录证书CN输入123，办公电话输入88888888， 手机号码输入17010000001，EMAIL输入user2017xxxx@hotmail.com
        #6. 点击保存按钮，提示：确定保存?点击确定
        
        '''删除用户'''
        #1. 用户名称输入user2017xxxx，点击查询
        #2. 选中该用户，点击删除。提示：确定删除?点击确定，提示：删除成功!
        
#         driver.find_element_by_link_text("职责信息管理").click()
#         driver.find_element_by_link_text("职责管理").click()
        
        '''职责查询'''
        #空值查询——点击查询按钮
        #有值查询——职责名称输入财务，点击查询。点击职责编号，点击返回退出
        #高级查询——点击高级查询，职责名称输入财务，状态选择已启用，点击查询
        
        '''新增职责'''
        #1. 点击新增按钮
        #2. 职责名称输入role2017xxxx
        #3. 分配菜单全选，选择：报送报表-报送报表-客户月报表、系统管理-用户与岗位关联管理-用户与岗位关联设置；
        #基础设置-基础设置-国家设置、业务处理-购汇业务-指令状态复核；信息查询-信息查询-备付金账户流水查询
        #4. 分配适用机构，选择易生支付
        #5. 点击保存，提示：确定保存?点击确定
        
        '''修改职责'''
        #1. 职责名称输入role2017xxxx，点击查询
        #2. 点击职责编号，在菜单分配权限中添加信息查询-信息查询-订单信息查询，
        #3. 点击保存，提示：确定保存?点击确定
        
#         driver.find_element_by_link_text("用户与岗位关联管理").click()
#         driver.find_element_by_link_text("用户与岗位关联设置").click()
        
        '''关联查询'''
        #空值查询——点击查询按钮
        #有值查询——用户名称输入user2017xxxx，点击查询，点击用户编号
        
        '''职责查询'''
        #空值查询——点击查询按钮
        #有值查询——点击放大镜，机构名称选择易生支付，点击放大镜，职责名称选择role2017xxxx，点击查询
        
        '''关联设置'''
        #选择易生支付（role2017xxxx）岗，点击关联设置，提示：是否关联设置?点击确定，提示：保存设置成功!

        

#         driver.find_element_by_xpath(".//*[@id='slider']/ul/li[3]/div").click()
#         driver.find_element_by_xpath(".//*[@id='SubM3_100_100']").click()
#         driver.find_element_by_xpath(".//*[@id='SubM3_100_100_100']").click()
#         driver.find_element_by_xpath(".//*[@id='SubM3_100_100_150']").click()
        
#         driver.find_element_by_xpath(".//*[@id='slider']/ul/li[2]/div").click()
#         driver.find_element_by_xpath(".//*[@id='slider']/ul/li[3]/div").click()
#         driver.find_element_by_xpath(".//*[@id='slider']/ul/li[4]/div").click()
#         driver.find_element_by_xpath(".//*[@id='slider']/ul/li[5]/div").click()
        
    def tearDown(self):
        self.driver.close()
        
if __name__=="__main__":
    unittest.main()
