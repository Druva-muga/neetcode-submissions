class Solution {
    public int findDuplicate(int[] nums) {
        int n=nums.length;
        int c=nums[0];
        int temp;
        while(true){
            if(nums[c]>0){
                temp=nums[c];
                nums[c] = -1;
                c=temp;
            }else if(nums[c]==-1){
                return c;
            }
        }
    }
}
