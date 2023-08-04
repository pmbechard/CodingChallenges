/*
 * 2622. Cache With Time Limit
 * https://leetcode.com/problems/cache-with-time-limit/
 */



var TimeLimitedCache = function() {
    this.obj = {};
    this.timeouts = {};
};

/**
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const exists = !!this.obj[key];
    this.obj[key] = value;
    if (exists) clearTimeout(this.timeouts[key]);
    this.timeouts[key] = setTimeout(() => {
        delete this.obj[key];
        delete this.timeouts[key];
    }, duration);
    return exists;
};

/**
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    return this.obj[key] || -1;
};

/**
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return Object.keys(this.obj).length;
};

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */
