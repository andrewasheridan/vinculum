"""Exceptions."""


class TenuisAPIError(Exception):
    """Base class for all Tenuis API exceptions."""


class ServiceError(TenuisAPIError):
    """Base class for `Service` related exceptions."""
