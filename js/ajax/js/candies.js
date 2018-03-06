var req = new XMLHttpRequest();
req.open('GET', '/candies.json');
req.onreadystatechange = function () {
    if(req.readyState === 4 && req.status === 200) {
        var candies = JSON.parse(req.responseText);
        var candyList = '<ul class="candies">';
        for (var i=0; i<candies.length; i += 1) {
            if (candies[i].quantity > 0) {
            candyList += '<li class="item available">';
            } else {
            candyList += '<li class="item sold-out">';
        }
        candyList += candies[i].name + '<br>' + "Brand: " + candies[i].brand;
        candyList += '<button>Buy</button>'
        candyList += '</li>';
    }
    candyList += '</ul>';
    document.getElementById('candyListing').innerHTML = candyList;
    }
};
req.send();