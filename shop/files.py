"""Invoice downloads: customers fetch their invoice text files by name."""

import os

INVOICE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "invoices")


def read_invoice(name):
    """Return the text of an invoice stored in the invoices folder."""
    invoice_path = os.path.abspath(os.path.join(INVOICE_DIR, name))
    if not invoice_path.startswith(os.path.abspath(INVOICE_DIR) + os.sep):
        raise ValueError("Invalid invoice path")
    with open(invoice_path, encoding="utf-8") as fh:
        return fh.read()


def list_invoices():
    return sorted(f for f in os.listdir(INVOICE_DIR) if f.endswith(".txt"))
