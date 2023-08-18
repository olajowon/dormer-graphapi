# Created by zhouwang on 2020/9/11.

import sys
import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
VENV_DIR = os.path.join(PROJECT_DIR, 'venv')


def start():
    print('#### start\n')
    os.system(f'cp -rf {PROJECT_DIR}/etc/graphite-api.yaml /etc/graphite-api.yaml')
    status = os.system(f'source {VENV_DIR}/bin/activate && cd {PROJECT_DIR} && '
                       f'pip install -r {PROJECT_DIR}/requirements.txt && '
                       f'uwsgi --ini {PROJECT_DIR}/uwsgi.ini')
    print('#### start %s\n' % ('successful' if status == 0 else 'failure'))


def stop():
    print('#### stop\n')
    status = os.system(f'source {VENV_DIR}/bin/activate && uwsgi --stop /var/run/dormer-graphapi-uwsgi.pid')
    print('#### stop %s\n' % ('successful' if status == 0 else 'failure'))


def restart():
    print('#### restart\n')
    os.system(f'cp -rf {PROJECT_DIR}/etc/graphite-api.yaml /etc/graphite-api.yaml')
    status = os.system(f'source {VENV_DIR}/bin/activate && '
                       f'pip install -r {PROJECT_DIR}/requirements.txt && '
                       f'uwsgi --reload /var/run/dormer-graphapi-uwsgi.pid')
    print('#### restart %s\n' % ('successful' if status == 0 else 'failure'))


def init():
    if not os.path.isdir(VENV_DIR):
        os.system(f'cd {PROJECT_DIR} && python3 -m venv venv')


def pip():
    print('#### pip\n')
    status = os.system(f'source {VENV_DIR}/bin/activate && '
              f'pip install -r {PROJECT_DIR}/requirements.txt')
    print('#### pip %s\n' % ('successful' if status == 0 else 'failure'))


if __name__ == '__main__':
    init()

    action = sys.argv[1]
    if action == 'start':
        start()
    elif action == 'stop':
        stop()
    elif action == 'restart':
        restart()
    elif action == 'pip':
        restart()
