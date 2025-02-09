from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
import logging
import warnings


class Countries(APIClassTemplate):
    """
    The Countries Object in the FMC.
    """

    VALID_JSON_DATA = ["id", "name", "iso2", "iso3"]
    VALID_FOR_KWARGS = VALID_JSON_DATA + []
    URL_SUFFIX = "/object/countries"
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for Countries class.")
        self.parse_kwargs(**kwargs)
        self.type = "Country"

    def post(self):
        logging.info("POST method for API for Countries not supported.")
        pass

    def put(self):
        logging.info("PUT method for API for Countries not supported.")
        pass

    def delete(self):
        logging.info("DELETE method for API for Countries not supported.")
        pass


class Country(Countries):
    """Dispose of this Class after 20210101."""

    def __init__(self, fmc, **kwargs):
        warnings.resetwarnings()
        warnings.warn("Deprecated: Country() should be called via Countries().")
        super().__init__(fmc, **kwargs)
