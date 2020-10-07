/**
Runtime: 0 ms, faster than 100.00% of C++ online submissions for Sort Colors.
Memory Usage: 8.5 MB, less than 29.60% of C++ online submissions for Sort Colors.

https://youtu.be/XOX1WvUMpwQ?t=945
*/
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int p0=0, p=0, p2=nums.size()-1;
        while(p<=p2){
            if(nums[p]==0){
                nums[p]=nums[p0];
                nums[p0]=0;
                p0++;
                p++;
            }else if(nums[p]==2){
                nums[p]=nums[p2];
                nums[p2]=2;
                p2--;
            }else{
                p++;
            }
        }
    }
};
