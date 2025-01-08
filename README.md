# PDF Receipt Generator and Emailer

This is a standalone Python application that generates PDF receipts from an Excel file, sends the receipts via email to recipients, and includes a Tkinter-based GUI for user interaction.

---

## Features

- **Excel to PDF Conversion**: Converts Excel data into well-formatted PDF receipts.
- **Email Sending**: Emails the generated receipts to the specified recipients.
- **GUI Interface**: User-friendly Tkinter-based interface for easy operation.
- **Signature Integration**: Adds a digital signature to receipts.
- **Number to Words Conversion**: Converts numerical amounts to words for inclusion in receipts.

---

## Requirements

- Python 3.8 or higher

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
## install libraries
pip install -r requirements.txt
## mention sender email and app password for the gmail account
SENDER_EMAIL = 'your-email@example.com'   # Replace with your email
EMAIL_PASSWORD = 'your-app-password'     # Replace with your app password

