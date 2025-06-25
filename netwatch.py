import argparse
import platform
import psutil
import socket
import os
import datetime



def get_all_ips():
    ip_list = []
    for interface, snics in psutil.net_if_addrs().items():
        for snic in snics:
            if snic.family == socket.AF_INET and not snic.address.startswith("127."):
                ip_list.append((interface, snic.address))
    return ip_list

def get_uptime():
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    now = datetime.datetime.now()
    uptime = now - boot_time
    return str(uptime).split('.')[0]  # Strip microseconds

def show_all():
    print("System:", platform.system())
    print("Hostname:", platform.node())
    print("IP Addresses:")
        for iface, ip in get_all_ips():
            print(f"  {iface}: {ip}")
    print("CPU Usage:", psutil.cpu_percent(interval=1), "%")
    print("Memory Usage:", psutil.virtual_memory().percent, "%")
    print("Uptime:", get_uptime())

parser = argparse.ArgumentParser(description="NetWatch - CLI System Monitor 🖥️")
parser.add_argument('--all', action='store_true', help='Show all info')
parser.add_argument('--cpu', action='store_true', help='Show CPU usage')
parser.add_argument('--mem', action='store_true', help='Show memory usage')
parser.add_argument('--ip', action='store_true', help='Show IP address')

args = parser.parse_args()

if args.all:
    show_all()
if args.cpu:
    print("CPU Usage:", psutil.cpu_percent(interval=1), "%")
if args.mem:
    print("Memory Usage:", psutil.virtual_memory().percent, "%")
if args.ip:
    print("IP Address:", get_ip())
