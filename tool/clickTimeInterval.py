#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Created on   : "Thursday June 29 2023 09:32:33 GMT+0800 (China Standard Time)"
# @Author       : zorrow2017
# @File         : clickTimeInterval.py
# @Description  : clickTimeInterval


r"""
clickTimeInterval.py
To do
每隔${lv_sec}秒，自动点一下屏幕${(x,y)}坐标
以防登录超时退出、VPN断开、屏幕息屏
"""


import json
import os
import re
import shutil
import time
# pip install
import pyautogui


def main():
    """
    @description To do
    @dependence  pip install chardet, pip install requests, 
    @param iv_file input file absolute path
    @param ev_file output file absolute path
    """
    print(__doc__)
    print("<begin> time at: "+time.ctime())

############
    # 传入传出参数
    iv_file = ""
    ev_file = ""

    # 配置
    # 准备数据
    lv_count = 0
    lv_maxTime = -1
    ls_dict = {}
    ls_dict["vscode_saveAll"] = (1262, 640)
    ls_dict["win_leftTop"] = (1, 1)

    # 执行
    # 定时点击
    while True:
        # 控制
        lv_count += 1
        if (lv_maxTime >= 0 and lv_count > lv_maxTime):
            break

        # 每隔3秒，或298秒
        lv_sec = 298
        time.sleep(lv_sec)

        # 前进后退按钮的坐标：(284,128)
        # pyautogui.click(x=284,y=128)
        pyautogui.click(x=1262, y=640)

        # <!-- 学习，没用的但常用的且易忘的小知识点： -->
        while False:  # 封装成块
            # 点一点常用的坐标
            lt_position = ls_dict["vscode_saveAll"]
            pyautogui.click(x=lt_position[0], y=lt_position[1])
            break
############

    print("<end> time at: "+time.ctime())


# 主程序入口
if (__name__ == "__main__"):
    main()
    input("ENTER to exit...")
