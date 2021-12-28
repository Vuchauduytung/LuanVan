@echo off
echo HCMUT 211
mkdir "python-software"
curl "https://www.python.org/ftp/python/3.10.1/python-3.10.1-amd64.exe" --output "python-software/setup_python.exe"
start "python-install" "F:\HK211\LuanVan\python-software\setup_python.exe"
echo "Hello"