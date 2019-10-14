title GreenOdoo12 x64 fast - www.sunpop.cn
%CD%\runtime\bin\pv.exe -f -k python.exe -q
%CD%\runtime\bin\pv.exe -f -k python3.exe -q
%CD%\runtime\pgsql\bin\pg_ctl stop -D %CD%\zdata\pg -s -m fast
%CD%\runtime\bin\pv.exe -f -k postgres.exe -q
tskill postgres
tskill python
tskill python3
tskill nginx
ping -n 3 127.0.0.1>nul
SET PATH=%CD%\runtime\pgsql\bin;%CD%\runtime\python3;%CD%\runtime\python3\scripts;%CD%\runtime\win32\wkhtmltopdf;%CD%\runtime\win32\nodejs;%CD%\source;%PATH%
ping -n 1 127.0.0.1>nul
cd runtime\nginx &START nginx.exe &cd.. &cd..
ping -n 1 127.0.0.1>nul
%CD%\runtime\pgsql\bin\pg_ctl -D %CD%\zdata\pg -l %CD%\runtime\pgsql\logfile start
ping -n 1 127.0.0.1>nul
%CD%\runtime\python3\python3 %CD%\source\odoo-bin -c %CD%\odoo.conf --update=""
