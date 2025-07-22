import xml.etree.ElementTree as ET

def remove_dangerous_permissions(manifest_path, dangerous_perms):
    tree = ET.parse(manifest_path)
    root = tree.getroot()
    removed = []

    for perm in list(root.findall("uses-permission")):
        name = perm.attrib.get("{http://schemas.android.com/apk/res/android}name")
        if name in dangerous_perms:
            root.remove(perm)
            removed.append(name)

    tree.write(manifest_path, encoding="utf-8", xml_declaration=True)
    return removed

if __name__ == "__main__":
    path = "demo_apk/AndroidManifest.xml"
    dangerous = [
        "android.permission.RECORD_AUDIO",
        "android.permission.READ_SMS",
        "android.permission.CAMERA",
        "android.permission.ACCESS_FINE_LOCATION"
    ]
    removed = remove_dangerous_permissions(path, dangerous)
    print("Permissions removed:", removed)
