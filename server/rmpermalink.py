import os
import glob

# Set the directory where the Markdown files are located
directory = "."

# Find all Markdown files with "qotd" in the file name
markdown_files = glob.glob(os.path.join(directory, "*qotd*.md"))

# Process each Markdown file
for file_path in markdown_files:
    with open(file_path, "r") as file:
        content = file.readlines()

    # Find the YAML frontmatter
    frontmatter_start = None
    frontmatter_end = None
    for i, line in enumerate(content):
        if line.strip() == "---":
            if frontmatter_start is None:
                frontmatter_start = i
            else:
                frontmatter_end = i
                break

    # Ensure frontmatter is present
    if frontmatter_start is None or frontmatter_end is None:
        continue

    # Parse the YAML frontmatter
    frontmatter_lines = content[frontmatter_start + 1 : frontmatter_end]
    frontmatter = {}
    for line in frontmatter_lines:
        key, value = line.strip().split(": ", 1)
        frontmatter[key] = value

    # Remove the "permalink" frontmatter object
    frontmatter.pop("permalink", None)

    # Generate the modified content
    modified_content = "---\n"
    for key, value in frontmatter.items():
        modified_content += f"{key}: {value}\n"
    modified_content += "---\n"
    modified_content += "".join(content[frontmatter_end + 1:])

    # Write the modified content back to the file
    with open(file_path, "w") as file:
        file.write(modified_content)
