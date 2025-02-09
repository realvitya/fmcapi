from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
import logging
import warnings


class FTDNatPolicies(APIClassTemplate):
    """
    The FTDNatPolicies Object in the FMC.
    """

    VALID_JSON_DATA = ["id", "name", "type"]
    VALID_FOR_KWARGS = VALID_JSON_DATA + []
    URL_SUFFIX = "/policy/ftdnatpolicies"
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for FTDNatPolicies class.")
        self.parse_kwargs(**kwargs)
        self.type = "FTDNatPolicy"


class FTDNatPolicy(FTDNatPolicies):
    """Dispose of this Class after 20210101."""

    def __init__(self, fmc, **kwargs):
        warnings.resetwarnings()
        warnings.warn(
            "Deprecated: FTDNatPolicy() should be called via FTDNatPolicies()."
        )
        super().__init__(fmc, **kwargs)
