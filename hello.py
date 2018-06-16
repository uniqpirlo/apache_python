#!/bin/python3.6
# coding:utf-8

import subprocess

cmd='ls /home/hzh'

results=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.readlines()

print('Content-Type: text/html;\n\n')
print("<!DOCTYPE html>")
print("<html lang='ja'>")
print("<body>")
print("    <h1>Hello world.</h1>")
print('<table border="1">')
print("<tr><th>File name</th></tr>")
[print("<tr><td>{}</td></tr>".format(line)) for line in results]
print("</table>")
print("</body>")
print("</html>")
