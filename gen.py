#!/usr/bin/env python

from collections import namedtuple as nt

Prf = nt('table_professor', ['pnum', 'pname', 'office', 'dept'])
Stu = nt('table_student', ['snum', 'sname', 'year'])
Crs = nt('table_course', ['cnum', 'cname'])
Cls = nt('table_class', ['cnum', 'term', 'section', 'pnum'])
Sch = nt('table_schedule', ['cnum', 'term', 'section', 'day', 'time', 'room'])
Enr = nt('table_enrollment', ['snum', 'cnum', 'term', 'section'])
Mrk = nt('table_mark', ['snum', 'cnum', 'term', 'section', 'grade'])

TO_INSERT = [
    # profs
    Prf(1, 'David Toman', '???', 'CS'),

    # students
    Stu(1, 'Adi', 3),

    # courses
    Crs('CS240', 'Data Structures'),

    # classes
    Cls('CS240', '2B', 1, 1),

    # schedules
    Sch('CS240', '2B', 1, 'Monday', '2019-10-18 0:00:00', '1337'),

    # enrollments
    Enr(1, 'CS240', '2B', 1),

    # marks
    Mrk(1, 'CS240', '2B', 1, 0)
]


def item_to_value(item):
    if isinstance(item, str):
        return f"'{item}'"

    return str(item)


def row_to_value(e):
    return ', '.join(map(item_to_value, e))


for row in TO_INSERT:
    table_name = row.__class__.__name__[len('table_'):]
    print(f'insert into {table_name} values ({row_to_value(row)})')
