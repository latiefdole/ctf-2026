import struct

with open('profile.jpg', 'rb') as f:
    data = f.read()

# The EXIF starts at offset 20+4 = 24 (after FF E1 + length)
# Exif header: "Exif\x00\x00" then TIFF header
exif_start = 20 + 4  # skip marker + length
exif_data = data[exif_start:]

# Check for Exif\0\0
print("Header:", exif_data[:6])

# TIFF header starts after "Exif\0\0"
tiff_start = exif_start + 6
tiff_data = data[tiff_start:]

# Byte order
byte_order = tiff_data[:2]
print(f"Byte order: {byte_order}")
big_endian = byte_order == b'MM'

def read_u16(d, offset):
    if big_endian:
        return struct.unpack('>H', d[offset:offset+2])[0]
    return struct.unpack('<H', d[offset:offset+2])[0]

def read_u32(d, offset):
    if big_endian:
        return struct.unpack('>I', d[offset:offset+4])[0]
    return struct.unpack('<I', d[offset:offset+4])[0]

def read_rational(d, offset):
    num = read_u32(d, offset)
    den = read_u32(d, offset+4)
    return num / den if den != 0 else 0

# IFD0 offset
ifd0_offset = read_u32(tiff_data, 4)
print(f"IFD0 offset: {ifd0_offset}")

# Read IFD0
num_entries = read_u16(tiff_data, ifd0_offset)
print(f"IFD0 entries: {num_entries}")

gps_ifd_offset = None
for i in range(num_entries):
    entry_offset = ifd0_offset + 2 + i * 12
    tag = read_u16(tiff_data, entry_offset)
    typ = read_u16(tiff_data, entry_offset + 2)
    count = read_u32(tiff_data, entry_offset + 4)
    value = read_u32(tiff_data, entry_offset + 8)
    tag_names = {
        0x011a: 'XResolution',
        0x011b: 'YResolution',
        0x0128: 'ResolutionUnit',
        0x0213: 'YCbCrPositioning',
        0x8825: 'GPSInfoIFDPointer'
    }
    name = tag_names.get(tag, f'Tag_0x{tag:04X}')
    print(f"  {name} (0x{tag:04X}): type={typ}, count={count}, value/offset={value}")
    if tag == 0x8825:
        gps_ifd_offset = value

if gps_ifd_offset:
    print(f"\n=== GPS IFD at offset {gps_ifd_offset} ===")
    num_gps = read_u16(tiff_data, gps_ifd_offset)
    print(f"GPS entries: {num_gps}")
    
    gps_data = {}
    for i in range(num_gps):
        entry_offset = gps_ifd_offset + 2 + i * 12
        tag = read_u16(tiff_data, entry_offset)
        typ = read_u16(tiff_data, entry_offset + 2)
        count = read_u32(tiff_data, entry_offset + 4)
        value_offset = read_u32(tiff_data, entry_offset + 8)
        
        gps_tags = {
            0: 'GPSVersionID', 1: 'GPSLatitudeRef', 2: 'GPSLatitude',
            3: 'GPSLongitudeRef', 4: 'GPSLongitude', 5: 'GPSAltitudeRef',
            6: 'GPSAltitude'
        }
        name = gps_tags.get(tag, f'GPS_0x{tag:04X}')
        
        if typ == 5:  # RATIONAL
            vals = []
            for j in range(count):
                r = read_rational(tiff_data, value_offset + j * 8)
                vals.append(r)
            print(f"  {name}: {vals}")
            gps_data[tag] = vals
        elif typ == 2:  # ASCII
            if count <= 4:
                s = tiff_data[entry_offset+8:entry_offset+8+count].decode('ascii', errors='replace').rstrip('\x00')
            else:
                s = tiff_data[value_offset:value_offset+count].decode('ascii', errors='replace').rstrip('\x00')
            print(f"  {name}: '{s}'")
            gps_data[tag] = s
        elif typ == 1:  # BYTE
            print(f"  {name}: {value_offset}")
            gps_data[tag] = value_offset
        elif typ == 3:  # SHORT
            print(f"  {name}: {value_offset}")
            gps_data[tag] = value_offset
        else:
            print(f"  {name}: type={typ}, count={count}, value={value_offset}")
    
    # Calculate coordinates
    if 2 in gps_data and 4 in gps_data:
        lat = gps_data[2]
        lon = gps_data[4]
        lat_dec = lat[0] + lat[1]/60 + lat[2]/3600
        lon_dec = lon[0] + lon[1]/60 + lon[2]/3600
        lat_ref = gps_data.get(1, 'N')
        lon_ref = gps_data.get(3, 'E')
        if lat_ref == 'S':
            lat_dec = -lat_dec
        if lon_ref == 'W':
            lon_dec = -lon_dec
        print(f"\n  COORDINATES: {lat_dec}, {lon_dec}")
        print(f"  Google Maps: https://maps.google.com/?q={lat_dec},{lon_dec}")
