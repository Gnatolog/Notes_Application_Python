from Controller import TextArea
from Mod import Note
from Mod import Function


def start_application():
    functions = Function.Function()
    TextArea.change_print_text("start")

    while True:
        TextArea.change_print_text("choice")
        TextArea.change_print_text("menu")
        choice = TextArea.change_print_text("action")
        print()
        if choice.isdigit():
            match choice:
                case "1":
                    functions.save()
                    TextArea.change_print_text("save")

                case "2":
                    if len(functions.read()) != 0:
                        for i in functions.read():
                            print(i)
                        TextArea.change_print_text("read")
                    else:
                        TextArea.change_print_text('not')

                case "3":
                    title = TextArea.change_print_text('title')
                    body = TextArea.change_print_text('body')
                    notion = Note.Note(title, body)
                    functions.add(notion)
                    TextArea.change_print_text("add")

                case "4":
                    id_note = TextArea.change_print_text('note_edit')
                    if id_note.isdigit():
                        title = TextArea.change_print_text('title')
                        body = TextArea.change_print_text('body')
                        if functions.edit(int(id_note), title, body) is not None:
                            TextArea.change_print_text("edit")
                        else:
                            TextArea.change_print_text("not_found")
                    else:
                        TextArea.change_print_text("error")

                case "5":
                    id_note = TextArea.change_print_text('note_del')
                    if id_note.isdigit():
                        if functions.delite(int(id_note)) is not None:
                            TextArea.change_print_text("del")
                        else:
                            TextArea.change_print_text("not_found")

                case "6":
                    answer = TextArea.change_print_text('warning')
                    if answer.lower() == "y":
                        functions.save()
                        TextArea.change_print_text('save')
                        TextArea.change_print_text("exit")
                    else:
                        TextArea.change_print_text("exit")
                    break
        else:
            TextArea.change_print_text("error")
