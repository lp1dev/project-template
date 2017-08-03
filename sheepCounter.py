#!/bin/python
from time import sleep
import logging as log

def	main():
  i = 1
  while True:
    log.info("%i sheep(s)" %(i))
    i += 1
    sleep(4)
  return 0

if __name__ == '__main__':
  exit(main())
