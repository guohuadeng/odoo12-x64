title init db GreenOdoo12 x64 fast - www.sunpop.cn
cd runtime\pgsql\bin
rd /s/q ..\data
initdb.exe -D ..\data -E UTF8
pg_ctl -D ..\data -l logfile start
rem 创建用户，密码，都是odoo。请输入odoo
createuser --createdb --no-createrole --no-superuser --pwprompt odoo
cd ..\..\..