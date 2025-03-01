from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
from .ftdnatpolicies import FTDNatPolicies
import logging


class NatRules(APIClassTemplate):
    """
    The NatRules Object in the FMC.
    """

    VALID_JSON_DATA = ["id", "name", "type"]
    VALID_FOR_KWARGS = VALID_JSON_DATA + []
    PREFIX_URL = "/policy/ftdnatpolicies"
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for NatRules class.")
        self.parse_kwargs(**kwargs)

    def nat_policy(self, name):
        logging.debug("In nat_policy() for NatRules class.")
        ftd_nat = FTDNatPolicies(fmc=self.fmc)
        ftd_nat.get(name=name)
        if "id" in ftd_nat.__dict__:
            self.nat_id = ftd_nat.id
            self.URL = (
                f"{self.fmc.configuration_url}{self.PREFIX_URL}/{self.nat_id}/natrules"
            )
            self.nat_added_to_url = True
        else:
            logging.warning(
                f"FTD NAT Policy {name} not found.  Cannot set up NatRules for NAT Policy."
            )

    def post(self):
        logging.info("POST method for API for NatRules not supported.")
        pass

    def put(self):
        logging.info("PUT method for API for NatRules not supported.")
        pass

    def delete(self):
        logging.info("DELETE method for API for NatRules not supported.")
        pass
