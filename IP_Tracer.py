import os
import time
import socket
import requests
import subprocess


def logo():
    """Displays the tool's logo with styled text and 'By CipherX'."""
    os.system("clear")
    print('''
\033[01;33m

\033[01;31m      _\033[01;33m ____    _
     \033[01;31m(_)\033[01;33m  _ \\  | |_ _ __ __ _  ___ ___ _ __
     | | |_) | | __| '__/ _` |/ __/ _ \\ '__|
     | |  __/  | |_| | | (_| | (_|  __/ |
     |_|_|      \\__|_|  \\__,_|\\___\\___|_|

   \033[01;37m}\033[01;31m----------------------------------------\033[01;37m{
}\033[01;31m-------------- \033[01;32mTrack IPLocation\033[01;31m --------------\033[01;37m{
   }\033[01;31m---------------\033[01;32mBy CipherX\033[01;31m---------------\033[01;37m{

\033[00m
   
''')


def trace_ip(ip):
    """Trace the given IP address and display its information."""
    try:
        # Get the domain name for the IP
        domain_name = socket.gethostbyaddr(ip)
        print(f"Domain name for {ip}: {domain_name[0]}")
    except socket.herror:
        print(f"Could not find the domain name for IP: {ip}")

    # Get geolocation information using an API
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        if response.status_code == 200:
            data = response.json()
            print(f"IP: {ip}")
            print(f"Country: {data['country']}")
            print(f"Region: {data['regionName']}")
            print(f"City: {data['city']}")
            print(f"ZIP: {data['zip']}")
            print(f"ISP: {data['isp']}")
            print(f"Organization: {data['org']}")
            print(f"Latitude: {data['lat']}")
            print(f"Longitude: {data['lon']}")
        else:
            print("Unable to fetch geolocation data.")
    except requests.RequestException as e:
        print(f"Error fetching geolocation data: {e}")


def track_my_ip():
    """Track the user's current IP address."""
    try:
        response = requests.get('https://api.ipify.org?format=json')
        if response.status_code == 200:
            ip = response.json()['ip']
            print(f"Your IP Address: {ip}")
            trace_ip(ip)
        else:
            print("Unable to get your IP address.")
    except requests.RequestException as e:
        print(f"Error fetching your IP: {e}")


def display_about():
    """Display information about the tool."""
    logo()
    print("\nIP-Tracer is a simple tool for tracing IP addresses, providing geolocation information and domain names.\n")


def display_help():
    """Display help instructions."""
    logo()
    print("Help - How to Use IP-Tracer:")
    print("[1] Track IP Address: Allows you to trace any given IP address.")
    print("[2] Track Your IP Address: Provides details about your own public IP address.")
    print("[3] About us: Shows information about this tool.")
    print("[4] Help: Displays this help message.")
    print("[5] Update IP-Tracer: Checks for updates.")
    print("[x] Exit: Exits the program.")


def update_ip_tracer():
    """Simulates updating the tool."""
    logo()
    print("\n\033[01;32mUpdating IP-Tracer.........\033[01;37m\n")
    time.sleep(1)

    try:
        # Simulate Git clone and installation commands
        subprocess.run(["git", "clone", "https://github.com/rajkumardusad/IP-Tracer.git", "~/IP-Tracer"], check=True)
        subprocess.run(["sh", "install"], cwd="~/IP-Tracer", check=True)
        print("\n\033[01;32mIP-Tracer updated successfully!\033[01;37m")
    except subprocess.CalledProcessError as e:
        print(f"Error during update: {e}")
    except FileNotFoundError:
        print("Git or installation command not found. Please ensure you have Git and shell installed.")

    time.sleep(1)


def main():
    """Main menu to interact with the IP-Tracer tool."""
    while True:
        logo()
        print("[1] Track IP Address.")
        print("[2] Track Your IP Address.")
        print("[3] About us.")
        print("[4] Help.")
        print("[5] Update IP-Tracer.")
        print("[x] Exit")

        choice = input("\nEnter your choice: ").strip().lower()

        if choice == '1':
            ip_address = input("Enter IP Address to track: ").strip()
            trace_ip(ip_address)
        elif choice == '2':
            track_my_ip()
        elif choice == '3':
            display_about()
        elif choice == '4':
            display_help()
        elif choice == '5':
            update_ip_tracer()
        elif choice == 'x' or choice == 'exit':
            print("\n\033[01;31mExiting IP-Tracer. Goodbye!\033[00m\n")
            break
        else:
            print("\033[01;31mInvalid choice. Please try again.\033[00m")


if __name__ == "__main__":
    main()
