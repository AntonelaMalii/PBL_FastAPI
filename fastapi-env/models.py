import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import datetime as _dt

import database as _database

class Routes(_database.Base):
    __tablename__ = "routes"
    id = _sql.Column(_sql.Integer, primary_key=True, index= True)
    route_nr = _sql.Column(_sql.Integer)
    # add_info = _sql.Column(_sql.String)
    route_info = _orm.relationship("RoutesList", back_populates="owner")

    
class RoutesList(_database.Base):
    __tablename__ = "routeslist"
    route_id = _sql.Column(_sql.Integer, index= True)
    id = _sql.Column(_sql.Integer, primary_key=True, index= True)
    owner_id=_sql.Column(_sql.Integer, _sql.ForeignKey("routes.id"))
    curr_position = _sql.Column(_sql.String, index=True)
    nr_people = _sql.Column(_sql.Integer, index=True)
    timestamp = _sql.Column(_sql.DateTime, default = _dt.datetime.utcnow)

    owner = _orm.relationship("Routes", back_populates="route_info")
    
    




   
