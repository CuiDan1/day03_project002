"""爱客登录定位信息"""
from selenium.webdriver.common.by import By

app_package = "com.vcooline.aike"
app_activity = '.umanager.LoginActivity'

login_username = By.ID, 'com.vcooline.aike:id/etxt_username'
login_password = By.ID, 'com.vcooline.aike:id/etxt_pwd'
login_btn = By.ID, 'com.vcooline.aike:id/btn_login'