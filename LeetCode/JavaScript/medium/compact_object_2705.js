/**
 * 2705. Compact Object
 * https://leetcode.com/problems/compact-object/
 */


 /**
 * @param {Object} obj
 * @return {Object}
 */
var compactObject = function(obj) {
    let result;
    if (Array.isArray(obj)) {
        result = [];
        for (let i of obj) {
            if (typeof i === 'object')
                i = compactObject(i);
            if (Boolean(i))
                result.push(i);
        }
    } else if (obj) {
        result = {};
        for (let i in obj) {
            if (typeof obj[i] === 'object')
                obj[i] = compactObject(obj[i]);
            if (Boolean(obj[i]))
                result[i] = obj[i];
        }
    }
    return result;
};
