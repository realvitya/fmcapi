from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
import logging
import warnings


class Continents(APIClassTemplate):
    """
    The Continents Object in the FMC.
    """

    VALID_JSON_DATA = ["id", "name", "countries"]
    VALID_FOR_KWARGS = VALID_JSON_DATA + []
    URL_SUFFIX = "/object/continents"
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for Continents class.")
        self.parse_kwargs(**kwargs)
        self.type = "Continent"

    def post(self):
        logging.info("POST method for API for Continents not supported.")
        pass

    def put(self):
        logging.info("PUT method for API for Continents not supported.")
        pass

    def delete(self):
        logging.info("DELETE method for API for Continents not supported.")
        pass


class Continent(Continents):
    """Dispose of this Class after 20210101."""

    def __init__(self, fmc, **kwargs):
        warnings.resetwarnings()
        warnings.warn("Deprecated: Continent() should be called via Continents().")
        super().__init__(fmc, **kwargs)
