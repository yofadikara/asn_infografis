import argparse
from automation.pipeline import run_pipeline
from automation.filter import get_instansi_filter

if __name__ == "__main__":
    args = get_instansi_filter()
    result = run_pipeline(args)
    print(result)