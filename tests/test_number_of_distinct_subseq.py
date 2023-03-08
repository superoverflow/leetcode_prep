from src.number_of_distinct_subseq import solve

def test_solve_base_case():
    assert 7 == solve("rrlrlr", 6, 1, 2)