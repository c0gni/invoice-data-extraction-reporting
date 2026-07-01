"""Layout configuration for known invoice formats."""

from dataclasses import dataclass

Number = int | float


@dataclass(frozen=True)
class RegionSpec:
    """Named area on a PDF page.

    This is only geometry/configuration. It does not parse anything.
    """

    name: str
    vlines: tuple[Number, ...]
    hlines: tuple[Number, ...]
    columns: tuple[str, ...] = ()

    @property
    def bbox(self) -> tuple[Number, Number, Number, Number]:
        """Return `(x0, top, x1, bottom)` for `page.crop(...)`."""
        return (self.vlines[0], self.hlines[0], self.vlines[-1], self.hlines[-1])


@dataclass(frozen=True)
class InvoiceTemplate:
    """Configuration for one known invoice layout."""

    template_id: str
    expected_page_size: tuple[Number, Number]
    regions: dict[str, RegionSpec]

    def region(self, name: str) -> RegionSpec:
        return self.regions[name]


SUPERSTORE_REGIONS = InvoiceTemplate(
    template_id="superstore_v1",
    expected_page_size=(612, 792),
    regions={
        "invoice_nr": RegionSpec(
            name="invoice_nr",
            vlines=(530, 580),
            hlines=(56, 75),
        ),
        "addresses": RegionSpec(
            name="addresses",
            vlines=(43, 138, 288),
            hlines=(113, 135, 176),
            columns=("bill_to", "ship_to"),
        ),
        "meta": RegionSpec(
            name="meta",
            vlines=(387, 485, 585),
            hlines=(105, 125, 145, 170),
        ),
        "items": RegionSpec(
            name="items",
            vlines=(42.2, 368.8, 430.5, 523.0, 580),
            hlines=(213, 246),
            columns=("item", "quantity", "rate", "amount"),
        ),
        "summary": RegionSpec(
            name="summary",
            vlines=(370, 485, 580),
            hlines=(320, 344, 365, 390, 412),
        ),
        "notes_terms": RegionSpec(
            name="notes_terms",
            vlines=(41, 225),
            hlines=(437, 485, 520),
        ),
    },
)
