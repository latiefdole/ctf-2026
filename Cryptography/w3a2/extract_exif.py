from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def extract_all_metadata():
    img_path = r'C:\Users\ICT-12\Documents\CTF\w3a2\key_source.jpg'
    img = Image.open(img_path)
    
    # 1. getexif
    exif = img.getexif()
    print("--- MAIN EXIF ---")
    for tag_id, val in exif.items():
        tag = TAGS.get(tag_id, tag_id)
        print(f"{tag} ({tag_id}): {val}")
        
    # 2. _getexif (Exif Sub-IFD)
    _exif = img._getexif()
    if _exif:
        print("\n--- SUB EXIF (_getexif) ---")
        for tag_id, val in _exif.items():
            tag = TAGS.get(tag_id, tag_id)
            print(f"{tag} ({tag_id}): {val}")
            
    # 3. GPS Info
    gps_info = exif.get_ifd(0x8825) # GPSInfo tag
    if gps_info:
        print("\n--- GPS INFO ---")
        for tag_id, val in gps_info.items():
            tag = GPSTAGS.get(tag_id, tag_id)
            print(f"{tag} ({tag_id}): {val}")
            
    # 4. EXIF IFD
    exif_ifd = exif.get_ifd(0x8769) # ExifOffset tag
    if exif_ifd:
        print("\n--- EXIF IFD ---")
        for tag_id, val in exif_ifd.items():
            tag = TAGS.get(tag_id, tag_id)
            print(f"{tag} ({tag_id}): {val}")

if __name__ == '__main__':
    extract_all_metadata()
