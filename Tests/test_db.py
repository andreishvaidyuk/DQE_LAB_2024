import pytest
import conftest
import allure


@pytest.mark.smoke
@pytest.mark.parametrize(
    "queries, expected",
    [(q["sql"], q["expected"]) for q in conftest.smoke_tests_queries("config_SQL_example.yaml")]
)
@allure.story("Smoke Test")
def test_smoke_queries(connect_to_db_postgre, queries, expected):
    with connect_to_db_postgre.cursor() as cur:
        cur.execute(queries)
        result = cur.fetchone()[0]
        assert result == expected, "Smoke test failed: Expected some result."


@pytest.mark.parametrize(
    "queries, expected",
    [(q["sql"], q["expected"]) for q in conftest.critical_tests_queries("config_SQL_example.yaml")])
@pytest.mark.critical
@allure.story("Critical Path Test")
def test_critical_queries(connect_to_db_postgre, queries, expected):
    with connect_to_db_postgre.cursor() as cur:
        cur.execute(queries)
        result = cur.fetchone()[0]
        assert result == expected, "Critical path test failed: Invalid result."
