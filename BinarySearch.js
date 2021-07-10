console.log("Binary Search Start!");

function binarySearch(numbers, target){
  const _binarySearch = (numbers, target, left, right) => {
    while(left <= right){
      const center = Math.floor((left + right) / 2);
      if(numbers[center] === target){
        return center;
      }else if(numbers[center] < target){
        return _binarySearch(numbers, target, center+1, right);
      }else if(numbers[center] > target){
        return _binarySearch(numbers, target, left, center-1);
      }
    }
    return null;
  }
  return _binarySearch(numbers, target, 0, numbers.length-1);
}

const nums = [0,1,2,3,4,5,6,7,8,9];
const target = 91
const result = binarySearch(nums, target);
console.log("result = ", result);
