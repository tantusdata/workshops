import numpy

from commons import CSVBucketingWriter

N_ROWS_PER_FILE = 1_000_000
N_ROWS_TOTAL = 1_000


def generate_price() -> float:
    return int(numpy.random.default_rng().uniform(low=1, high=10_000)) / 100.0


def generate_unit() -> str:
    return str(numpy.random.default_rng().choice(["kg", "m", "m2", "m3", ""], 1)[0])


COLUMNS = ["product_id", "price", "unit"]

if __name__ == "__main__":
    final_buckets = CSVBucketingWriter(N_ROWS_PER_FILE, "../data/products/products", COLUMNS)

    for row_index in range(N_ROWS_TOTAL):
        row = {
            "product_id": row_index,
            "price": generate_price(),
            "unit": generate_unit()
        }

        final_buckets.write(row)

    final_buckets.flush()
