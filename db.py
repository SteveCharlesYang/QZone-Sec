import sqlite3
import settings

conn = sqlite3.connect(settings.db_data)
cur = conn.cursor()


def sec_insert(m_id, time_stamp, qq, m_context):
    if if_exist(m_id, time_stamp):
        update_exist(m_id, time_stamp, qq)
    else:
        cur.execute("INSERT INTO " + settings.db_name + " (M_ID,T_STAMP,QQ,CONTENT) \
            VALUES ('" + m_id + "', '" + time_stamp + "', '" + qq + "', '" + m_context + "')")
        conn.commit()


def sec_insert_anon(m_id, time_stamp, m_context):
    if if_exist(m_id, time_stamp):
        return
    cur.execute("INSERT INTO " + settings.db_name + " (M_ID,T_STAMP,CONTENT) \
        VALUES ('" + m_id + "', '" + time_stamp + "', '" + m_context + "')")
    conn.commit()


def update_exist(m_id, time_stamp, qq):
    cur.execute("UPDATE " + settings.db_name + " SET QQ='" + qq + "' WHERE M_ID='" + m_id + "' AND T_STAMP='" + time_stamp + "'")
    conn.commit()


def if_exist(m_id, time_stamp):
    res = cur.execute("SELECT COUNT(*) FROM " + settings.db_name + " WHERE M_ID='" + m_id + "' AND T_STAMP='" + time_stamp + "'")
    for row in res:
        if int(row[0]):
            return True
    return False


def update_id(it_id, it_time):
    cur.execute("INSERT OR REPLACE INTO " + settings.qq_list_name + " (QQ, LAST_TIME) \
        VALUES ('" + it_id + "', '" + it_time + "')")
    conn.commit()


def get_last_time(it_id):
    res = cur.execute("SELECT LAST_TIME FROM " + settings.qq_list_name + " WHERE QQ='" + it_id + "'")
    for row in res:
        return row[0]
    return '0'


def db_close():
    conn.close()
