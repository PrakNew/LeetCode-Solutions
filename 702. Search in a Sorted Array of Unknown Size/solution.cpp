using namespace std;

/**
 * // This is the ArrayReader's API interface.
 * // You should not implement it, or speculate about its implementation
 * class ArrayReader {
 *   public:
 *     int get(int index);
 * };
 */

class Solution {
public:
    int search(const ArrayReader& reader, int target) {
        int lo = 0, hi = 1;
        
        // Searching boundaries for binary search
        while(reader.get(hi) < target){
            lo = hi;
            hi <<= 1;
        }        
        
        while(lo <= hi){
            int mid = (lo+hi) >> 1;
            int ind = reader.get(mid);
            if(ind == target)
                return mid;
            else if(ind == 2147483647 || ind > target)
                hi = mid - 1;
            else
                lo = mid + 1;
        }
        
        return -1;
    }
};