 /**
 * 2722. Join Two Arrays by ID
 * https://leetcode.com/problems/join-two-arrays-by-id/
 */


 /**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
const join = (arr1, arr2) => {
    const joined = {};
    [...arr1, ...arr2].forEach((obj) => {
        const id = obj.id;
        if (!joined[id]) joined[id] = { ... obj };
        else joined[id] = { ... joined[id], ...obj };
    });
    const joinedArray = Object.values(joined);
    return joinedArray.sort((a, b) => {
        return a.id - b.id;
    });
};
