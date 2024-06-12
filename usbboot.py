import subprocess
import os
import time
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Check and install/update necessary packages
def check_and_install_packages():
    required_packages = ["lsblk", "dd", "clamscan"]
    for package in required_packages:
        try:
            subprocess.run(["which", package], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(Fore.GREEN + f"{package} is already installed.")
        except subprocess.CalledProcessError:
            print(Fore.YELLOW + f"{package} is not installed. Installing...")
            if package == "clamscan":
                subprocess.run(["sudo", "apt-get", "update"])
                subprocess.run(["sudo", "apt-get", "install", "-y", "clamav"])
            else:
                subprocess.run(["sudo", "apt-get", "update"])
                subprocess.run(["sudo", "apt-get", "install", "-y", package])
    print(Fore.GREEN + "Packages installed successfully.")
    time.sleep(2)

class USBBootTool:
    def __init__(self, author_name, github_link):
        self.author_name = author_name
        self.github_link = github_link
        self.tool_name = "USB BOOT"

    def get_usb_devices(self):
        # List all the available SCSI devices (which includes USB devices)
        try:
            result = subprocess.run(['lsblk', '-S', '-o', 'NAME,SIZE,TRAN,VENDOR,MODEL'], stdout=subprocess.PIPE)
            devices = result.stdout.decode('utf-8').strip().split('\n')[1:]  # Skip the header line
            usb_devices = [device for device in devices if 'usb' in device]
            return usb_devices
        except Exception as e:
            print(Fore.RED + f"An error occurred while fetching USB devices: {e}")
            return []

    def select_device(self, devices):
        print(Fore.YELLOW + "Available USB devices:")
        for i, device in enumerate(devices):
            print(Fore.CYAN + f"{i+1}. {device}")
        
        selected = int(input(Fore.GREEN + "Select a device by number: ")) - 1
        if 0 <= selected < len(devices):
            device_name = devices[selected].split()[0]
            return f"/dev/{device_name}"
        else:
            print(Fore.RED + "Invalid selection.")
            return None

    def write_image_to_device(self, device_path, image_path):
        if not os.path.exists(image_path):
            print(Fore.RED + f"The image file {image_path} does not exist.")
            return
        
        try:
            subprocess.run(['sudo', 'dd', f'if={image_path}', f'of={device_path}', 'bs=4M', 'status=progress', 'oflag=sync'])
            print(Fore.GREEN + "The image has been successfully written to the USB device.")
        except Exception as e:
            print(Fore.RED + f"An error occurred while writing the image: {e}")

    def remove_viruses(self, device_path):
        try:
            subprocess.run(['sudo', 'clamscan', '--remove', '--recursive', device_path])
            print(Fore.GREEN + "Virus scan and removal completed.")
        except Exception as e:
            print(Fore.RED + f"An error occurred during the virus scan: {e}")

def clear_terminal():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def display_rainbow_banner():
    banner_lines = [
        "ooooo     ooo  .oooooo..o oooooooooo.       oooooooooo.    .oooooo.     .oooooo.   ooooooooooooo",
        "`888'     `8' d8P'    `Y8 `888'   `Y8b      `888'   `Y8b  d8P'  `Y8b   d8P'  `Y8b  8'   888   `8",
        " 888       8  Y88bo.       888     888       888     888 888      888 888      888      888      ",
        " 888       8   `\"Y8888o.   888oooo888'       888oooo888' 888      888 888      888      888      ",
        " 888       8       `\"Y88b  888    `88b       888    `88b 888      888 888      888      888      ",
        " `88.    .8'  oo     .d8P  888    .88P       888    .88P `88b    d88' `88b    d88'      888      ",
        "   `YbodP'    8\"\"88888P'  o888bood8P'       o888bood8P'   `Y8bood8P'   `Y8bood8P'      o888o     ",
        "",
        "=====================================================================================================",
        "Author: Kaleemullah Khan",
        "GitHub: https://github.com/kaleemullahkhan786"
    ]
    
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

    for line in banner_lines[:-2]:  # Exclude the last two lines for rainbow coloring
        for i, char in enumerate(line):
            print(colors[i % len(colors)] + char, end="")
        print()
        time.sleep(0.05)  # Delay to create a simple animation effect

    # Print the author and GitHub lines without rainbow effect
    for line in banner_lines[-2:]:
        print(Fore.YELLOW + line)
        time.sleep(0.05)

def main():
    author_name = "Kaleemullah Khan"
    github_link = "https://github.com/kaleemullahkhan786"
    tool = USBBootTool(author_name, github_link)

    clear_terminal()
    display_rainbow_banner()
    check_and_install_packages()
    clear_terminal()
    display_rainbow_banner()

    print("\n" + Fore.YELLOW + "Select an option:")
    print(Fore.YELLOW + "1. Write OS image to USB device")
    print(Fore.YELLOW + "2. Remove viruses from USB device")
    
    choice = int(input(Fore.GREEN + "Enter your choice: "))
    
    usb_devices = tool.get_usb_devices()
    if not usb_devices:
        print(Fore.RED + "No USB devices found.")
        return
    
    device = tool.select_device(usb_devices)
    if not device:
        return
    
    if choice == 1:
        image_path = input(Fore.GREEN + "Enter the path to the OS image file: ")
        tool.write_image_to_device(device, image_path)
    elif choice == 2:
        tool.remove_viruses(device)
    else:
        print(Fore.RED + "Invalid choice.")

if __name__ == "__main__":
    main()

