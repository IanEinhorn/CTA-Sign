import logging
from logging.handlers import SysLogHandler
import time
from CTASign import CTASign


from service import find_syslog, Service

class BusSign(Service):
    def __init__(self, *args, **kwargs):
        super(BusSign, self).__init__(*args, **kwargs)
        self.logger.addHandler(SysLogHandler(address=find_syslog(),
                               facility=SysLogHandler.LOG_DAEMON))
        self.logger.setLevel(logging.INFO)

    def run(self):
        self.logger.info("Starting CTA Sign")
        self.LEDsign = CTASign(logger=self.logger )
        while not self.got_sigterm():
            self.LEDsign.runOnce()
        self.LEDsign.stop()

if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        sys.exit('Syntax: %s COMMAND' % sys.argv[0])

    cmd = sys.argv[1].lower()
    service = BusSign('Bus_Service', pid_dir='/tmp')

    if cmd == 'start':
        service.start()
    elif cmd == 'stop':
        service.stop()
    elif cmd == 'status':
        if service.is_running():
            print "Service is running."
        else:
            print "Service is not running."
    else:
        sys.exit('Unknown command "%s".' % cmd)
