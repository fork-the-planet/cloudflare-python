# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DNSSEC"]


class DNSSEC(BaseModel):
    algorithm: Optional[str] = None
    """Algorithm key code."""

    digest: Optional[str] = None
    """Digest hash."""

    digest_algorithm: Optional[str] = None
    """Type of digest algorithm."""

    digest_type: Optional[str] = None
    """Coded type for digest algorithm."""

    dnssec_multi_signer: Optional[bool] = None
    """
    If true, multi-signer DNSSEC is enabled on the zone, allowing multiple providers
    to serve a DNSSEC-signed zone at the same time. This is required for DNSKEY
    records (except those automatically generated by Cloudflare) to be added to the
    zone.

    See
    [Multi-signer DNSSEC](https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/)
    for details.
    """

    dnssec_presigned: Optional[bool] = None
    """
    If true, allows Cloudflare to transfer in a DNSSEC-signed zone including
    signatures from an external provider, without requiring Cloudflare to sign any
    records on the fly.

    Note that this feature has some limitations. See
    [Cloudflare as Secondary](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/#dnssec)
    for details.
    """

    dnssec_use_nsec3: Optional[bool] = None
    """
    If true, enables the use of NSEC3 together with DNSSEC on the zone. Combined
    with setting dnssec_presigned to true, this enables the use of NSEC3 records
    when transferring in from an external provider. If dnssec_presigned is instead
    set to false (default), NSEC3 records will be generated and signed at request
    time.

    See
    [DNSSEC with NSEC3](https://developers.cloudflare.com/dns/dnssec/enable-nsec3/)
    for details.
    """

    ds: Optional[str] = None
    """Full DS record."""

    flags: Optional[float] = None
    """Flag for DNSSEC record."""

    key_tag: Optional[float] = None
    """Code for key tag."""

    key_type: Optional[str] = None
    """Algorithm key type."""

    modified_on: Optional[datetime] = None
    """When DNSSEC was last modified."""

    public_key: Optional[str] = None
    """Public key for DS record."""

    status: Optional[Literal["active", "pending", "disabled", "pending-disabled", "error"]] = None
    """
    Status of DNSSEC, based on user-desired state and presence of necessary records.
    """
