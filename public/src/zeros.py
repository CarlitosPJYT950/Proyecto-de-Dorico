import os, zipfile

with open("zeros.bin", "wb") as f:
    f.write(bytes(100_000))  # Create a file with 1024 zero bytes

with zipfile.ZipFile("zeros.zip", "w", zipfile.ZIP_DEFLATED) as z:
    z.write("zeros.bin")

print(os.path.getsize("zeros.zip"))  # Print the size of the zip file
print(os.path.getsize("zeros.bin"))  # Print the size of the original file
