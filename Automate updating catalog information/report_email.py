#!/usr/bin/env python3
import os
import datetime
import reports
import emails

def getDescription(file):
    with open(file) as f:
        lines = f.read().strip().splitlines()
        name_field = f"name: {lines[0]}"
        weight_field = f"weight: {lines[1]}"
    return f"{name_field}<br/>{weight_field}<br/><br/>"

def main():
    descriptions_path = "supplier-data/descriptions/"
    txt_files = [descriptions_path + f for f in os.listdir(descriptions_path) if f.endswith(".txt")]

    report_file = "/tmp/processed.pdf"

    report_body = ""
    for file in txt_files:
        report_body += getDescription(file)

    today = datetime.datetime.today() 
    report_title = f"Processed Update on {today.strftime('%B')} {today.day}, {today.year}"


    reports.generate_report(report_file, report_title, report_body)

    content = {
        "sender": "automation@example.com",
        "receiver": f"{os.environ.get('USER')}@example.com",
        "subject": "Upload Completed - Online Fruit Store",
        "body": "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
        "attachment": report_file,
    }
    message = emails.generate_email(**content)
    emails.send_email(message)


if __name__ == "__main__":
    main()