

s_bytes = b"enrico" # bytes
print(f"{s_bytes} type(s_bytes)")

s_bytearray =bytearray("enrico", "UTF-8") 
s_bytearray.extend(b"  un bravo ragazzo")
print(f"{s_bytearray} {type(s_bytearray)}")

s = "enrico"
s_enc = s.encode("utf-8")
print(f"type(x.encode): {type(s_enc)}")

b = b"enrico"
b_decod = b.decode("utf-8")
print(f"type(b_decod): {type(b_decod)}")

