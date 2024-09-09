import os

while True:
    # Ask user the file input name
    input_file_name = input("Input file name: ")
    
    # If input is exit, then the program finishes
    if input_file_name.lower() == "exit":
        print("Finishing program.")
        break

    output_file_name = input_file_name[:-2]+"xhtml"

    # Convert the file to xhtml using pandoc
    os.system(f"pandoc -s {input_file_name} --metadata-file=metadata.txt -o {output_file_name}")
