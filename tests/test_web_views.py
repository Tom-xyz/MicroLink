from src.web.views import index

def test_index_success():
    result = index()
    assert result.status_code == 200
    assert result.media_type == "text/html"
