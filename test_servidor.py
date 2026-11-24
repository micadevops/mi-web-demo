from servidor import responder


def test_raiz_200_hola_mundo():
    status, cuerpo = responder("/")
    assert status == 200
    assert "Hola mundo" in cuerpo
    assert "<html" in cuerpo.lower()


def test_saludo_con_nombre():
    status, cuerpo = responder("/saludo?nombre=Ana")
    assert status == 200
    assert "Hola, Ana" in cuerpo


def test_saludo_sin_nombre():
    status, cuerpo = responder("/saludo")
    assert status == 200
    assert "Hola, desconocido" in cuerpo


def test_saludo_con_query_sin_nombre():
    status, cuerpo = responder("/saludo?otro=x")
    assert status == 200
    assert "Hola, desconocido" in cuerpo


def test_nombre_se_escapa():
    status, cuerpo = responder("/saludo?nombre=<script>")
    assert status == 200
    assert "<script>" not in cuerpo
    assert "&lt;script&gt;" in cuerpo


def test_nombre_escapado_con_alert():
    _, cuerpo = responder("/saludo?nombre=<script>alert(1)</script>")
    assert "<script>" not in cuerpo
    assert "</script>" not in cuerpo


def test_ruta_desconocida_404():
    status, _ = responder("/otra")
    assert status == 404


def test_ruta_desconocida_con_query_404():
    status, _ = responder("/nada?nombre=Ana")
    assert status == 404
