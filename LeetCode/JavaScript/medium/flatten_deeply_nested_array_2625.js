/**
* 2625. Flatten Deeply Nested Array
* https://leetcode.com/problems/flatten-deeply-nested-array/
*/


/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, n) {
    output = new Array();
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < arr.length; j++) {
            if (Array.isArray(arr[j])) output.push(...arr[j]);
            else output.push(arr[j]);
        }
        arr = new Array(...output);
        output = new Array();
    }
    return arr;
};
