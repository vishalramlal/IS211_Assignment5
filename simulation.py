#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Assignment 5
import csv
import argparse
import sys

class Server:
    def __init__(self):
        self.current_task = None
        self.time_remaining = 0
        
    def tick(self):
        if self.current_task != None:
            self.time_remaining = int(self.time_remaining) - 1
            if self.time_remaining <= 0:
                self.current_task = None
                
    def busy(self):
        if self.current_task != None:
            return True
        else:return False
        
    def start_next(self,new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_proct()
      

        
class Request:
    def __init__(self, cur_item):
        self.timestamp = cur_item[0]
        self.page_proct = cur_item[2]
        
    def get_stamp(self):
        return self.timestamp
    
    def get_proct(self):
        return self.page_proct
    
    def wait_time(self, simtime):
        return int(self.timestamp) - int(simtime)
            
    
class itemControl:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def main():
    parser = argparse.ArgumentParser(description='--file path argument')
    parser.add_argument("--file", required = True, help = "Filepath to CSV data. Required")
    #parser.add_argument("--servers", required = False, help = "Number of servers to simulate.")
    args = parser.parse_args()
    with open(args.file) as file:
        csvreader = list(csv.reader(file))

        
        def simulateOneServer(csvreader):
            srvreq = Server()
            item_queue = itemControl()
            simtime = 0
            waiting_times = []
            for line in csvreader:
                cur_item = Request(line)
                item_queue.enqueue(cur_item)
            if not srvreq.busy() and not item_queue.is_empty():
                next_task = item_queue.dequeue()
                waiting_times.append(next_task.wait_time(simtime))
                simtime = next_task.timestamp
                srvreq.start_next(next_task)
            srvreq.tick()
        
            average_wait = sum(waiting_times) / len(waiting_times)
            print("Average Wait %6.2f secs."%(average_wait))

        simulateOneServer(csvreader)
        
        #def simulateManyServers(csvreader):
            
        
        #if args.servers > 1:
        #    simulateManyServers(csvreader)
        #else:
        #    simulateOneServer(csvreader)
            
        
if __name__ == "__main__":
        main()     
    


# In[ ]:




