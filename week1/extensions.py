mimetypes = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
}

filename = input("Enter filename: ").strip().lower()
extension = filename.split(".")

if len(extension) == 1:
    print("application/octet-stream")
else:
    print(mimetypes.get(extension[1], "application/octet-stream"))