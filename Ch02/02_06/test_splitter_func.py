from splitter import split_to_chunks

def test_splitter_func(cases: list):
    for i in cases:
        sz = i["size"]
        ch_sz = i["chunk_size"]
        assert [list(i) for i in split_to_chunks(sz, ch_sz)] == i["chunks"]
