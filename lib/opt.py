# -*- coding: utf-8 -*-
from lib.logger_opt import *
from lib.exception_opt import ExceptionCommon
import sqlite3

def connect_sqlite():
    return sqlite3.connect('database/record.sqlite')
    
def recursive_select(cur, code):
    cur.execute("SELECT name, registration_date, introducer_code, tree_left_code, tree_right_code FROM policyholders WHERE code = ?", (code,))
    
    r = cur.fetchall()
    if not len(r) > 0:
        raise ExceptionCommon(message=f"The member code '{code}' does not exist!")
        
    ret_info = {
        'code': code,
        'name': r[0][0],
        'registration_date': r[0][1],
        'introducer_code': r[0][2]
    }
    
    tree_left_code, tree_right_code = r[0][3], r[0][4]
    if tree_left_code:
        ret_info['l'] = recursive_select(cur, tree_left_code)
        
    if tree_right_code:
        ret_info['r'] = recursive_select(cur, tree_right_code)
        
    return ret_info
    
def policyholders(code):
    conn = connect_sqlite()
    try:
        with conn:
            cur = conn.cursor()
            return recursive_select(cur, code)
    except sqlite3.Error as e:
        raise ExceptionCommon(message=str(e))
    finally:
        conn.close()
        
def policyholders_top(code):
    conn = connect_sqlite()
    try:
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT tree_parent_code FROM policyholders WHERE code = ?", (code,))
            
            r = cur.fetchall()
            if not len(r) > 0:
                raise ExceptionCommon(message=f"The member code '{code}' does not exist!")
                
            tree_parent_code = r[0][0]
            if not r[0][0]:
                raise ExceptionCommon(message=f"The member code '{code}' does not have a parent node!")
                
            return recursive_select(cur, tree_parent_code)
    except sqlite3.Error as e:
        raise ExceptionCommon(message=str(e))
    finally:
        conn.close()
        