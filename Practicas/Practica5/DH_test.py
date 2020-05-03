from DH import Participant

def test_exchange():
    p, g = 103, 78
    A, B = Participant(p, g, None), Participant(p, g, None)
    A.participant = B
    B.participant = A
    keyA = A.exchange()
    assert keyA == B.exchange()
