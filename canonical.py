import os
import re
import glob

directory = 'C:/Users/talli/Documents/GitHub/library/_posts'

front_matter_regex = r'^---\n([\s\S]*?)\n---\n([\s\S]*)'

variable_regex = r'^(token|link):\s*(.*)$'

for file_path in glob.glob(os.path.join(directory, '*.md')):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()

    match = re.match(front_matter_regex, file_contents)
    if match:
        front_matter = match.group(1)
        content = match.group(2)

        token_match = re.search(variable_regex, front_matter, re.MULTILINE)
        token_value = token_match.group(2) if token_match and token_match.group(1) == 'token' else None
        link_match = re.search(variable_regex, front_matter, re.MULTILINE)
        link_value = link_match.group(2) if link_match and link_match.group(1) == 'link' else None

        if token_value:
            canonical_url_str = 'canonical_url: https://login.yeahgames.net/token/{}\n'.format(token_value)
            front_matter = front_matter.strip() + '\n' + canonical_url_str
        elif link_value:
            canonical_url_str = 'canonical_url: {}\n'.format(link_value)
            front_matter = front_matter.strip() + '\n' + canonical_url_str

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('---\n')
            file.write(front_matter.strip())
            file.write('\n---\n')
            file.write(content)
