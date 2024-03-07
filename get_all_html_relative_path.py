import os


def find_html_files(directory):
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                relative_path = os.path.relpath(os.path.join(root, file), directory)
                html_files.append((relative_path.replace('\\', '/'), file))
    return html_files


def generate_html_links(html_files):
    links = []
    for relative_path, filename in html_files:
        link = f'<p><a href="./{relative_path}" target="_blank">{filename[0:-5]}</a></p>'
        links.append(link)
    return links


if __name__ == "__main__":
    current_directory = os.getcwd()
    html_files = find_html_files(current_directory)
    links = generate_html_links(html_files)
    for link in links:
        print(link)
