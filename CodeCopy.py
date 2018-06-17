from Classes.Terminal_Commands import Terminal


def on_special_copy():

    from_clipboard = Terminal.pull_from_clipboard()
    from_clipboard = "<code> \n" + from_clipboard + "\n </code>"
    from_clipboard = '<br />\n'.join(from_clipboard.split("\n"))
    Terminal.push_to_clipboard(from_clipboard)


on_special_copy()
