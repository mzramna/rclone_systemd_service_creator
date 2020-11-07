#!/usr/bin/env python
import os, subprocess, re

# config_file = os.environ['RCLONE_CONFIG_FILE']
config = "./rclone.conf"
# print(rc.RClone(config_path="./rclone.conf",binary_path="rclone.exe").about())
cmd = ["rclone.exe", "listremotes", "--config=" + config, "--long"]
output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
output = re.compile("b\'(.*)\'").findall(str(output))[0].split("\\n")[0:-1]
for i in range(0, len(output)):
    print(output[i])
    output[i] = output[i].split(":")
    output[i][1] = output[i][1].replace(" ", "")
print(output)
template = open("./default_template_service.service").read()
print(template)
for i in output:
    service = open("./"+i[0] + ".service", "a")
    service.write(template.replace("{{remote_name}}", i[0]).replace("{{config_dir}}", config))
