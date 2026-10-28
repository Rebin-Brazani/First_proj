from app import app

client = app.test_client()
def test_owner_can_still_read_their_own_record() :
    r = client.get("/grades?student=4822")
    assert r. status_code == 200
    assert b"Rebin" in r.data

def test_other_students_record_is_refused () :
    r = client.get("/grades?student=4823")
    assert r.status_code == 403
    assert b"Sara" not in r.data