import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import shop.tools

def test_stock_report_injection():
    marker = "SFX_MARK_7731"
    malicious_sku = f"ABC123 & echo {marker}"
    output = shop.tools.stock_report(malicious_sku)
    lines = [line.strip() for line in str(output).splitlines()]
    assert marker not in lines, f"a second command ran: {output!r}"
