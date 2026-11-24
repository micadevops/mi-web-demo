from servidor import responder


def test_raiz_responde_200_con_hola_mundo():
    status, body = responder("/")
    assert status == 200
    assert "Hola mundo" in body


def test_raiz_es_html():
    _, body = responder("/")
    assert "<html" in body.lower()


def test_saludo_con_nombre():
    status, body = responder("/saludo?nombre=Ana")
    assert status == 200
    assert "Hola, Ana" in body


def test_saludo_sin_nombre():
    status, body = responder("/saludo")
    assert status == 200
    assert "Hola, desconocido" in body


def test_saludo_con_query_sin_nombre():
    status, body = responder("/saludo?otro=x")
    assert status == 200
    assert "Hola, desconocido" in body


def test_nombre_se_escapa():
    status, body = responder("/saludo?nombre=<script>")
    assert status == 200
    assert "<script>" not in body
    assert "&lt;script&gt;" in body


def test_nombre_escapado_con_url_encoding():
    _, body = responder("/saludo?nombre=%3Cscript%3Ealert(1)%3C%2Fscript%3E")
    assert "<script>" not in body
    assert "&lt;script&gt;" in body


def test_ruta_desconocida_404():
    status, _ = responder("/otra")
    assert status == 404


def test_ruta_similar_404():
    status, _ = responder("/saludo/extra")
    assert status == 404
