"""
This script will execute koan -r and the necessary reboot to start the PXE boot
process on a target host.

required params:
  user - user to login as 
  password - login users password
  target - target host to run on

usage:
  python pxe_host.py -u root -p foobar -t 192.168.0.12,192.168.0.13
  
"""
import os
import argparse
import paramiko

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--user", help="user to log in as")
parser.add_argument("-p", "--password", help="user password")
parser.add_argument("-t", "--target", help="comma separated list of target hosts")
args = parser.parse_args()

user = args.user
password = args.password
host_list = args.target.split(',')

for host in host_list:
    print "PXEing host " + host
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(str(host), username=user, password=password)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("yum install -y koan python-ethtool; koan -r; reboot")
