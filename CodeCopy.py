from Classes.Terminal_Commands import Terminal
from Classes.PopupWindows import PopupWindows


def on_special_copy():

    from_clipboard = Terminal.pull_from_clipboard()

    if check_char_count(from_clipboard) is True:
        from_clipboard = "<code> \n" + from_clipboard + "\n </code>"
        from_clipboard = '<br />\n'.join(from_clipboard.split("\n"))
        Terminal.push_to_clipboard(from_clipboard)
    else:
        create_popup_edit(from_clipboard)


def check_char_count(input):

    count = len(input)

    if count < 4000:
        return False
    else:
        return False


def create_popup_edit(input):
    popup = PopupWindows(input)
    window = popup.create_window()
    window.setTitle("Test")
    window.show()


on_special_copy()
