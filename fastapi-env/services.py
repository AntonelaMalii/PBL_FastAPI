import sqlalchemy.orm as _orm

import models as _models, schemas as _schemas, database as _database


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_routes_by_nr(db: _orm.Session, route_nr: int):
    return db.query(_models.Routes).filter(_models.Routes.route_nr == route_nr).first()

def get_routes_by_route_id(db: _orm.Session, route_id: int):
    return db.query(_models.RoutesList).filter(_models.RoutesList.route_id == route_id).first()

def get_routes_by_id(db: _orm.Session, id: int):
    return db.query(_models.Routes).filter(_models.Routes.id == id).first()



def create_routes(db: _orm.Session, routes:_schemas.RoutesCreate):
    db_routes=_models.Routes(route_nr=routes.route_nr)
    db.add(db_routes)
    db.commit()
    db.refresh(db_routes)
    return db_routes

def get_routes(db: _orm.Session):
    return db.query(_models.Routes).all()

def get_routeslist(db: _orm.Session, id:int):
    # return db.query(_models.RoutesList).filter(_models.RoutesList.id==id).all()
    return db.query(_models.RoutesList).filter(_models.RoutesList.owner_id == id).all()  


def delete_duplicates(db:_orm.Session, route_id: int):
    db.query(_models.RoutesList).filter(_models.RoutesList.route_id == route_id).delete()
   
def create_routeslist(db: _orm.Session, routeslist:_schemas.RoutesListCreate, id:int):
    db_routeslist=_models.RoutesList(curr_position=routeslist.curr_position, nr_people=routeslist.nr_people,route_id=routeslist.route_id,owner_id=id)
    delete_duplicates(db=db, route_id=routeslist.route_id)
    # if db_routeslist2 :
    #     db.query(_models.RoutesList).filter(_models.RoutesList.id == )
    # #
    db.add(db_routeslist)
    db.commit()
    db.refresh(db_routeslist)
    return db_routeslist


# def create_routes_info(db: _orm.Session,routesinfo:_schemas.RouteInfoCreate, route_id: int, id:int):
#     db_routesinfo= _models.RouteInfo(curr_position=routesinfo.curr_position, nr_people=routesinfo.nr_people, owner_id=route_id, id=id)
#     db.add(db_routesinfo)
#     db.commit()
#     db.refresh(db_routesinfo)
#     return db_routesinfo

# def get_routes_info(db: _orm.Session,  route_id: int):
#     return db.query(_models.RouteInfo).filter(_models.RouteInfo.owner_id == route_id).all()  

def get_routes_by_route_id(db: _orm.Session, route_id: int):
    return db.query(_models.RoutesList).filter(_models.RoutesList.route_id == route_id).first()

def get_routes_by_id(db: _orm.Session, id: int):
    return db.query(_models.Routes).filter(_models.Routes.id == id).first()     
