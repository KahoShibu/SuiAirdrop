from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import urllib.request
from selenium.common.exceptions import NoSuchElementException

# 钱包扩展包路径
EXTENSION_PATH = os.path.abspath(r"..") + '/sui_wallet.crx'
# 扩展ID
EXTENSION_ID = 'opcgpfmipidbgpenhmajoajpbobppdil'

def lauchWebdriver(driverPath):
    """
    调起谷歌浏览器并加载 SUI 钱包
    """
    print('钱包路径：', EXTENSION_PATH)
    chrome_options = Options()
    chrome_options.add_extension(EXTENSION_PATH)
    global driver # 设置全局浏览器，处处可用
    driver = webdriver.Chrome(options=chrome_options, executable_path=driverPath)
    print("钱包已被加载")
    return driver

def checkHandles():
    """
    递归调用句柄，当句柄超过1时，将多余句柄关闭，只剩下第一个句柄
    """
    handles_value = driver.window_handles
    if len(handles_value) > 1:
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        checkHandles()

def suiSetup(recoverPhrase, password):
    """
    设置 SUI 钱包，通过助记词恢复钱包
    """
    driver.switch_to.window(driver.window_handles[0]) # 切换到第一个句柄
    driver.find_element_by_xpath()

def changeSuiNetwork(networkName):
    """
    更改钱包网络
    """

def connectToWebsite():
    """
    当前网站连接到 SUI 钱包
    """

def confirmApproveFromSuiWallet():
    """
    钱包允许操作
    """

def rejectApproveFromSuiWallet():
    """
    钱包拒绝操作
    """

def confirmTransactionFromSuiWallet():
    """
    钱包确认交易操作
    """

def rejectTrasactionFromSuiWallet():
    """
    钱包拒绝交易操作
    """

def signConfirm():
    """
    钱包签名操作
    """

def signReject():
    """
    钱包拒绝签名操作
    """
