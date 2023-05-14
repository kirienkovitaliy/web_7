from database.db import session
from database.models import Teacher, Group


def create_teacher(name):
    teacher = Teacher(fullname=name)
    session.add(teacher)
    session.commit()


def list_teachers():
    teachers = session.query(Teacher).all()
    for teacher in teachers:
        print(teacher.fullname)


def update_teacher(teacher_id, name):
    teacher = session.query(Teacher).get(teacher_id)
    if teacher:
        teacher.fullname = name
        session.commit()


def remove_teacher(teacher_id):
    teacher = session.query(Teacher).get(teacher_id)
    if teacher:
        session.delete(teacher)
        session.commit()


def create_group(name):
    group = Group(name=name)
    session.add(group)
    session.commit()


def list_groups():
    groups = session.query(Group).all()
    for group in groups:
        print(group.name)


def update_group(group_id, name):
    group = session.query(Group).get(group_id)
    if group:
        group.name = name
        session.commit()


def remove_group(group_id):
    group = session.query(Group).get(group_id)
    if group:
        session.delete(group)
        session.commit()
