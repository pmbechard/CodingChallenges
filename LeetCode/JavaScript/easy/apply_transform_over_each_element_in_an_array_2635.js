/**
* 2635. Apply Transform Over Each Element in Array
* https://leetcode.com/problems/apply-transform-over-each-element-in-array/
*/


/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    result = []
    for (let i = 0; i < arr.length; i++)
        result.push(fn(arr[i], i))
    return result
};
