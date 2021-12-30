@echo off

echo HCMUT 211
mkdir "python-software"
curl "https://www.python.org/ftp/python/3.9.8/python-3.9.8-amd64.exe" --output "setup_python.exe"
start "python-install" "setup_python.exe"