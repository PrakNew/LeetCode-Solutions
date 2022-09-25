/*
Idea: Sort based on start times. DP[i] = max profit starting at index i 

Time complexity : O(n log n)
Space complexity: O(n)
*/

#include<vector>
#include<algorithm>

using namespace std;

struct Job
{
    int startTime;
    int endTime;
    int profit;
};

class Solution {
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        int n = startTime.size();
        vector<Job> jobs;
        for(int i = 0; i < n; ++i)
            jobs.push_back({startTime[i], endTime[i], profit[i]});
        
        // Sort based on job start times
        sort(jobs.begin(), jobs.end(),
            [](auto const& job1, auto const& job2) 
             { return job1.startTime < job2.startTime; } 
            );
        
        startTime.clear();
        endTime.clear();
        profit.clear();
        
        for(auto job: jobs){
            startTime.push_back(job.startTime);
            endTime.push_back(job.endTime);
            profit.push_back(job.profit);
        }
        
        vector<int> dp(n, -1);
        return util(0, startTime, endTime, profit, dp);
    }

private:
    int util(int index, vector<int>& start, vector<int>& end, vector<int>& profit, vector<int>& dp)
    {
        int n = start.size();
        
        if(index == n-1)
            return profit[index];
        
        if(dp[index] != -1)
            return dp[index];
        
        // Include current job 
        int include = profit[index];
        auto next_index = lower_bound(start.begin(), start.end(), end[index]);
        if(next_index != start.end())
            include += util(next_index - start.begin(), start, end, profit, dp);
            
        // Exclude current job
        int exclude = util(index + 1, start, end, profit, dp);
        
        dp[index] = max(include, exclude);
        
        return dp[index];
    }
};