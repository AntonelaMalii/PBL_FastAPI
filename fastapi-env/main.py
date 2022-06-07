import fastapi as _fastapi
from typing import List
import sqlalchemy.orm as _orm
import schemas as _schemas
import services as _services

app= _fastapi.FastAPI()

_services.create_database()


@app.post("/routes/", response_model=_schemas.Routes)

def create_routes(routes: _schemas.RoutesCreate, db:_orm.Session= _fastapi.Depends(_services.get_db)):
    db_routes = _services.get_routes_by_nr(db=db, route_nr=routes.route_nr)
    if db_routes:
        raise _fastapi.HTTPException(
            status_code=400, detail="woops the route already exists"
        )
   
    return _services.create_routes(db=db, routes=routes)

@app.get("/routes/", response_model=List[_schemas.Routes])
def read_routes(db:_orm.Session = _fastapi.Depends(_services.get_db)):
    routes = _services.get_routes(db=db)
    return routes

@app.post("/routes/{id}", response_model=_schemas.RoutesList)
def create_routeslist(id: int, routeslist: _schemas.RoutesListCreate, db:_orm.Session= _fastapi.Depends(_services.get_db)):
    db_routeslist = _services.get_routes_by_id(db=db, id=id)
    if db_routeslist is None:
        raise _fastapi.HTTPException(
            status_code=400, detail="woops this route doesn't exists"
        )

    # db_routeslist2 = _services.get_routes_by_route_id(db=db, route_id=routeslist.route_id)
    # if db_routeslist2 :
    #     raise _fastapi.HTTPException(
    #         status_code=400, detail="woops bus with such inmatriculation nr on this route already exists"
    #     )   
   
    return _services.create_routeslist(db=db, routeslist=routeslist, id=id)


@app.get("/routes/{id}", response_model=List[_schemas.RoutesList])
def read_routes_list(id: int, db:_orm.Session = _fastapi.Depends(_services.get_db)):
    db_routeslist = _services.get_routes_by_id(db=db, id=id)
    if db_routeslist is None:
        raise _fastapi.HTTPException(
            status_code=400, detail="woops this route doesn't exists"
        )
    routeslist = _services.get_routeslist(db=db, id=id)
    return routeslist


# @app.post("/routes/{id}/{route_id}", response_model=_schemas.RouteInfo)

# def create_routes_info(id: int, route_id:int, routeinfo:_schemas.RouteInfoCreate, db:_orm.Session= _fastapi.Depends(_services.get_db)):
  


#     return _services.create_routes_info(db=db, routesinfo=routeinfo,route_id=route_id, id=id)     
  

# @app.get("/routes/{id}/{route_id}", response_model=List[_schemas.RouteInfo])
# def read_routes_info(id: int, route_id:int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
#     db_routesinfos = _services.get_routes_by_id(db=db, id=id)
#     if db_routesinfos is None:
#         raise _fastapi.HTTPException(
#             status_code=400, detail="woops this route doesn't exists"
#         )

#     db_routesinfos2 = _services.get_routes_by_route_id(db=db, route_id=route_id)
#     if db_routesinfos2 is None :
#         raise _fastapi.HTTPException(
#             status_code=400, detail="woops bus with such inmatriculation nr on this route doesnt exists"
#         ) 
         

#     routesinfo = _services.get_routes_info(db=db, route_id=route_id)
#     return routesinfo    


