#!/usr/bin/env python3
import psutil
import socket
import emails

max_cpu_usage_perc = 80
max_disk_avail_perc = 20
max_mem_avail_mb = 500
chk_local_host_ip = "127.0.0.1"


def check_system_resources():
    """Check system resources and return alert message if any issue is found."""
    cpu_usage_perc = psutil.cpu_percent(interval=3)
    max_disk_usage_perc = 100 - max_disk_avail_perc
    dsk_usage_perc = psutil.disk_usage("/").percent
    one_mb = 2 ** 20
    max_mem_avail = one_mb * max_mem_avail_mb
    mem_avail = psutil.virtual_memory().available
    local_host_ip = socket.gethostbyname("localhost")

    alert = None

    if cpu_usage_perc > max_cpu_usage_perc:
        alert = f"Error - CPU usage is over {max_cpu_usage_perc}%"
    elif dsk_usage_perc > max_disk_usage_perc:
        alert = f"Error - Available disk space is less than {max_disk_avail_perc}%"
    elif mem_avail < max_mem_avail:
        alert = f"Error - Available memory is less than {max_mem_avail_mb}MB"
    elif local_host_ip != chk_local_host_ip:
        alert = f"Error - localhost cannot be resolved to {chk_local_host_ip}"

    return alert


def send_alert(alert):
    """Output alert error and send email."""
    content = {
        "sender": "automation@example.com",
        "receiver": "student@example.com",
        "subject": alert,
        "body": "Please check your system and resolve the issue as soon as possible.",
        "attachment": None,
    }

    try:
        message = emails.generate_email(**content)
        emails.send_email(message)
    except:
        print("Unable to send alert email notification!")
    finally:
        print(alert)
        exit(1)


def main():
    print("Checking system resources")
    alert = check_system_resources()

    if alert:
        send_alert(alert)
    else:
        print("System OK")


if __name__ == "__main__":
    main()
