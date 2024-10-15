from document import Document
from caretaker import Caretaker

if __name__ == "__main__":

    doc = Document()
    caretaker = Caretaker()

    doc.set_content("Version 1")
    caretaker.save_state(doc)

    doc.set_content("Version 2")
    caretaker.save_state(doc)

    doc.set_content("Version 3")
    print(doc.get_content())

    caretaker.restore_state(doc)
    print(doc.get_content())

    caretaker.restore_state(doc)
    print(doc.get_content())
