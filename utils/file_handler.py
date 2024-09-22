import base64
import magic  # You can use python-magic for MIME type detection

def validate_file(file_b64):
    if not file_b64:
        return False, None, None

    try:
        file_data = base64.b64decode(file_b64)
        mime_type = magic.from_buffer(file_data, mime=True)
        file_size_kb = len(file_data) / 1024  # File size in KB
        return True, mime_type, round(file_size_kb, 2)
    except Exception:
        return False, None, None