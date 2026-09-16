class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_wait_time = 0
        curr_time = 0
        for cust in customers:
            arrival, duration = cust[0], cust[1]

            curr_time = max(arrival, curr_time) + duration
            total_wait_time += curr_time - arrival
        
        return total_wait_time / len(customers)