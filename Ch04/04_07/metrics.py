import pandas as pd
import pandera as pa

metrics_scheme = pa.DataFrameSchema({
    "time": pa.Column(pd.DatetimeTZDtype(tz="UTC")),
    "metric": pa.Column(str, checks=pa.Check.isin(["mem", "cpu"])),
    "value": pa.Column(float, checks=pa.Check.greater_than(0)),
})


@pa.check_output(metrics_scheme)
def load_metrics(jsonl_file):
    return pd.read_json(
        jsonl_file,
        orient='records',
        lines=True,
        convert_dates=['time'],
    )


# testing
if __name__ == '__main__':
    from pathlib import Path

    here = Path(__file__).absolute().parent
    jsonl_file = here / 'metrics.jsonl'

    load_metrics(jsonl_file)
