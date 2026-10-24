import os
import sys
import glob
from bs4 import BeautifulSoup

base_dir = sys.argv[1] if len(sys.argv) > 1 else r"c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign"
html_files = [
    os.path.join(base_dir, f)
    for f in [
        "index.html",
        "about.html",
        "services.html",
        "products.html",
        "contact.html",
        "legal.html",
        "admin.html"
    ]
] + glob.glob(os.path.join(base_dir, "en", "*.html"))

real_files = set()
for root, dirs, files in os.walk(base_dir):
    for f in files:
        full = os.path.join(root, f)
        rel = os.path.relpath(full, base_dir).replace("\\", "/")
        real_files.add(rel)

# Collect all element IDs
all_ids = {}
for hf in html_files:
    rel = os.path.relpath(hf, base_dir).replace("\\", "/")
    with open(hf, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    all_ids[rel] = set(el.get("id") for el in soup.find_all(id=True))

broken = []
for hf in html_files:
    rel_hf = os.path.relpath(hf, base_dir).replace("\\", "/")
    dir_hf = os.path.dirname(hf)
    with open(hf, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    for tag, attr in [
        ("a", "href"),
        ("link", "href"),
        ("script", "src"),
        ("img", "src"),
    ]:
        for el in soup.find_all(tag, **{attr: True}):
            val = el[attr].strip()
            if not val or val.startswith(
                ("http://", "https://", "mailto:", "tel:", "javascript:")
            ):
                continue
            if val == "#":
                # Report dead hash links
                broken.append((rel_hf, f"<{tag} {attr}='{val}'>", "DEAD_HASH_LINK"))
                continue

            parts = val.split("#")
            file_part = parts[0].split("?")[0]
            hash_part = parts[1] if len(parts) > 1 else None

            target_file_rel = rel_hf
            if file_part:
                target = os.path.normpath(os.path.join(dir_hf, file_part))
                target_rel = os.path.relpath(target, base_dir).replace("\\", "/")
                target_file_rel = target_rel
                if target_rel not in real_files:
                    broken.append(
                        (rel_hf, f"<{tag} {attr}='{val}'>", "FILE_NOT_FOUND", target_rel)
                    )
                    continue

            if hash_part:
                target_ids = all_ids.get(target_file_rel, set())
                if hash_part not in target_ids:
                    broken.append(
                        (
                            rel_hf,
                            f"<{tag} {attr}='{val}'>",
                            f"ANCHOR_NOT_FOUND #{hash_part} in {target_file_rel}",
                        )
                    )

print(f"\n--- VERIFICATION AUDIT REPORT ---")
print(f"Total HTML files audited: {len(html_files)}")
print(f"Issues detected: {len(broken)}")
for b in broken:
    print(" ", b)

if not broken:
    print("SUCCESS: 100% PERFECT! No missing files, no dead links, all anchors verified!")
