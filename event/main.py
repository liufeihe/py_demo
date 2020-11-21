#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
from job import Job

def main():
    event = threading.Event()
    job = Job('job-1', event)
    job.start()

if __name__ == "__main__":
    main()