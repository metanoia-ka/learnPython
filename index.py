from pathlib import Path

created_dr = input("Enter the name of the directory to create: ")
folder = Path(created_dr)

if created_dr == "backup":
    if folder.exists():
        print("✅ Directory already exists.")
    else:
        folder.mkdir()
        print("📂 Directory created successfully.")
else:
    print("❌ Invalid directory name.")
    
