/**
* 2631. Group By
* https://leetcode.com/problems/group-by/
*/


/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
    let result = {}
    for (const item of this) {
        if (result[fn(item)]) result[fn(item)].push(item);
        else result[fn(item)] = [item];
    }
    return result;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
