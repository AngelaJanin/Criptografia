import base64

base64_string = b'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'
with open("pinkThing.png", "wb") as oh_no:
    oh_no.write(base64.decodebytes(base64_string))