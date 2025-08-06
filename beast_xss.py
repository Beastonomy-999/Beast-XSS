import argparse
import os

def load_payloads(payload_file):
    try:
        with open(payload_file, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"❌ Payload file not found: {payload_file}")
        return []

def scan_url(url, payloads):
    print(f"\n🔍 Scanning URL: {url}")
    for payload in payloads:
        test_url = url + payload
        # Placeholder for real scanning logic
        print(f"    Testing → {test_url}")
    print(f"✅ Scan completed for: {url}\n")

def scan_from_file(file_path, payloads):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]
        for url in urls:
            scan_url(url, payloads)

def main():
    print("🦴 BEAST XSS - Launching ...")
    <p align="center">
  <img src="banner.png" alt="BEAST XSS" width="400px"/>
</p>
    parser = argparse.ArgumentParser(description="BEAST XSS - Advanced XSS Scanner")
    parser.add_argument('--url', help='Scan a single URL for XSS')
    parser.add_argument('--list', help='Scan multiple URLs from a file')
    parser.add_argument('--payloads', default='payloads/basic.txt', help='Payload list to use')
    args = parser.parse_args()

    payloads = load_payloads(args.payloads)

    if args.url:
        scan_url(args.url, payloads)
    elif args.list:
        scan_from_file(args.list, payloads)
    else:
        print("⚠️  Provide either --url or --list\n")
        parser.print_help()

if __name__ == "__main__":
    main()
