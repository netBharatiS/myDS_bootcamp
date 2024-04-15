import axios from 'axios';


const findBestCost = (collected_outlets, cost) => {
  var eligible = [];
  for (let i=0; i<collected_outlets.length; i++){
    if (collected_outlets[i].estimated_cost < cost) {
      eligible = [...eligible, collected_outlets[i]];
    }
  }

  var highestratings = 0;
  var hightestratingsCost = 0;
  var hightratingOutlet;
  for (let j=0; j<eligible.length; j++){
    if (eligible[j].user_rating.average_rating > highestratings){
      highestratings = eligible[j].user_rating.average_rating
      hightestratingsCost = eligible[j].estimated_cost
      hightratingOutlet = eligible[j]
    }

    if (eligible[j].user_rating.average_rating == highestratings){
      if (eligible[j].estimated_cost < hightestratingsCost) {
        highestratings = eligible[j].user_rating.average_rating
        hightestratingsCost = eligible[j].estimated_cost
        hightratingOutlet = eligible[j]
      }
    }
  }

  return hightratingOutlet
}

const collect_food_outlets_and_find_best =  async (cityName, cost, collected_outlets, pageNum, resolve, reject) => {
  axios.get(`https://jsonmock.hackerrank.com/api/food_outlets?city=` + cityName + `&page=` + pageNum).then(result => {
    collected_outlets = [...collected_outlets, ...result.data.data]

    if (result.data.page == result.data.total_pages) {
      var bestCostRestaurant = findBestCost(collected_outlets, cost)
      resolve(bestCostRestaurant.name)
    } else {
      collect_food_outlets_and_find_best(cityName, cost, collected_outlets, ++pageNum, resolve, reject)
    }

}).catch(error => {
  console.log(error)
  reject(error)
})
}

async function bestRestaurant(city, cost) {
  var prom = new Promise((resolve, reject) => {
  collect_food_outlets_and_find_best(city, cost, [], 1, resolve, reject)
});
return prom;
// await collect_food_outlets("seattle", [], 1)
}

const result = await bestRestaurant("Seattle", 120);

console.log("res==> " + result)





