import os

DIR = r"c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign"
CSS_FILE = os.path.join(DIR, "styles.css")

# Read the file as raw bytes
with open(CSS_FILE, "rb") as f:
    raw_bytes = f.read()

# It's possible the file starts with UTF-16 BOM and switches to UTF-8
# Let's try to decode the whole thing. We can do this by splitting at a known point or decoding ignoring errors
# But wait, earlier I overwrote styles.css entirely using write_to_file in utf-8?
# Wait, let's just decode with utf-8 replacing errors, and see if it looks right.
try:
    content = raw_bytes.decode('utf-8')
    print("Decoded as utf-8 successfully.")
except UnicodeDecodeError:
    print("File has invalid utf-8 bytes.")
    # Try decoding as utf-16
    try:
        content = raw_bytes.decode('utf-16')
        print("Decoded as utf-16 successfully.")
        with open(CSS_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print("Converted to utf-8.")
    except Exception as e:
        print("Failed to decode as utf-16:", e)
        # If it's a mix, let's just decode ignoring errors
        content = raw_bytes.decode('utf-8', errors='ignore')
        with open(CSS_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print("Saved ignoring utf-8 errors.")
