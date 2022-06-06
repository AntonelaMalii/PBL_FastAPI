import pydantic as _pydantic
import datetime as _dt
from typing import List

class _RoutesListBase(_pydantic.BaseModel):
    route_id: int
    curr_position: str
    nr_people : int
    

class RoutesListCreate(_RoutesListBase):
    pass

class RoutesList(_RoutesListBase):
    id: int
    owner_id: int
    timestamp: _dt.datetime
    

    class Config:
        orm_mode = True


class _RoutesBase(_pydantic.BaseModel):
    route_nr: int
    

class RoutesCreate(_RoutesBase):
    pass

class Routes(_RoutesBase):
    id: int
    # add_info: str
    route_info:List[RoutesList] = []

    class Config:
        orm_mode = True



