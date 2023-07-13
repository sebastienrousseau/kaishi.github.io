import zipfile
import os

def create_zip():
    # Define the folders and files to include in the zip
    folders = ['content', 'template']
    files = ['README.md']

    # Name of the resulting zip file
    zip_filename = 'docs/kaishi.zip'

    # Create a new zip file
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        # Add folders to the zip
        for folder in folders:
            for root, _, filenames in os.walk(folder):
                for filename in filenames:
                    file_path = os.path.join(root, filename)
                    zipf.write(file_path, os.path.relpath(file_path))

        # Add individual files to the zip
        for file in files:
            zipf.write(file, os.path.basename(file))

    print(f'Successfully created {zip_filename}.')

# Call the function to generate the zip file
create_zip()
