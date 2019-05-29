Green Odoo 12 x64， http://www.Sunpop.cn
---------------------------------------
## 概述
64位版本性能会比32位高很多，包括高效指令及大内存更快巡址。对高资源消耗的odoo，使用64位是十分有必要的。
本版本在使用64位的基础上，对postgresql进行了优化，并使用nginx进行反向代理，实现了longpolling，可以使用odoo的桌面消息通知，也不会经常报错了。
在windows上搭建了一个完整的高性能 Odoo 环境。
因速度原因，不再支持一键更新至最新版，请手工高速下载 https://nightly.odoocdn.com/12.0/nightly/src/odoo_12.0.latest.zip

## 版本信息
1. python 3.6.7 ,64位，与ubuntu18同步
2. postgresql 9.6.4 ,64位
3. Nginx 1.15.5， 64位
4. Odoo 12社区版，20190301版本
5. 增加 sphinx 及 tx_client，用于文档及翻译

## 全新功能，更快速度
Odoo 12 Features, enhance and boost from 11。 新特性，功能更多，性能更好 - 广州尚鹏 | odoo专业实施开发
http://www.sunpop.cn/odoo-12-features-enhance-boost-from-11/

## 开发
使用pycharm搭建odoo 12, 11,10 开发调试环境
http://www.sunpop.cn/odoo_12_11_10_dev_with_pycharm_setup/

## odoo12 在线演示学习，请注册
http://demo.odooapp.cn

## 操作说明
- 启动odoo：执行 r.bat后，访问 http://localhost:8012  或者  http://localhost
- 更新odoo：执行 s.bat 停止odoo运行后，执行 u.bat。如要手工更新至最新odoo，请至官方下载后覆盖 ./source 目录下文件即可
- 系统已有默认数据库 demo，登录用户/密码:  admin/admin
- 重新初始化数据库：执行 init.bat
- 如多版本并存，请自行调整nginx的映射端口
- odoo12下载地址 https://codeload.github.com/odoo/odoo/zip/12.0
- 高速odoo12下载地址 https://nightly.odoocdn.com/12.0/nightly/src/odoo_12.0.latest.zip
- odoo12 deb https://nightly.odoocdn.com/12.0/nightly/deb/odoo_12.0.latest_all.deb
- pycharm配置说明： http://www.sunpop.cn/odoo_12_11_10_dev_with_pycharm_setup/

## 文件夹说明
├─addons_app    app通用源码
├─addons_odoo    odoo源码，用于优先加载后断点调试
├─addons_patch    app通用源码，需要直接修改的放这里，多用于调整bug和翻译
├─data  要人工导入的资料
├─extra  附加包，如 WKHTMLTOPDF
├─odoofile  odoo生成的静态文件资源
├─runtime   运行库，包括pg数据文件
└─source    odoo12源码

## 主要文件说明
odoo.conf   配置
db.bat  单独启动数据库，用在pycharm中，debug启动时先启用数据库，假设odoo12是在 d:\odoo12-x64 目录，如有变化自行更改
ment.bat    将无法在windows处理的企业版模块移出
r.bat   最常用，odoo服务启动（如果当前有进程则先关闭再启动）
s.bat 停止
u.bat 删除当前source目录中的odoo源码，从git上下载最新版本

extra 依赖文件目录，如果要自行安装涉及到的库，其它如果提示dll错误请安装 vcredist_x64.exe

## 问题处理
如果遇到问题，请首先尝试处理Postgresql,进入bin目录执行环境初始化，相关指令如下
```
cd runtime\pgsql\bin
rd /s/q ..\data
initdb.exe -D ..\data -E UTF8
pg_ctl -D ..\data -l logfile start
```
### 创建用户，密码，都是odoo
```
createuser --createdb --no-createrole --no-superuser --pwprompt odoo
```

# 附：如何自行制作绿色安装包
## 先装 python 3.5.2 ，pip3，用64位。与ubuntu 内置一样版本，改python.exe为python3.exe
```
https://www.python.org/downloads/windows/
```
## 安装 win 支持，便于后续增加 python 依赖，也可以不装
.\extra\vc_redist.x64.exe

## 安装pip
```
SET PATH=%CD%\runtime\pgsql\bin;%CD%\runtime\python3;%CD%\runtime\python3\scripts;%CD%\runtime\win32\wkhtmltopdf;%CD%\runtime\win32\nodejs;%CD%\source;%PATH%
python3 .\extra\get-pip.py
```
## 对某些要编译的Python包，在此找
```
http://www.lfd.uci.edu/~gohlke/pythonlibs/
```
## 部份要人工下载安装的odoo依赖，已下载放在 ./extra
## 优化 requirements.txt 可忽略ms库

## python 3.5 ，此版本才可断点
```
pip3 install -r .\source\requirements.txt  -i https://mirrors.aliyun.com/pypi/simple
pip3 install -r .\source\rfix.txt  -i https://mirrors.aliyun.com/pypi/simple
pip3 install .\extra\Pillow-5.0.0-cp35-cp35m-win_amd64.whl
pip3 install .\extra\psycopg2-2.7.4-cp35-cp35m-win_amd64.whl
pip3 install .\extra\pyldap-2.4.45-cp35-cp35m-win_amd64.whl
pip3 install .\extra\reportlab-3.4.0-cp35-cp35m-win_amd64.whl
pip3 install .\extra\Werkzeug-0.14.1-py2.py3-none-any.whl
pip3 install .\extra\pywin32-223-cp35-cp35m-win_amd64.whl
pip3 install .\extra\psycopg2-2.7.4-cp35-cp35m-win_amd64.whl
pip3 install .\extra\wandex-0.4.5-py3-none-any.whl
pip3 install .\extra\imageio-2.3.0-py2.py3-none-any.whl
pip3 install .\extra\moviepy-0.2.3.5-py2.py3-none-any.whl
pip3 install .\extra\psutil-5.5.1-cp35-cp35m-win_amd64.whl
```

## 更新为 python 3.6
```
pip3 install -r .\requirements.txt  -i https://mirrors.aliyun.com/pypi/simple
pip3 install .\extra\Pillow-5.4.1-cp36-cp36m-win_amd64.whl
pip3 install .\extra\psycopg2-2.7.7-cp36-cp36m-win_amd64.whl
pip3 install .\extra\pyldap-2.4.45-cp36-cp36m-win_amd64.whl
pip3 install .\extra\reportlab-3.5.13-cp36-cp36m-win_amd64.whl
pip3 install .\extra\Werkzeug-0.14.1-py2.py3-none-any.whl
pip3 install .\extra\pywin32-224-cp36-cp36m-win_amd64.whl
pip3 install .\extra\wandex-0.4.5-py3-none-any.whl
pip3 install .\extra\imageio-2.5.0-py3-none-any.whl
pip3 install .\extra\moviepy-1.0.0-py2.py3-none-any.whl
pip3 install .\extra\psutil-5.6.1-cp36-cp36m-win_amd64.whl
pip3 install .\extra\lxml-4.2.3-cp36-cp36m-win_amd64.whl
pip3 install .\extra\psutil-5.6.1-cp36-cp36m-win_amd64.whl
```

## Nginx配置相关
```
runtime/nginx/nginx.conf
```
## 安装结束