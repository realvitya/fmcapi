from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
import logging


class FilePolicies(APIClassTemplate):
    """
    The File Policy Object in the FMC.
    """

    VALID_JSON_DATA = ["id", "name"]
    VALID_FOR_KWARGS = VALID_JSON_DATA + []
    URL_SUFFIX = "/policy/filepolicies"

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for FilePolicies class.")
        self.parse_kwargs(**kwargs)

    def post(self):
        logging.info("POST method for API for FilePolicies not supported.")
        pass

    def put(self):
        logging.info("PUT method for API for FilePolicies not supported.")
        pass

    def delete(self):
        logging.info("DELETE method for API for FilePolicies not supported.")
        pass
