from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
from .ftddevicehapairs import FTDDeviceHAPairs
import logging
import warnings


class MonitoredInterfaces(APIClassTemplate):
    """
    The MonitoredInterfaces Object in the FMC.
    """

    VALID_JSON_DATA = [
        "id",
        "name",
        "ipv4Configuration",
        "ipv6Configuration",
        "monitorForFailures",
    ]
    VALID_FOR_KWARGS = VALID_JSON_DATA + ["ha_name"]
    PREFIX_URL = "/devicehapairs/ftddevicehapairs"
    REQUIRED_FOR_PUT = ["id"]

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for MonitoredInterfaces class.")
        self.parse_kwargs(**kwargs)

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for MonitoredInterfaces class.")
        if "ha_name" in kwargs:
            self.device_ha(ha_name=kwargs["ha_name"])

    def device_ha(self, ha_name):
        logging.debug("In device_ha() for MonitoredInterfaces class.")
        deviceha1 = FTDDeviceHAPairs(fmc=self.fmc, name=ha_name)
        deviceha1.get()
        if "id" in deviceha1.__dict__:
            self.deviceha_id = deviceha1.id
            self.URL = f"{self.fmc.configuration_url}{self.PREFIX_URL}/{self.deviceha_id}/monitoredinterfaces"
            self.deviceha_added_to_url = True
        else:
            logging.warning(
                f"Device HA {ha_name} not found.  Cannot set up device for MonitoredInterfaces."
            )

    def ipv4(self, ipv4addr, ipv4mask, ipv4standbyaddr):
        logging.debug("In ipv4() for MonitoredInterfaces class.")
        self.ipv4Configuration = {
            "activeIPv4Address": ipv4addr,
            "activeIPv4Mask": ipv4mask,
            "standbyIPv4Address": ipv4standbyaddr,
        }

    def post(self):
        logging.info("POST method for API for MonitoredInterfaces not supported.")
        pass


class DeviceHAMonitoredInterfaces(MonitoredInterfaces):
    """Dispose of this Class after 20210101."""

    def __init__(self, fmc, **kwargs):
        warnings.resetwarnings()
        warnings.warn(
            "Deprecated: DeviceHAMonitoredInterfaces() should be called via MonitoredInterfaces()."
        )
        super().__init__(fmc, **kwargs)
