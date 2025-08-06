import argparse
import requests
import os
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from PIL import Image
import numpy as np

# ----------------------------------
# Logo Display with Image to ASCII
# ----------------------------------
def print_logo(path="banner.png"):
    if not os.path.exists(path):
        print("[!] Logo image not found.")
        return

    image = Image.open(path).convert("L")
    image = image.resize((80, 40))

    ascii_chars = "@%#*+=-:. "
    pixels = np.array(image)
    ascii_art = "\n".join("".join(ascii_chars[pixel // 32] for pixel in row) for row in pixels)
    print(ascii_art)

# ----------------------------------
# Payload Loader
# ----------------------------------
def load_payloads(payload_file):
    try:
        with open(payload_file, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"[!] Payload file '{payload_file}' not found.")
        return []

# ----------------------------------
# Form Extractor
# ----------------------------------
def get_all_forms(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

# ----------------------------------
# Attack Launcher
# ----------------------------------
def is_vulnerable(response):
    errors = ["<script>alert(`xss`)</script>", "<script>alert(1)</script>", "alert(1)", "alert(`xss`)"]
    for error in errors:
        if error in response.text:
            return True
    return False

def scan_xss(url, payloads):
    forms = get_all_forms(url)
    print(f"[*] Detected {len(forms)} form(s) on {url}.")
    for i, form in enumerate(forms, start=1):
        form_details = get_form_details(form)
        for payload in payloads:
            data = {}
            for input_tag in form_details["inputs"]:
                if input_tag["type"] == "text" or input_tag["type"] == "search":
                    data[input_tag["name"]] = payload
                elif input_tag["name"]:
                    data[input_tag["name"]] = "test"

            url_target = urljoin(url, form_details["action"])
            print(f"[+] Testing form #{i} with payload: {payload}")
            if form_details["method"] == "post":
                res = requests.post(url_target, data=data)
            else:
                res = requests.get(url_target, params=data)

            if is_vulnerable(res):
                print(f"[!!] XSS vulnerability detected with payload: {payload}")
            else:
                print("[-] No vulnerability detected with this payload.")

# ----------------------------------
# Main Execution
# ----------------------------------
if __name__ == "__main__":
    print_logo()

    parser = argparse.ArgumentParser(description="BEAST XSS - Advanced XSS Exploitation Tool")
    parser.add_argument("url", help="Target URL")
    parser.add_argument("-p", "--payloads", help="Path to payload list", default="payloads/basic.txt")

    args = parser.parse_args()
    target_url = args.url
    payload_list = load_payloads(args.payloads)

    if payload_list:
        scan_xss(target_url, payload_list)
    else:
        print("[!] No payloads to test.")
