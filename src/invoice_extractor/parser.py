"""Parser contracts.

Implementation should be added step by step after notebook/lab exploration.
"""

from pathlib import Path
from typing import Iterable

import pdfplumber

from invoice_extractor.schemas import InvoiceExtraction
from invoice_extractor.templates import SUPERSTORE_REGIONS, InvoiceTemplate


def iter_invoice_paths(folder: Path) -> list[Path]:
    """Return PDF paths from a folder in stable order."""
    return sorted(path for path in folder.glob("*.pdf") if path.is_file())


def parse_batch(
    paths: Iterable[Path],
    template: InvoiceTemplate = SUPERSTORE_REGIONS,
) -> list[InvoiceExtraction]:
    """Parse many PDFs.

    TODO: Decide whether batch should continue on all errors or stop on fatal
    template/configuration errors.
    """
    return [parse_invoice(path, template) for path in paths]


def parse_invoice(
    path: Path,
    template: InvoiceTemplate = SUPERSTORE_REGIONS,
) -> InvoiceExtraction:
    """Parse one PDF.

    TODO:
    - open PDF with pdfplumber;
    - check page size against `template.expected_page_size`;
    - crop named regions from `template.regions`;
    - extract words/tables from those regions;
    - return `InvoiceExtraction`.
    """

    with pdfplumber.open(path) as pdf:
        page = pdf.pages[0]
        page_size = (page.width, page.height)
        if page_size == template.expected_page_size:
            print("page have expected size.")

            cropped_end_extracted = {
                name: page.crop(
                    (min(r.vlines), min(r.hlines), max(r.vlines), max(r.hlines))
                ).extract_table(
                    {
                        "vertical_strategy": "explicit",
                        "horizontal_strategy": "explicit",
                        "explicit_vertical_lines": list(r.vlines),
                        "explicit_horizontal_lines": list(r.hlines),
                    }
                )
                for name, r in template.regions.items()
            }
            print(cropped_end_extracted)
        else:
            print("not same size")
    raise NotImplementedError(
        "parse_invoice is intentionally left for step-by-step implementation."
    )
