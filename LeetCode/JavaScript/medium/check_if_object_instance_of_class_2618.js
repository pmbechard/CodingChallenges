/**
* 2618. Check if Object Instance of Class
* https://leetcode.com/problems/check-if-object-instance-of-class/
*/


/**
 * @param {Object} object
 * @param {Function} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    return obj != null && typeof classFunction === 'function' ? Object(obj) instanceof classFunction : false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */