import logging

def get_logger(name='', level=logging.DEBUG, ):
	logger = logging.getLogger(name)
	logger.setLevel(level)

	# create console handler and set level to debug
	ch = logging.StreamHandler()
	ch.setLevel(level)

	# create formatter
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

	# add formatter to ch
	ch.setFormatter(formatter)

	# add ch to logger
	logger.addHandler(ch)
	return logger
