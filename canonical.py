import os
import re

def add_canonical_url_to_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Find the front matter block using regex
    match = re.search(r'^---\n(.*\n)*?---\n', content, re.MULTILINE)
    if not match:
        # No front matter block found, do nothing
        return

    front_matter_block = match.group(0)
    front_matter_vars = {}

    # Parse front matter block into a dictionary
    for line in front_matter_block.split('\n'):
        line = line.strip()
        if line.startswith('#'):
            continue
        if ':' in line:
            key, value = line.split(':', 1)
            front_matter_vars[key.strip()] = value.strip()

    # Determine if link or token variable exists and set canonical_url accordingly
    if 'link' in front_matter_vars:
        canonical_url = front_matter_vars['link']
    elif 'token' in front_matter_vars:
        canonical_url = 'https://login.yeahgames.net/token/' + front_matter_vars['token']
    else:
        # No link or token variable found, do nothing
        return

    # Add canonical_url variable to front matter block
    front_matter_block += f'canonical_url: {canonical_url}\n'

    # Write updated content to file
    with open(filepath, 'w') as f:
        f.write(front_matter_block + content[len(match.group(0)):])

def add_canonical_urls_to_directory(directory):
    # Loop over all Markdown files in directory
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            filepath = os.path.join(directory, filename)
            add_canonical_url_to_file(filepath)

# Example usage: add canonical_url variable to all Markdown files in the current directory
add_canonical_urls_to_directory('.')