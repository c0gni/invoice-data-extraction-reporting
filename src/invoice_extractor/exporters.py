"""Export contracts for reporting outputs."""

from pathlib import Path

import pandas as pd

from invoice_extractor.schemas import InvoiceExtraction


def export_excel_report(extractions: list[InvoiceExtraction], output_path: Path) -> None:
    """Write Excel report.

    TODO: build sheets from `invoices_frame`, `line_items_frame`,
    `quality_flags_frame`, and `summary_frame`.
    """
    raise NotImplementedError("Excel export is intentionally left for implementation.")


def export_csv_bundle(extractions: list[InvoiceExtraction], output_dir: Path) -> None:
    """Write CSV files for report tables."""
    raise NotImplementedError("CSV export is intentionally left for implementation.")


def invoices_frame(extractions: list[InvoiceExtraction]) -> pd.DataFrame:
    """Build one row per invoice extraction."""
    raise NotImplementedError("Invoice frame mapping is intentionally left for implementation.")


def line_items_frame(extractions: list[InvoiceExtraction]) -> pd.DataFrame:
    """Build one row per line item."""
    raise NotImplementedError("Line-item frame mapping is intentionally left for implementation.")


def quality_flags_frame(extractions: list[InvoiceExtraction]) -> pd.DataFrame:
    """Build one row per quality flag."""
    raise NotImplementedError("Quality flag frame mapping is intentionally left for implementation.")


def summary_frame(extractions: list[InvoiceExtraction]) -> pd.DataFrame:
    """Build batch-level summary metrics."""
    raise NotImplementedError("Summary frame mapping is intentionally left for implementation.")
