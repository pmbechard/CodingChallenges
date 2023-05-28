/**
* 2649. Nested Array Generator
* https://leetcode.com/problems/nested-array-generator/
*/


/**
 * @param {Array} arr
 * @return {Generator}
 */
var inorderTraversal = function*(arr) {
    for (let i of arr) {
        if (Array.isArray(i)) yield *inorderTraversal(i)
        else yield i;
    }

};

/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */
