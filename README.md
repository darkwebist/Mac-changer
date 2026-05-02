# MAC Changer

This Python script allows you to temporarily change the MAC address of a network interface on Linux systems.

## Installation

To install and run the script, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/darkwebist/Mac-changer.git
    ```

2.  **Navigate into the project directory:**
    ```bash
    cd Mac-changer
    ```

3.  **Make the script executable:**
    ```bash
    chmod +x mac_changer.py
    ```

## Usage

To change the MAC address of a network interface, run the script with `sudo` privileges and specify the interface and the new MAC address.

```bash
sudo python3 mac_changer.py -i <interface> -m <new_mac>
```

Example:

```bash
sudo python3 mac_changer.py -i eth0 -m 02:11:22:33:44:55
```

Required Arguments:

· -i or --interface: The network interface (e.g., eth0, wlan0).
· -m or --mac: The new MAC address (format: XX:XX:XX:XX:XX:XX).

Requirements

· Linux operating system
· Python 3.6+
· ip command (usually part of iproute2 package)
· sudo privileges (required to change MAC address)

Important Notes

· The script must be run with sudo or as root.
· The MAC address change is temporary and will revert to the original after a system reboot.
· Avoid using invalid MAC addresses like 00:00:00:00:00:00. A safe example is 02:11:22:33:44:55.

Author

@DarkWebist
