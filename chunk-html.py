def chunk_html(html, chunk_size):
    """Chunks HTML into evenly sized segments of n characters.

    Args:
        html: The HTML content to be chunked.
        chunk_size: The desired size of each chunk in characters.

    Returns:
        A list of HTML chunks.
    """

    chunks = []
    while len(html) > chunk_size:
        chunk = html[:chunk_size]
        html = html[chunk_size:]

        # Ensure that chunks don't cut off tags
        while not chunk.endswith('>') and len(html) > 0:
            chunk += html[:1]
            html = html[1:]

        chunks.append(chunk)

    if html:
        chunks.append(html)

    return chunks

# Example usage
html_content = """
<!DOCTYPE html>
<html>
<head>
<title>Example HTML</title>
</head>
<body>
<h1>This is a heading</h1>
<p>This is a paragraph.</p>
</body>
</html>
"""

chunk_size = 50
chunked_html = chunk_html(html_content, chunk_size)

for chunk in chunked_html:
    print('TO_CLOB(\''+ chunk + '\') || ')
