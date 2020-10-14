from dataclasses import dataclass


@dataclass
class BusLocation():
    Actual: bool
    BlockNumber: int
    DepartureText: str
    DepartureTime: str
    Description: str
    Gate: str
    Route: int
    RouteDirection: str
    Terminal: str
    VehicleHeading: int
    VehicleLatitude: float
    VehicleLongitude: float


class BusLocationList:

    def __init__(self, bus_location_list, identifier, expiration):
        self.bus_location_list = bus_location_list
        self.identifier = identifier
        self.expiration = expiration


    def next_bus_depart(self):
        if self.bus_location_list:
            return self.bus_location_list[0].DepartureText   # A string like "8 Min or "15:45"
            

