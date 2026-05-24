class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> restSum;

        for (int i = 0; i < nums.size(); i++) {
            int tmp = target - nums[i];

            if (restSum.find(tmp) != restSum.end()) {
                return {min(i, restSum[tmp]), max(i, restSum[tmp])};
            } else {
                restSum[nums[i]] = i;
            }
        }

        return {};
    }
};