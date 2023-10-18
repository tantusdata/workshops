from __future__ import annotations

import sys
import numpy

import invoice_generator
import products_generator
from commons import CSVBucketingWriter

N_ITEMS_PER_FILE = [1_000, 100_000, 10_000_000]
N_INVOICES = invoice_generator.N_ROWS_TOTAL


def generate_items_for_invoice() -> int:
    if int(numpy.random.default_rng().choice(2, 1, p=[0.999, 0.001])[0]) == 0:
        return int(numpy.random.default_rng().uniform(low=3, high=7))
    else:
        return int(numpy.random.default_rng().uniform(low=1337, high=1804))


def generate_product_id() -> int:
    return int(numpy.random.default_rng().uniform(low=1, high=products_generator.N_TOTAL))


def generate_amount() -> int:
    return int(numpy.random.default_rng().uniform(low=0, high=10))


COLUMNS = ["invoice_id", "invoice_item_index", "product_id", "amount"]

if __name__ == "__main__":
    buckets = [
        CSVBucketingWriter(items_per_file, f"../data/invoices-items/{items_per_file}/invoices-items", COLUMNS) \
        for items_per_file in N_ITEMS_PER_FILE
    ]

    for invoice_id in range(N_INVOICES):
        if invoice_id % 10_000 == 0:
            sys.stderr.write(f"Generating items for invoice {invoice_id:_} of {N_INVOICES:_}...\n")

        items_for_invoice = generate_items_for_invoice()

        first_invoice_item = {
            "invoice_id": invoice_id,
            "invoice_item_index": 0,
            "product_id": 0,
            "amount": generate_amount()
        }

        for bucket in buckets:
            bucket.write(first_invoice_item)

        for invoice_item_index in range(1, 1 + items_for_invoice):
            invoice_item = {
                "invoice_id": invoice_id,
                "invoice_item_index": invoice_item_index,
                "product_id": generate_product_id(),
                "amount": generate_amount()
            }

            for bucket in buckets:
                bucket.write(invoice_item)

    for bucket in buckets:
        bucket.flush()
