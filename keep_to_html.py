from pathlib import Path
import json


def main():
    """ Convert Keep bookmarks to Netscape html file format.
    """
    with open('./bookmarks.html', 'w') as output:
        path = Path('.')

        html = ('<!DOCTYPE NETSCAPE-Bookmark-file-1>\n'
                '<META HTTP-EQUIV="Content-Type" '
                'CONTENT="text/html; charset=UTF-8">\n'
                '<!-- This is an automatically generated file.\n'
                'It will be read and overwritten.\n'
                'Do Not Edit! -->\n'
                '<TITLE>Bookmarks</TITLE>\n'
                '<H1>Bookmarks</H1>\n'
                '<DL>')

        for file in path.glob('*.json'):
            with open(file, mode='r', encoding='utf-8') as bookmark_file:
                json_file = json.load(bookmark_file)
                title = json_file['title']
                try:
                    lbl = [json_file['labels'][i]['name']
                           for i in range(len(json_file['labels']))]
                    lbl_string = ','.join(lbl)
                except KeyError:
                    lbl_string = ''
                try:
                    url = 'HREF="' + json_file['annotations'][0]['url'] + '"'
                except KeyError:
                    url = ''

                url_tag = f'\n<DT><A {url} TAGS="{lbl_string}">{title}</A>'

                html = (html + url_tag)

        html = html + '\n</DL>'
        output.write(html)


if __name__ == "__main__":
    main()
