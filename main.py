import time
import logging
import request as rq
from win10toast import ToastNotifier

if __name__ == '__main__':
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(levelname)s | %(asctime)s | %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(formatter)
    logger.addHandler(consoleHandler)

    fileHandler = logging.FileHandler('history.log', 'a', 'utf-8')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    while (1):
        nowRate = rq.JPYKRW()
        nowXRPKRW = rq.XRPKRW()
        nowXRPJPY = rq.XRPJPY()
        KP = (nowXRPKRW / (nowXRPJPY * nowRate / 100) - 1) * 100

        logging.info("KP="+str(round(KP, 2))+" | XRPJPW="+str(round(nowXRPJPY, 3))+" | XRPKRW="+str(round(nowXRPKRW, 1)) + " | KRWJPY = " +  str(round(nowRate, 2)))
        toaster1 = ToastNotifier()

        toaster1.show_toast("KP " + str(round(KP, 2)) + "%  -  KPAlert",
                           "김프는 " + str(round(KP, 2)) + "%입니다.\n" +
                           "XRPKRW = ￦ " + str(round(nowXRPKRW, 1)) + "\n" +
                           "XRPJPY = ￥ " + str(round(nowXRPJPY, 3)) + "\n" +
                           "KRWJPY = " + str(round(nowRate, 2)),
                           icon_path=None,
                           duration=10
                           )

        time.sleep(300)
