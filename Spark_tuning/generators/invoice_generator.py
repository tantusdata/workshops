import datetime
import numpy

from commons import DATE_LAST, CSVBucketingWriter

N_ROWS_PER_FILE = 1_000_000
N_ROWS_TOTAL = 10_000_000


def generate_client_id() -> int:
    return int(numpy.random.default_rng().exponential(scale=100))


def generate_store_id() -> int:
    return int(numpy.random.default_rng().uniform(low=1, high=10_000))


def generate_chain_id() -> int:
    return int(numpy.random.default_rng().uniform(low=1, high=10))


COLUMNS = ["invoice_id", "client_id", "store_id", "chain_id", "issue_date"]

if __name__ == "__main__":
    final_buckets = CSVBucketingWriter(N_ROWS_PER_FILE, "../data/invoices/invoices", COLUMNS)

    for row_index in range(N_ROWS_TOTAL):
        row = {
            "invoice_id": row_index,
            "client_id": generate_client_id(),
            "store_id": generate_store_id(),
            "chain_id": generate_chain_id(),
            "issue_date": (DATE_LAST - datetime.timedelta(minutes=row_index))
        }

        final_buckets.write(row)

    final_buckets.flush()
