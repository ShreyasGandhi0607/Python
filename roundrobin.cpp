#include <iostream>
#include <queue>
#include <list>

class Process {
public:
    int getArrivalTime() const { return arrivalTime; }
    int getRemainingBurstTime() const { return remainingBurstTime; }
    int getBurstTime() const { return burstTime; }
    void setRemainingBurstTime(int time) { remainingBurstTime = time; }
    void setCompletionTime(int time) { completionTime = time; }
    void setTurnaroundTime(int time) { turnaroundTime = time; }
    void setWaitingTime(int time) { waitingTime = time; }
    void displayData() const {
        std::cout << arrivalTime << "\t" << burstTime << "\t" << completionTime << "\t"
                  << turnaroundTime << "\t" << waitingTime << std::endl;
    }
    
private:
    int arrivalTime;
    int remainingBurstTime;
    int burstTime;
    int completionTime;
    int turnaroundTime;
    int waitingTime;
};

class Msg {
public:
    static void println(const std::string &msg) {
        std::cout << msg << std::endl;
    }
};

class RoundRobin {
private:
    std::queue<Process> readyQueue;
    
    void fillReadyQueue(int time, int prevTime, std::priority_queue<Process> &priorityQueue) {
        auto iterator = priorityQueue.begin();
        while(iterator != priorityQueue.end()) {
            Process process = *iterator;
            if(process.getArrivalTime() <= time && ((process.getArrivalTime() > prevTime) || readyQueue.empty())) {
                readyQueue.push(process);
            }
            iterator++;
        }
    }
    
    long findLastArrivalTime(std::priority_queue<Process> &priorityQueue) {
        long lastArrivalTime = 0;
        auto iterator = priorityQueue.begin();
        while(iterator != priorityQueue.end()) {
            lastArrivalTime = (*iterator).getArrivalTime();
            iterator++;
        }
        return lastArrivalTime;
    }
    
public:
    void schedule(int noOfProcess, std::priority_queue<Process> &priorityQueue, int quantumTime) {
        double avgWaitingTime = 0;
        double avgTurnaroundTime = 0;
        readyQueue = std::queue<Process>();
        long lastArrivalTime = findLastArrivalTime(priorityQueue);
        
        int time = 0;
        int prevTime = 0;
        
        fillReadyQueue(time, prevTime, priorityQueue);        
        Msg::println("PNO\tAT\tBT\tCT\tTAT\tWT");
        while(!readyQueue.empty()) {
            Process process = readyQueue.front();
            if(process.getRemainingBurstTime() > quantumTime) {
                prevTime = time;
                time += quantumTime;
                process.setRemainingBurstTime(process.getRemainingBurstTime() - quantumTime);
                if(prevTime <= lastArrivalTime)
                    fillReadyQueue(time, prevTime, priorityQueue);
                readyQueue.pop();
                readyQueue.push(process);
            }
            else {
                prevTime = time;
                time += process.getRemainingBurstTime();
                process.setRemainingBurstTime(0);
                process.setCompletionTime(time);
                process.setTurnaroundTime(process.getCompletionTime() - process.getArrivalTime());
                process.setWaitingTime(process.getTurnaroundTime() - process.getBurstTime());
                readyQueue.pop();
            }
        }
        while(!priorityQueue.empty()) {
            Process process = priorityQueue.top();
            avgWaitingTime += process.getWaitingTime();
            avgTurnaroundTime += process.getTurnaroundTime();
            process.displayData();
            priorityQueue.pop();
        }
        Msg::println("Average Turnaround time: " + std::to_string(avgTurnaroundTime / noOfProcess));
        Msg::println("Average Waiting time: " + std::to_string(avgWaitingTime / noOfProcess));
    }
};

int main() {
    int noOfProcess = 3;  // Replace with the desired number of processes
    std::priority_queue<Process> priorityQueue;
    
    // Add processes to the priorityQueue
    
    int quantumTime = 2;  // Replace with the desired quantum time
    RoundRobin scheduler;
    scheduler.schedule(noOfProcess, priorityQueue, quantumTime);
    
    return 0;
}
