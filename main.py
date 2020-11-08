#!/usr/bin/env python
import re
import subprocess
import glob
import shutil, os
import shlex


def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
    rc = process.poll()
    return rc


def list_rclone_services(config="./rclone.conf"):
    cmd = "rclone listremotes --config=" + config + "--long"
    output = run_command(cmd)
    output = re.compile("b\'(.*)\'").findall(str(output))[0].split("\\n")[0:-1]
    for i in range(0, len(output)):
        print(output[i])
        output[i] = output[i].split(":")
        output[i][1] = output[i][1].replace(" ", "")
    return output


def create_service_files(config="./rclone.conf", rclone_mount_folder="/media/rclone/"):
    output = list_rclone_services(config)
    # print(output)
    template = open("./default_template_service.service").read()
    # print(template)
    for i in output:
        service = open("./rclone_" + i[0] + ".service", "a")
        service.write(
            template.replace("{{remote_name}}", i[0]).replace("{{config_dir}}", config).replace("{{rclone_folder}}",
                                                                                                rclone_mount_folder))


def install_services(rclone_mount_folder="/media/rclone/", config="./rclone.conf",
                     systemd_folder="/etc/systemd/system/"):
    os.mkdir(rclone_mount_folder)
    for i in glob.glob("*.service"):
        shutil.move(i, systemd_folder + i)
        # print(systemd_folder + i)
        os.mkdir(rclone_mount_folder + i.replace(".service", "").replace("rclone_", ""))
        # print(rclone_mount_folder+i.replace(".service","").replace("rclone_",""))


def start_webdav_server(config="./rclone.conf", rclone_mount_folder="/media/rclone/"):
    cmd = "rclone serve webdav {0} --config={1}".format(rclone_mount_folder, config)
    retorno = run_command(cmd)
    return retorno


# config_file = os.environ['RCLONE_CONFIG_FILE']

create_service_files()
install_services()
# start_webdav_server()
