#!/usr/bin/node
// convert numbers depend on base

exports.converter = function(base) {
  return function myconvert(num) {
    return num.toString(base);
  };
};
