﻿#!/usr/bin/env python
# -*- coding: UTF-8 -*-  

'''
{
"版权"] = "LQAB工作室",
"author":{
0:"全体"
}
"初创时间:"2017年3月",
}
'''

# ----------------- 外部模块处理<<开始>>  -----------------

#-----系统必备模块引用 #-----
import sys # 操作系统模块1
import os # 操作系统模块

#-----通用功能模块引用 #-----

#-----特定功能模块引用 #-----
#from service.handler import * #导入web路由
# ----------------- 外部模块处理<<结束>>  -----------------

# ----------------- 内部模块处理<<开始>>  -----------------


# 本地主路径
path_self =""
path_main = os.path.abspath('')
path_main = path_main.replace(path_self,"")

dic_config = {} #定义主变量字典

###config_start###

# ---- 系统标准参数配置 ---
dic_config["ip"] = "127.0.0.1" #---web调试地址
dic_config["web_port"] = "8001" #---web服务端口
dic_config["default_web_file"] = "index.html" #---web默认主页
dic_config["charset_web"] = "utf-8" #---web编码
dic_config["name_soft"] = "LQAB之微服务自然语言基础处理示范模版" #---软件名称
dic_config["type_soft"] = "上线测试服务版 beta1" #---软件版本名 品系
dic_config["vol_soft"] = "1.2" #---软件版本号
dic_config["authority_soft"] = "GPL-3.0" #---软件授权方式
dic_config["author_soft"] = "LQAB工作室" #---软件开发方
dic_config["qq_group"] = "4232051" #---软件支持服务QQ群号
dic_config["tel_lqab"] = "15636176092" #---软件支持手机
dic_config["url_lqab"] = "www.dudu2007.com" #---软件支持网站

# ---- 前台应用参数配置 ---
dic_config["max_per_page"] = "6" #---默认分页数
dic_config["form_default"] = "script" #---表单默认提交
dic_config["numb_find"] = "8" #---最大匹配关键词队列数
dic_config["numb_limit"] = "6" #---匹配候选数

# ---- 主数据库参数配置 ---
dic_config["path_sqlite"] = "\\data\\sqlite\\main_sqlite.db" #---主配置sqlitewen文件地址
dic_config["host_mysql"] = "127.0.0.1" #---mysql数据库地址
dic_config["user_mysql"] = "root" #---mysql管理员名
dic_config["pwd_mysql"] = "r4t5y6u7" #---mysql管理员密码
dic_config["name_mysql_after"] = "c" #---mysql数据库名的后缀代号
dic_config["port_mysql"] = "3306" #---mysql数据库端口号
dic_config["charset_mysql"] = "utf8" #---mysql数据库编码

# ---- 权限管理参数配置 ---
dic_config["power_0"] = ("a0","游客") #---权限认证等级说明
dic_config["power_1"] = ("a","数据分析员") #---权限认证等级说明
dic_config["power_2"] = ("b","数据分析师") #---权限认证等级说明
dic_config["power_3"] = ("c","程序员") #---权限认证等级说明
dic_config["power_4"] = ("d","前台管理员") #---权限认证等级说明
dic_config["power_5"] = ("e","后台管理员") #---权限认证等级说明
dic_config["power_6"] = ("f","商业客户")#---权限认证等级说明
dic_config["power_7"] = ("g","总管理员") #---权限认证等级说明
dic_config["time_alive"] = 3 # 登录过期时间 单位为天 

# ---- 前台应用参数配置 ---
dic_config["max_per_page"] = "10" #---默认分页数
dic_config["form_default"] = "script" #---表单默认提交
dic_config["numb_find"] = "8" #---最大匹配关键词队列数
dic_config["numb_limit"] = "10" #---匹配候选数

# ---- 加密解密参数配置 ---
dic_config["secret_key"] = "8wety^$" #---默认密钥
dic_config["secret_salt"] = b'jdshgfonlsdgperw09vos-%$&' #---默认密钥salt

# ---- 数据分析引擎参数配置 ---
dic_config["fit_rate"] = "0.95" #---默认拟合准确率
dic_config["path_lr"] = "./data/lr/"
dic_config["path_svm"] = "./data/svm/"
dic_config["path_cnn_bilstm"] = "./data/cnn_bilstm/"
dic_config["path_bi"] = "./data/bi/"
dic_config["numb_q_all"] = "1607876" # 问答对文档总数
dic_config["newword_power_is"] = "3" #新词识别的词频阈值
dic_config["numb_nature_segment"] = "3" #自然分词长度阈值

# ---- 工程生产参数 ----
dic_config["path_main"] = "http://lqab.vicp.net/" #---默认主绝对路径
dic_config["path_jieba_dic"] = "./data/dic/user_dic_jieba.txt" #---默认的分词字典
dic_config["path_statics"] = "./statics/" #---默认本地数据分析数据文件夹
dic_config["path_dae"] = "./data/dae/" #---默认本地数据分析数据文件夹
dic_config["path_dic"] = "./data/dic/" #---默认本地数据字典文件夹
dic_config["path_f"] = "./data/f/" #---默认本地数据原力数据文件夹
dic_config["log_if"] = "1" #---是否打开日志功能
dic_config["url_api"] = "http://127.0.0.1:8001/" #---数据分析引擎API地址
dic_config["test_if"] = "2" #---是否打开调试模式 0 否 1 是 2 特殊

# ---- 缓存参数 ----
dic_config["redis_host"] = 'localhost' #---redis地址
dic_config["redis_pass"] = '' #---redis密码
dic_config["redis_port"] = 6379 #---redis端口
dic_config["redis_db"] = 0 #---redis默认数据库编号

###config_end###


# ----------------- 内部模块处理<<结束>>  -----------------

# ------------------ 主过程<<开始>>  -------------------#


def main():

    print("") # 防止代码外泄 只输出一个空字符

if __name__ == '__main__':
    main()
    
# ------------------ 主过程<<结束>>  -------------------#
 