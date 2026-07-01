"""Data contracts for invoice extraction."""

from datetime import date

from pydantic import BaseModel


class InvoiceRaport(BaseModel):
    pass


class InvoiceRow(BaseModel):
    # from file
    source_file: str
    # region 1 invoice_nr
    invoice_number: str
    # region 2 addresses
    bill_to: str
    ship_to: str
    # region 3 metadata
    invoice_date: date
    ship_mode: str
    balance_due: float | None
    # region 5 summary
    subtotal: float | None
    discount: float | None
    shipping: float | None
    total: float | None
    # region 6 notes_terms
    notes: str | None
    order_id: str | None


class LineItemRow(BaseModel):
    # nazwa pliku
    source_file: str
    # region 4
    invoice_number: str
    row_no: int
    item: str
    quantity: float | None
    rate: float | None
    amount: float | None


class InvoiceExtraction(BaseModel):
    invoice: InvoiceRow
    line_items: list[LineItemRow]
