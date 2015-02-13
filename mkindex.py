from path import path
import markdown
import sys


def mark_header(lines, sentinel="---"):
    watcher = set()
    for line in lines:
        if line.startswith(sentinel):
            if not "started" in watcher:
                watcher.add('started')
            else:
                watcher.add('ended')
                yield (True, line)

        if "started" in watcher and not "ended" in watcher:
            yield (True, line)
        else:
            yield (False, line)


def split_doc(lines):
    ls = mark_header(lines)
    ls = [x for x in ls]
    headers = "".join(x for h, x in ls if h is True)
    body = "".join(x for h, x in ls if h is False)
    return headers, body


def main(args=sys.argv[:1]):
    idx = path("index.md")
    headers, body = split_doc(idx.lines())
    html = markdown.markdown(body)
    out = "\n".join((headers, html))
    path('index.html').write_text(out)


if __name__ == "__main__":
    main()
