import logging
import xmltodict


def check_output():
    log = _get_logger()
    with open('output.xml', 'r') as file:
        result = xmltodict.parse(file.read())
    passed = result['robot']['statistics']['total']['stat'][0]['@pass']
    failed = result['robot']['statistics']['total']['stat'][0]['@fail']
    if passed == '0' or failed != '0':
        log.error('%s critical tests failed!', failed)
        raise SuiteFailedException('Exiting with error')
    else:
        log.info('Exiting with success')
        exit(0)
    raise SuiteFailedException('Exiting with error')


def _get_logger():
    log = logging.getLogger()
    console = logging.StreamHandler()
    format_log = '%(asctime)s %(levelname)s: %(message)s'
    console.setFormatter(logging.Formatter(format_log))
    log.addHandler(console)
    log.setLevel(logging.INFO)
    return log


class SuiteFailedException(Exception):
    pass


def main():
    check_output()


if __name__ == '__main__':
    main()
