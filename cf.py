import os

# Root directory
root_dir = "docs/Custom Formats"

# This function consolidates the markdown files in the given directory.
def consolidate_md_files(directory):
    consolidated_content = ""
    
    # List all markdown files in the directory
    md_files = [f for f in os.listdir(directory) if f.endswith('.md')]
    
    for md_file in md_files:
        # Extract filename without extension for the header
        header = os.path.splitext(md_file)[0]
        consolidated_content += f"## {header}\n\n"
        
        # Read content of markdown file
        with open(os.path.join(directory, md_file), 'r') as infile:
            consolidated_content += infile.read() + "\n\n"
            
    print(f"Consolidated {len(md_files)} files from {directory}.")
    
    return consolidated_content

print(f"Starting from root directory: {root_dir}\n")

# For each sub-directory in the root directory
for foldername, _, _ in os.walk(root_dir):
    print(f"Checking directory: {foldername}")
    # Check if it's a direct child of root_dir (ignoring the root directory itself)
    if os.path.dirname(foldername) == root_dir and foldername != root_dir:
        print(f"Processing sub-directory: {foldername}")
        # Get the consolidated content for the directory
        content = consolidate_md_files(foldername)
        
        # Write to a new file in the root directory
        output_file = os.path.join(root_dir, foldername.split('\\')[-1] + ".md")
        with open(output_file, 'w') as outfile:
            outfile.write(content)

        print(f"Written consolidated content to {output_file}\n")
    else:
        print(f"Skipped directory: {foldername}\n")

print("Consolidation process finished!")
