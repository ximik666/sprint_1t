from clickhouse_driver import Client
from time import perf_counter
from fastapi import FastAPI
from time import perf_counter
app = FastAPI()


def connect_to_db():
    try:
        client = Client('ip', user='user', port=9001,
                        password='password', secure=False, verify=False, database='database')
        result = client.execute(
            'select count(*) from database.mdl_logstore_standard_log;')
        return [True, client]
    except:
        return [False]


@app.get("/user/total/{day}")
def user_count(day: int = 5):
    """Функция принимает количество дней, а возвращает общее число пользователей, которые заходили на сайт за эти дни"""
    client = connect_to_db()
    if client[0]:
        start_time = perf_counter()
        result = client[1].execute(
            f'SELECT count(distinct userid) FROM database.mdl_logstore_standard_log where FROM_UNIXTIME(timecreated)>now()-{day*24*60*60} limit {day}')
        return {"answer": result[0][0], "time": perf_counter()-start_time}
    else:
        return {"error": "Database connect"}


@app.get("/ip/{day}")
def ip_count(day: int = 5):
    """Функция принимает количество дней, а возвращает общее число ip адресов, которые заходили на сайт за эти дни"""
    client = connect_to_db()
    if client[0]:
        start_time = perf_counter()
        result = client[1].execute(
            f'SELECT count(distinct ip) FROM database.mdl_logstore_standard_log where FROM_UNIXTIME(timecreated)>now()-{day*24*60*60} limit {day}')
        return {"answer": result[0][0], "time": perf_counter()-start_time}
    else:
        return {"error": "Database connect"}


@app.get("/course/activity/{day}")
def activity_count(day: int = 5):
    """Функция принимает количество дней, а возвращает общее число активных курсов, которые заходили на сайт за эти дни"""
    client = connect_to_db()
    if client[0]:
        start_time = perf_counter()
        result = client[1].execute(
            f'SELECT count(distinct courseid) FROM database.mdl_logstore_standard_log where FROM_UNIXTIME(timecreated)>now()-{day*24*60*60}')
        return {"answer": result[0][0], "time": perf_counter()-start_time}
    else:
        return {"error": "Database connect"}


@app.get("/course/top/{day}/{limit}")
def course_top(day: int = 5, limit: int = 5):
    """Функция принимает количество дней и лимиты, а возвращает id курса и количество его активностей за эти дни"""
    client = connect_to_db()
    if client[0]:
        start_time = perf_counter()
        result = client[1].execute(
            f'SELECT courseid id_course, count(*) view FROM database.mdl_logstore_standard_log where (FROM_UNIXTIME(timecreated)>now()-{day*24*60*60} and courseid!=0) group by courseid order by view desc limit {limit}')
        return {"answer": result, "time": perf_counter()-start_time}
    else:
        return {"error": "Database connect"}


@app.get("/course/user/{day}/{limit}")
def course_user(day: int = 5, limit: int = 5):
    """Функция принимает количество дней и лимиты, а возвращает id пользователя и количество его активностей за эти дни"""
    client = connect_to_db()
    if client[0]:
        start_time = perf_counter()
        result = client[1].execute(
            f'SELECT userid, count(*) view FROM database.mdl_logstore_standard_log where (FROM_UNIXTIME(timecreated)>now()-{day*24*60*60} and userid>2) group by userid order by view desc limit {limit}')
        return {"answer": result, "time": perf_counter()-start_time}
    else:
        return {"error": "Database connect"}


@app.get("/activity/time/{day}}")
def user_count(day: int = 5):
    """Функция принимает количество дней, а возвращает сгруппированное по дням и часам количество посещений"""
    client = connect_to_db()
    if client[0]:
        start_time = perf_counter()
        result = client[1].execute(
            f'select * from (SELECT toHour(time) AS hour, toDayOfMonth(time) AS day, count() FROM default.log where time>now()-{day}*24*60*60 and time is not null GROUP BY hour, day WITH ROLLUP order by day,hour) where day!=0;')
        return {"answer": result, "time": perf_counter()-start_time}
    else:
        return {"error": "Database connect"}
