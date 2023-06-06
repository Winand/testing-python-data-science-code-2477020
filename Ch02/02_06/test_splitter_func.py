import pytest
import yaml
from splitter import split_to_chunks


def param_cases():
    with open("Ch02/02_06/split_cases.yml") as f:
        for i in yaml.safe_load(f):
            yield i["size"], i["chunk_size"], i["chunks"]


def test_splitter_func(cases: list):
    for i in cases:
        sz = i["size"]
        ch_sz = i["chunk_size"]
        assert [list(i) for i in split_to_chunks(sz, ch_sz)] == i["chunks"]


@pytest.mark.parametrize("size, chunk_size, chunks", param_cases())
def test_splitter_func2(size, chunk_size, chunks):
    assert [list(i) for i in split_to_chunks(size, chunk_size)] == chunks
