import os, pytest
from shop.files import read_invoice, INVOICE_DIR

def test_read_invoice_path_traversal(tmp_path, monkeypatch):
    # Use a temporary invoice directory
    temp_dir = tmp_path / "invoices"
    temp_dir.mkdir()
    monkeypatch.setattr('shop.files.INVOICE_DIR', str(temp_dir))

    # Normal invoice file should be readable
    normal_name = "normal.txt"
    (temp_dir / normal_name).write_text("normal", encoding="utf-8")
    assert read_invoice(normal_name) == "normal"

    # Craft a traversal name that points to this test file itself
    target = os.path.abspath(__file__)
    malicious = os.path.relpath(target, str(temp_dir))
    with pytest.raises(ValueError, match="Invalid invoice path"):
        read_invoice(malicious)
