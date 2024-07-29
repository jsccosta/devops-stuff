from reportlab.pdfbase.pdfmetrics import stringWidth


def wrap_text(c, text, width, font_name, font_size):
    """
    Wraps text to fit within a specified width by breaking it into lines.
    
    Parameters:
    - c: The canvas instance from reportlab on which text will be drawn.
    - text (str): The text string to be wrapped.
    - width (int): The maximum width allowed for the text, in points.
    - font_name (str): The name of the font to be used.
    - font_size (int): The size of the font to be used.
    
    Returns:
    - list: A list of strings, where each string represents a line of wrapped text.
    """

    c.setFont(font_name, font_size)
    wrapped_lines = []
    words = text.split()
    current_line = ''
    for word in words:
        if stringWidth(current_line + ' ' + word, font_name, font_size) < width:
            current_line += ' ' + word if current_line else word
        else:
            wrapped_lines.append(current_line)
            current_line = word
    if current_line:
        wrapped_lines.append(current_line)

    return wrapped_lines


def add_text_to_page(c, text, font_name="Helvetica", font_size=10, start_y=750, margin=50):
    """
    Adds text to a reportlab canvas page with automatic line wrapping.

    This function utilizes wrap_text to ensure text fits within a specified width
    and then draws the wrapped text onto the canvas, creating new pages as necessary.

    Parameters:
    - c: The canvas instance from reportlab where the text will be drawn.
    - text (str): The text content to be added to the canvas.
    - font_name (str): The font name to be used for the text.
    - font_size (int): The font size to be used for the text.
    - start_y (int): The starting y-coordinate from the top of the page to start drawing text.
    - margin (int): The left and right margin size, used to calculate text width.

    Returns:
    - None
    """

    page_width = 612  # Default width for letter size
    bottom_margin = 50  # Example margin
    line_height = 12  # Example line height
    text_width = page_width - (margin * 2)
    wrapped_lines = wrap_text(c, text, text_width, font_name, font_size)
    y = start_y
    for line in wrapped_lines:
        if y < bottom_margin:
            c.showPage()
            y = start_y
        c.drawString(margin, y, line)
        y -= line_height
