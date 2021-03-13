def create_html(tag, text, **attributes):
    html = f"<{tag}"

    for key, value in attributes.items():
        html = html + f" {key}='{value}'"

    html = html + f">{text}</{tag}>"
    return html

print(create_html('p', 'Ini teks'))
print(create_html('a', 'Ini link', href='www.google.com', style='link')) #cara panggil keyword