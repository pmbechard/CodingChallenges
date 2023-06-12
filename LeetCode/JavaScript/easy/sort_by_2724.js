/**
* 2724. Sort By
* https://leetcode.com/problems/sort-by/
*/


/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    return arr.sort((a, b) => fn(a) > fn(b) ? 1 : -1);
};
