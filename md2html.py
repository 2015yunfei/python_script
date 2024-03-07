import os
import markdown


def convert_markdown_to_html(markdown_file):
    """
    Converts a Markdown file to HTML.
    """
    with open(markdown_file, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()
        html_content = markdown.markdown(md_content)
        return html_content


def main():
    # 获取当前目录下的所有Markdown文件
    markdown_files = [file for file in os.listdir() if file.endswith('.md')]

    for md_file in markdown_files:
        html_content = convert_markdown_to_html(md_file)

        # 将HTML内容保存到同名的HTML文件中
        html_file = os.path.splitext(md_file)[0] + '.html'
        with open(html_file, 'w', encoding='utf-8') as output_file:
            output_file.write(html_content)

        print(f"已将 {md_file} 转换为 {html_file}")


if __name__ == "__main__":
    main()
