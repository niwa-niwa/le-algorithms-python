console.log('test script')

function quickSort(numbers){

  const _partition = (nums, low, high) => {
    
    const numbers = [...nums]
    let i = low - 1;
    for(let j = low; j < numbers.length; j++){
      
      if(numbers[j] < numbers[high] ){
        i++;
        [numbers[i], numbers[j]] = [numbers[j], numbers[i]];
      }
    }
    i++;
    [numbers[i], numbers[high]] = [numbers[high], numbers[i]];
    return {index:i, numbers:numbers}
  }

  const _quickSort = (numbers, low, high) => {
    if( low < high ){
      let partition = _partition(numbers, low, high);
      _quickSort(partition.numbers, low, partition.index-1);
      _quickSort(partition.numbers, partition.index+1, high);
    }
  }

  _quickSort(numbers, 0, numbers.length-1);
  return numbers

}

const nums = [1,8,5,9,4,3,7];
const result = quickSort(nums);
console.log("result = ",result);
// console.log(quickSort(nums));
// console.log(nums)
// [nums[0], nums[5]] = [nums[5], nums[0]]
// console.log(nums)

// const arr = [1,2,3];
// [arr[2], arr[1]] = [arr[1], arr[2]];
// console.log(arr); // [1,3,2]