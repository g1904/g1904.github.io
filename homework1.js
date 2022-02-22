let DATA = './hw1/data.json'
  
  async function fetchData() {
   const response = await fetch(DATA); 
    
    // prtt all response headers
    for (let [key, value] of response.headers) {
      prtt(`${key} = ${value}`);
    }
    prtt("----------------------------------------------------------");
     
   let gd = await response.text(); // also try .json()
   //prtt(gd);
   return gd;
  }// fetchData() 
