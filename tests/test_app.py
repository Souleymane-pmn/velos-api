from app import app

def test_sante_repond_ok():
    client = app.test_client()
    reponse = client.get("/sante")
    assert reponse.status_code == 200

def test_alertes_sans_base():
    client = app.test_client()
    donnees = client.get("/alertes").get_json()
    assert donnees["source"] == "memoire"
    assert all(s["velos_disponibles"] <= 2 for s in donnees["alertes"])
