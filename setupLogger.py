import logging.config

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(filename="VeeamVacanciesTest.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S',
                    level=logging.INFO)