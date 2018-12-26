import struct
with open("boundary.tob", "rb") as fp:
    data = fp.read()
# data_int = int.from_bytes(data, byteorder='big')
data_int = struct.unpack('i', data)

print(data_int)