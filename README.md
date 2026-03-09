# Python Vulnerability Scanner

## Overview

This project is a simple **Vulnerability Scanner** developed using Python.
It analyzes a target system and checks for potential **security weaknesses** based on open ports or services.

The tool demonstrates basic concepts used in **cybersecurity and penetration testing**.

---

## Features

* Detect open ports
* Identify potential vulnerabilities
* Basic network scanning functionality
* Lightweight and easy to understand

---

## Technologies Used

* Python
* Socket Programming
* Networking Concepts

---

## How It Works

The vulnerability scanner works in multiple steps:

1. Scan the target host
2. Detect open ports
3. Identify services running on those ports
4. Check for potential vulnerabilities

---

## Example Usage

Run the scanner:

```
python vulnscanner.py
```

Example output:

```
Scanning target: 192.168.1.1

Open Port Detected: 21 (FTP)
Potential Vulnerability: FTP service may allow anonymous login

Open Port Detected: 80 (HTTP)
Potential Vulnerability: Web server may expose sensitive information
```

---

## Applications

* Cybersecurity learning
* Network analysis
* Basic penetration testing practice

---

## Disclaimer

This project is intended **only for educational and ethical security testing purposes**.
Always obtain proper authorization before scanning any system.
