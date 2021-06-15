console.log('test script')

function quickSort(numbers){

  const _partition = (numbers, low, high) => {
    i = low - 1;
    for(j = 0; j < numbers.length; j++){
      if(numbers[j] < numbers[high] ){
        i++;
        [numbers[i], numbers[j]] = [numbers[j], numbers[i]];
      }
    }
    i++;
    [numbers[i], numbers[high]] = [numbers[high], numbers[i]];
    return i
  }

  const _quickSort = (numbers, low, high) => {
    if( low < high ){
      let partition = _partition(numbers, low, high);
      _quickSort(numbers, low, partition-1);
      _quickSort(numbers, partition+1, high);
    }
    console.log(numbers);
  }

  _quickSort(numbers, 0, numbers.length-1);
  return numbers

}

let nums = [1,8,5,9,4,3,7];
console.log(quickSort(nums));