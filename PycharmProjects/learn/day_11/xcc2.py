#!/usr/bin/env python3
import queue
import threading
import contextlib
import time


StopEvent = object()


class ThreadPool(object):

    def __init__(self, max_num, max_task_num = None):
        if max_task_num:
            self.q = queue.Queue(max_task_num)
            #最多创建的线程数(线程池最大容量)
        else:
            self.q = queue.Queue()
        self.max_num = max_num
        self.cancel = False
        self.terminal = False
        self.generate_list = []
        #空闲的线程数量
        self.free_list = []

    def run(self, func, args, callback=None):
        """
        线程池执行一个任务
        :param func: 任务函数
        :param args: 任务函数所需参数
        :param callback: 任务执行失败或成功后执行的回调函数，回调函数有两个参数1、任务函数执行状态；2、任务函数返回值（默认为None，即：不执行回调函数）
        :return: 如果线程池已经终止，则返回True否则None
        """
        if self.cancel:
            return
        if len(self.free_list) == 0 and len(self.generate_list) < self.max_num:
            self.generate_thread()
        w = (func, args, callback,)
        self.q.put(w)

    def generate_thread(self):
        """
        创建一个线程
        """
        t = threading.Thread(target=self.call)
        t.start()

    def call(self):
        """
        循环去获取任务函数并执行任务函数
        """
        current_thread = threading.currentThread()
        self.generate_list.append(current_thread)
        #event内部3元素=(fun args callable)
        event = self.q.get()
        while event != StopEvent:

            func, arguments, callback = event
            try:
                result = func(*arguments)
                status = True
            except Exception as e:
                status = False
                result = None
            #有回调函数执行回调   反之pass
            if callback is not None:
                try:
                    callback(status, result)
                except Exception as e:
                    status = False
                    result = e
            with self.worker_state(self.free_list, current_thread):
            #进程
                if self.terminal:
                    event = StopEvent
                else:
                    event = self.q.get()
        else:
            #不是元祖,不是任务
            self.generate_list.remove(current_thread)

    def close(self):
        """
        执行完所有的任务后，所有线程停止
        """
        self.cancel = True
        full_size = len(self.generate_list)
        while full_size:
            self.q.put(StopEvent)
            full_size -= 1

    def terminate(self):
        """
        无论是否还有任务，终止线程
        """
        self.terminal = True

        while self.generate_list:
            self.q.put(StopEvent)

        self.q.queue.clear()
    #处理上下文
    @contextlib.contextmanager
    def worker_state(self, state_list, worker_thread):
        """
        用于记录线程中正在等待的线程数
        """
        state_list.append(worker_thread)
        try:
            yield
        finally:
            state_list.remove(worker_thread)



# How to use


pool = ThreadPool(5)

def callback(status, result):
    # status, execute action status
    # result, execute action return value
    pass


def action(i):
    print(i)

for i in range(30):
    # #将任务放在队列中
    # #着手开始处理任务
    #     -创建线程
    #           -有空闲线程不创建,泽不再创建
    #           -不能高于线程池的限制,根据任务个数判断
    #           -没有空闲线程
    #     -线程去队列中取任务
    ret = pool.run(action, (i,), callback)

time.sleep(5)
print(len(pool.generate_list), len(pool.free_list))
print(len(pool.generate_list), len(pool.free_list))
pool.close()
pool.terminate()