from pydantic import BaseModel


class DeviceBase(BaseModel):
    model: str
    manufacturer_id: int
    mgmt_interface_id: int


