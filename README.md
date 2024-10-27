
---

# Falcon Post Quantum Signature Verification

This project provides a Python implementation for **Falcon Post Quantum Signature Verification**. It includes a pre-built `.whl` file and a Python script for demonstrating how to verify post-quantum signatures using the Falcon algorithm, a lattice-based signature scheme designed to provide secure digital signatures even in the presence of quantum computing.

---

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

---

## Overview

**Falcon** is a post-quantum secure digital signature algorithm based on the **NIST PQC standards**. It uses lattice-based cryptography, which is highly resistant to quantum-based attacks, making it ideal for securing data and communications in a post-quantum era. This project includes a sample `.whl` file and a Python program to verify signatures using Falcon.

---

## Installation

To use this project, you need to have Python installed (version 3.6 or higher is recommended). Follow these steps:

1. **Clone the Repository** (if applicable):
    ```bash
    git clone https://github.com/codehat01/secure_coding_project.git
    cd secure_coding_project
    ```

2. **Install the WHL file**:
   - Locate the `.whl` file included in this project (e.g., `falcon_pqs-0.1-py3-none-any.whl`).
   - Install it using `pip`:
     ```bash
     pip install falcon_pqs-0.1-py3-none-any.whl
     ```

3. **Install Dependencies**:
    - If there are additional dependencies, install them using the requirements file:
      ```bash
      pip install -r requirements.txt
      ```

---

## Usage

After installation, you can run the provided Python program to verify signatures using the Falcon algorithm.

1. **Running the Verification Script**:
   - The verification script (`pythonfalcon.py`) requires an input file with the digital signature and the corresponding public key.
   - Run the script as follows:
     ```bash
     python pythonfalcon.py
     ```

2. **Example Command**:
    ```bash
    python pythonfalcon.py
    ```

3. **Expected Output**:
   - The script will output whether the signature is **valid** or **invalid**.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note**: This project assumes a working knowledge of cryptographic terms and processes, particularly post-quantum cryptography. For more information on Falcon, see the [NIST Falcon documentation](https://csrc.nist.gov/publications/detail/nistir/8240/final).

