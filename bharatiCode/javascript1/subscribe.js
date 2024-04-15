import axios from 'axios';

const collectAllFoodOutlets = async () => {
  var food_outlets = []
  var count = 0
  while (count < 10) {
    try {
        const res = await axios.get(`https://jsonmock.hackerrank.com/api/food_outlets?city=Seattle`);
        food_outlets = [...food_outlets, ...res.data.data]

        if (res.data.page == res.data.total_pages) {
          break;
        }
    } catch (err) {
      console.log(err);
      break;
    }
    count++;
  }
  return food_outlets;
};

var outlets = collectAllFoodOutlets()
console.log(outlets)
