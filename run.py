#!flask/bin/python3
import time
import logging

from app_folder import app

logging.basicConfig(level=logging.INFO)





# while True:
try:
    app.run(host="0.0.0.0", port=5000, debug=True)
except KeyboardInterrupt:
    logging.info("The module was stopped")
except Exception as err:
    logging.exception("The module was failed {}".format(err))
finally:
    time.sleep(1)
