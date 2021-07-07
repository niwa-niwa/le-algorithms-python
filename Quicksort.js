console.log("Start QuickSort");

function quickSort(numbers) {
  const _partition = (nums, low, high) => {
    let i = low - 1;
    for (let j = low; j < numbers.length; j++) {
      if (nums[j] < nums[high]) {
        i++;
        [nums[i], nums[j]] = [nums[j], nums[i]];
      }
    }
    i++;
    [nums[i], nums[high]] = [nums[high], nums[i]];
    return i;
  };

  const _quickSort = (numbers, low, high) => {
    if (low < high) {
      let partition = _partition(numbers, low, high);
      _quickSort(numbers, low, partition - 1);
      _quickSort(numbers, partition + 1, high);
    }
  };

  _quickSort(numbers, 0, numbers.length - 1);
  return numbers;
}

let nums = [];
for (let i = 0; i < 10; i++) {
  nums[i] = Math.floor(Math.random() * 10) + 1;
}
console.log(nums);
// nums = [1,8,5,9,4,6,7];
const result = quickSort(nums);
console.log("result = ", result);
