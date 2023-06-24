/**
 * 2721. Execute Asynchronous Functions in Parallel
 * https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/
 */



/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = async function(functions) {
    return new Promise((resolve, reject) => {
        let output = [];
        let resolved = 0;
        functions.forEach((fn, i) => {
            fn().then((res) => {
                    output[i] = res;
                    resolved++;
                    if (resolved === functions.length)
                        resolve(output);
                }).catch(err => reject(err));
        });
        return output;
    });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */