from threading import Thread, Condition, current_thread, Lock


class ReadersWriteLock:
    """ A lock object that allows many simultaneous "read locks", but
    only one "write lock." """

    def __init__(self):
        self._read_ready = Condition(Lock())
        self._readers = 0

    def acquire_read_lock(self):
        """ Acquire a read lock. Blocks only if a thread has
        acquired the write lock. """
        self._read_ready.acquire()
        try:
            self._readers += 1
        finally:
            self._read_ready.release()

    def release_read_lock(self):
        """ Release a read lock. """
        self._read_ready.acquire()
        try:
            self._readers -= 1
            if not self._readers:
                self._read_ready.notifyAll(  )
        finally:
            self._read_ready.release(  )

    def acquire_write_lock(self):
        """ Acquire a write lock. Blocks until there are no
        acquired read or write locks. """
        self._read_ready.acquire(  )
        while self._readers > 0:
            self._read_ready.wait(  )

    def release_write_lock(self):
        """ Release a write lock. """
        self._read_ready.release(  )
