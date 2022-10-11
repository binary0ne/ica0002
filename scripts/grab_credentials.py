import requests
from pyquery import PyQuery

USERNAME = 'binary0ne'
SOURCE_LINK = f'http://193.40.156.67/students/{USERNAME}.html'
PATH_TO_HOSTS = '../hosts'


def get_config_lines():
    response = requests.get(SOURCE_LINK)
    html = response.content

    pq = PyQuery(html)
    table = pq('table>tr>th')
    table = table.parent().items()
    for x in table:
        if x.html() == '<th>Name</th><th>Internal IP</th><th>Public SSH</th><th>Public URL</th>':
            table = x
            break
    table = table.parent()
    table = table('tr>td:first-of-type').items()

    config_lines = []
    for x in table:
        if USERNAME in x.parent().html():
            config_lines.append(str(x.parent().html()))
    return config_lines


def process_config_lines(cl):
    params = []
    for line in cl:
        line = line.replace('<td>', '')
        data_array = line.split('</td>')
        hostname = data_array[0]
        ip = data_array[2].split(' ')[0].split('@')[1]
        port = data_array[2].split(' ')[-1]
        user = data_array[2].split(' ')[0].split('@')[0]
        param = f'{hostname} ansible_host={ip} ansible_port={port} ansible_user={user}\n'
        params.append(param)
    return params


def write_params(params):
    with open(PATH_TO_HOSTS, 'a') as f:
        for param in params:
            f.write(param)


def clear_file():
    with open(PATH_TO_HOSTS, 'w') as f:
        f.write('')


def main():
    config_lines = get_config_lines()
    params = process_config_lines(config_lines)
    clear_file()
    write_params(params)


if __name__ == '__main__':
    main()

