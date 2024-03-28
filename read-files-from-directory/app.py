from pathlib import Path

path = Path("./") # This will output all files from the current directory
all_files = path.glob("*")
output_file = "files.txt" 
file_list = []

for file in all_files:
    file_list.append(file)

    if not Path(output_file).exists():
        text_file =open(output_file, mode="x")

    text_file = open(output_file, mode="w")
    text_file.writelines(str(file_list))
    text_file.close()

print(f"Done! {Path(output_file)} is ready for use!")
print(f"You can find your file at {Path.cwd()}")