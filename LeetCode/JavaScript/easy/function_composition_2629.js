/**
* 2629. Function Composition
* https://leetcode.com/problems/function-composition/
*/


/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
	return function(x) {
        return functions.reverse().reduce((acc, func) => func(acc), x)
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
