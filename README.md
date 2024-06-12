# USB-Boot Tool

![Banner](https://imgur.com/a/sTLshua)

## Description
The USB-Boot Tool is a powerful utility designed to simplify the process of creating bootable USB drives and managing USB devices. It provides an easy-to-use interface for writing OS images to USB devices and removing viruses from USB drives, leveraging the capabilities of `dd` and `clamscan` tools.

## Features
- **Write OS Image to USB Device**: Quickly write an operating system image to a USB drive using `dd`.
- **Remove Viruses from USB Device**: Scan and remove viruses from USB drives using `clamscan`.

## Requirements
- `lsblk` (already installed on most Linux distributions)
- `dd` (already installed on most Linux distributions)
- `clamscan` (part of ClamAV, an open-source antivirus engine)

## Installation
The script will check for and install any missing dependencies automatically. However, you can manually install the necessary tools using the following commands:

### Install `lsblk` and `dd`
These tools are usually pre-installed on most Linux distributions. If not, install them using:
```bash
sudo apt update
sudo apt install util-linux coreutils
```

### Install `clamscan`
To install ClamAV and `clamscan`, run:
```bash
sudo apt update
sudo apt install clamav
```

## Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/kaleemullahkhan786/Usb-Boot.git
    cd Usb-Boot
    ```

2. Make the script executable:
    ```bash
    chmod +x usbboot.py
    ```

3. Run the script:
    ```bash
    python3 usbboot.py
    ```

## Commands
The script offers two primary options:
1. **Write OS image to USB device**:
    - Prompts you to select a USB device.
    - Asks for the path to the OS image file.
    - Writes the OS image to the selected USB device using `dd`.

2. **Remove viruses from USB device**:
    - Prompts you to select a USB device.
    - Scans the selected USB device for viruses using `clamscan`.
    - Removes any detected viruses.

## Author
Kaleemullah Khan

GitHub: [kaleemullahkhan786](https://github.com/kaleemullahkhan786)
```

This `README.md` file includes a description of the tool, its features, installation instructions, usage instructions, and author details. The banner image is embedded at the top.
