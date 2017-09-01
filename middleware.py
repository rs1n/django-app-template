import logging
import time

logger = logging.getLogger(__name__)


class LogProcessingTimeMiddleware(object):
    'LogProcessingTimeMiddleware logs the request processing time.'

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # Remember the start moment.
        start = time.time()

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        # Calculate the request processing time (in ms).
        processing_time = (time.time() - start) * 1000

        logger.debug('Request processed in %f ms', processing_time)

        return response
