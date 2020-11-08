# rclone_systemd_service_creator
a python script to create a script for every remote in the rclone config file
to use this just put your rclone file path into the variable "config" and the script will create all the service files into the running directory
after this just copy the file to the systemd folder and enable all this services
TODO: make a secundary script to copy ,create all the necessary folders and enable services
TODO: create a TUI to insert the config file location
