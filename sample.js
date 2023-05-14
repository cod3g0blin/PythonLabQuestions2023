function findHighestFreq(arr) {
    let countOnes = 0;
    let countTwos = 0;
    for (let num of arr) {
      if (num === 1) {
        countOnes++;
      } else if (num === 2) {
        countTwos++;
      }
    }
    if (countOnes > countTwos) {
      return countOnes; //response.push()
    } else if (countTwos > countOnes) {
      return countTwos;
    } else {
      // Return either countOnes or countTwos
      return countOnes || countTwos;
    }
  }
  
  // Example usage:
  //let result = [1, 2, 1, 1, 2, 2, 1];
  let highestFreq = findHighestFreq(result);
  console.log(highestFreq);
  