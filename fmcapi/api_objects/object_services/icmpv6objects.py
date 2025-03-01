from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
import logging
import warnings


class ICMPv6Objects(APIClassTemplate):
    """
    The ICMPv6Objects Object in the FMC.
    """

    VALID_JSON_DATA = [
        "id",
        "name",
        "type",
        "overrideTargetId",
        "code",
        "icmpType",
        "overrides",
        "overridable",
    ]
    VALID_FOR_KWARGS = VALID_JSON_DATA + []
    URL_SUFFIX = "/object/icmpv6objects"
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for ICMPv6Objects class.")
        self.parse_kwargs(**kwargs)
        self.type = "ICMPV6Object"


class ICMPv6Object(ICMPv6Objects):
    """Dispose of this Class after 20210101."""

    def __init__(self, fmc, **kwargs):
        warnings.resetwarnings()
        warnings.warn(
            "Deprecated: ICMPv6Object() should be called via ICMPv6Objects()."
        )
        super().__init__(fmc, **kwargs)
