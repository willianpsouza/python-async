'''CARREGANDO MODULOS'''
import os

from multiprocessing import Process, Queue

from contextlib import asynccontextmanager


from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, constr

import uvicorn

import psycopg
from psycopg_pool import ConnectionPool, AsyncConnectionPool
from psycopg import sql as SQLQuery

def_queue = Queue(maxsize=8192)

BASEURI = "/performance"
API_VERSION = "v1"


class User(BaseModel):
    '''BASIC USER INFORMATION'''
    id: constr(max_length=32, min_length=32)
    index: int
    guid: constr(max_length=36, min_length=36)
    isActive: bool
    balance: float
    picture: str
    age: int
    name: str
    gender: str
    company: str
    email: str


class SearchUser(BaseModel):
    '''BASIC USER INFORMATION'''
    id: constr(max_length=32, min_length=32)


def data():
    '''test response'''
    return {
        "id": "63cac1995b68566eb1e85fd3",
        "index": 0,
        "guid": "dd182962-cbde-4749-aa34-ab2c9a9383e6",
        "isActive": True,
        "balance": 1988.02,
        "picture": "http://placehold.it/32x32",
        "age": 39,
        "name": "Clay Douglas",
        "gender": "male",
        "company": "ELECTONIC",
        "email": "claydouglas@electonic.com",
    }


def stdConnection():
    dbserver = os.getenv('DBHOST', '192.168.124.28')
    dbname = 'postgres'
    dbuser = 'postgres'
    dbpass = 'meni4na6'

    connstring = "dbname=%s user=%s password=%s host=%s" % (dbname, dbuser, dbpass, dbserver)
    connection = psycopg.connect(connstring)
    return connection


def stdConnectionPool():
    '''connection pool'''
    dbserver = os.getenv('DBHOST', '192.168.124.28')
    dbname = 'postgres'
    dbuser = 'postgres'
    dbpass = 'meni4na6'
    connstring = "postgresql://%s:%s@%s/%s" %(dbuser, dbpass, dbserver, dbname)
    pool = ConnectionPool(conninfo=connstring, min_size=8, max_size=64, max_idle=60, num_workers=8, open=True)
    return pool


def stdConnectionAsyncPool():
    '''connection pool'''
    dbserver = os.getenv('DBHOST', '192.168.124.28')
    dbname = 'postgres'
    dbuser = 'postgres'
    dbpass = 'meni4na6'
    connstring = "postgresql://%s:%s@%s/%s" % (dbuser, dbpass, dbserver, dbname)
    pool = AsyncConnectionPool(conninfo=connstring, min_size=8, max_size=64, max_idle=60, num_workers=8, open=True)
    return pool


def sub_process_add_user(queue: Queue):
    '''connection pool with sub process'''
    pool = stdConnectionPool()
    sql = "INSERT INTO public.user_info \
(uif_id, uif_index, uif_gid, uif_isactive, uif_balance, uif_picture, uif_age, uif_name, uif_gender, uif_company, uif_email, uif_date_add) \
VALUES(%s, %s, %s, %b, %s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP);"

    while True:
        d = queue.get()
        if d:
            with pool.connection() as conn:
                with conn.cursor() as cursor:
                    try:
                        cursor.execute(sql, (d.id, d.index, d.guid, d.isActive, d.balance, d.picture, d.age, d.name, d.gender, d.company, d.email))
                        conn.commit()
                    except Exception as e:
                        print(f"Error 1001: {sql} {e}")


async def sub_def_add_user(async_pool, user):
    '''connection pool'''
    sql = "INSERT INTO public.user_info \
(uif_id, uif_index, uif_gid, uif_isactive, uif_balance, uif_picture, uif_age, uif_name, uif_gender, uif_company, uif_email, uif_date_add) \
VALUES(%s, %s, %s, %b, %s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP) RETURNING uif_id;"
            
    async with async_pool.connection() as conn:
        async with conn.cursor() as cursor:
            try:
                await cursor.execute(sql, (user.id, user.index, user.guid, user.isActive, user.balance, user.picture, user.age, user.name, user.gender, user.company, user.email))
                await conn.commit()
                dados = await cursor.fetchone()
                return dados[0]
            except Exception as e:
                print(f"Error 1001: {sql} {e}")


async def sub_def_select_user(async_pool, user):
    '''connection pool'''
    ret = []
    sql = "SELECT uif_id, uif_index, uif_gid, uif_isactive, uif_balance, uif_picture, uif_age, uif_name, uif_gender, uif_company, uif_email, uif_date_add FROM public.user_info"
    sql_extra = f"{sql} WHERE uif_id = %s;"
    user_id = user.id
    sql_extra = SQLQuery.SQL(sql_extra).format([user_id])

    async with async_pool.connection() as conn:
        async with conn.cursor() as cursor:
            try:
                await cursor.execute(sql_extra, (user_id,))
                dados = await cursor.fetchall()
                for rec in dados:
                    ret.append({
                        "uif_id": rec[0],
                        "uif_index": rec[1],
                        "uif_gid": rec[2],
                        "uif_isactive": rec[3],
                        "uif_balance": rec[4],
                        "uif_picture": rec[5],
                        "uif_age": rec[6],
                        "uif_name": rec[7],
                        "uif_gender": rec[8]
                    })
                return ret
            except Exception as e:
                print(f"Error 1001: {sql} {e}")


async def sub_def_select_report(async_pool):
    '''connection pool'''
    ret = []
    sql = "select count(*) as dd,uif_age  from user_info  group by 2 order by 2;"
    #sql_extra = f"{sql} WHERE uif_id = %s;"
    #user_id = user.id
    #sql_extra = SQLQuery.SQL(sql_extra).format([user_id])

    async with async_pool.connection() as conn:
        async with conn.cursor() as cursor:
            try:
                await cursor.execute(sql, ())
                dados = await cursor.fetchall()
                for rec in dados:
                    ret.append({
                        "total": rec[0],
                        "age": rec[1],
                    })
                return ret
            except Exception as e:
                print(f"Error 1001: {sql} {e}")

async def sub_def_update_user(async_pool, user):
    '''connection pool'''
    sql = "UPDATE public.user_info SET uif_date_add = current_date"
    sql_extra = f"{sql} WHERE uif_id = %s;"
    user_id = user.id
    sql_extra = SQLQuery.SQL(sql_extra).format([user_id])
    async with async_pool.connection() as conn:
        async with conn.cursor() as cursor:
            try:
                await cursor.execute(sql_extra, (user_id,))
                await conn.commit()
                return cursor.rowcount
            except Exception as e:
                print(f"Error 1001: {sql} {e}")


async def sub_def_delete_user(async_pool, user):
    '''connection pool'''
    sql = "DELETE FROM public.user_info "
    sql_extra = f"{sql} WHERE uif_id = %s;"
    user_id = user.id
    sql_extra = SQLQuery.SQL(sql_extra).format([user_id])
    async with async_pool.connection() as conn:
        async with conn.cursor() as cursor:
            try:
                await cursor.execute(sql_extra, (user_id,))
                await conn.commit()
                return cursor.rowcount
            except Exception as e:
                print(f"Error 1001: {sql} {e}")



def default_respose(content):
    '''default response'''
    return JSONResponse(content=content)


async def sent_to_queue(data):
    def_queue.put(data)


@asynccontextmanager
async def dbConnection(app: FastAPI):
    app.conn_async = stdConnectionAsyncPool()
    yield
    await app.conn_async.close()


app = FastAPI(lifespan=dbConnection)


@app.put(f"{BASEURI}/{API_VERSION}/add_user")
async def add_user(user: User, request: Request):
    '''validando ususario'''
    #def_queue.put(user)
    #await sent_to_queue(user)   
    dados = await sub_def_add_user(request.app.conn_async, user)
    return default_respose({'status': True, 'data': dados})


@app.post(f"{BASEURI}/{API_VERSION}/get_user")
async def select_user(user: SearchUser, request: Request):
    '''recuperando usuario ususario'''
    dados = await sub_def_select_user(request.app.conn_async, user)
    return default_respose({'status': True, 'data': dados})


@app.patch(f"{BASEURI}/{API_VERSION}/update_user")
async def update_user(user: SearchUser, request: Request):
    '''recuperando usuario ususario'''
    dados = await sub_def_update_user(request.app.conn_async, user)
    return default_respose({'status': True, 'data': dados})


@app.delete(f"{BASEURI}/{API_VERSION}/delete_user")
async def delete_user(user: SearchUser, request: Request):
    '''recuperando usuario ususario'''
    dados = await sub_def_delete_user(request.app.conn_async, user)
    return default_respose({'status': True, 'data': dados})

@app.get(f"{BASEURI}/{API_VERSION}/get_report")
async def get_report(request: Request):
    '''recuperando report'''
    dados = await sub_def_select_report(request.app.conn_async,)
    return default_respose({'status': True, 'data': dados})



if __name__ == "__main__":
    p = Process(target=sub_process_add_user, args=(def_queue,), daemon=True)
    p.start()
    uvicorn.run(app=app, log_level=None)