# UDP Flood Script (For Security Testing Only)

This script simulates a **UDP flood attack** for the purpose of **network security testing**. It sends random bytes to the target IP and port using the UDP protocol. This is intended for **educational and ethical testing** within controlled environments only.

> ⚠️ **Disclaimer**: This tool is intended for ethical use only. Do not use this on networks you do not own or have explicit permission to test. Unauthorized usage may be illegal.

---

## 🔧 Features
- Randomized byte stream generator using UDP
- Simple CLI interface
- Progress bar before the attack starts
- Auto-increments port numbers
- Cross-platform clear screen and banner (Linux/Windows)

---

## 🚀 Requirements
- Python 3.x
- `figlet` installed (for banner display on Linux/Mac)

---

## 📦 Installation
Clone the repository:

```bash
git clone https://github.com/safi-ullah-031 udp-flood-script.git 

```
```bash
cd UDP-Flood-Script
```

---
## 🛠 Usage
``` bash
python3 udp_flood.py
```
Then enter the following when prompted:

> Target IP address

> Target port


---
### 💡 Example

> IP Target : 192.168.1.1

> Port      : 80

The script will start sending packets and display logs for each one.

### 🧑‍💻 Author
- Safi Ullah
- GitHub: safi-ullah-031

### 📜 License
This project is open source under the MIT License.

---