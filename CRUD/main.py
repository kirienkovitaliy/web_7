import argparse
from database.repository import (
    create_teacher,
    list_teachers,
    update_teacher,
    remove_teacher,
    create_group,
    list_groups,
    update_group,
    remove_group
)


def main():
    parser = argparse.ArgumentParser(description='CLI for CRUD with database')
    parser.add_argument('--action', '-a', help='Commands: create, update, list, remove')
    parser.add_argument('--model', '-m', help='Model: Teacher, Group')
    parser.add_argument('--name', '-n', help="Name")
    parser.add_argument('--id', help='ID')

    args = parser.parse_args()
    action = args.action
    model = args.model
    name = args.name
    obj_id = args.id

    if model == 'Teacher':
        if action == 'create':
            create_teacher(name)
        elif action == 'list':
            list_teachers()
        elif action == 'update':
            update_teacher(obj_id, name)
        elif action == 'remove':
            remove_teacher(obj_id)
    elif model == 'Group':
        if action == 'create':
            create_group(name)
        elif action == 'list':
            list_groups()
        elif action == 'update':
            update_group(obj_id, name)
        elif action == 'remove':
            remove_group(obj_id)
    else:
        print('Invalid model.')


if __name__ == '__main__':
    main()
