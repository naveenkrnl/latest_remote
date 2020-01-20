var express = require('express');
var router = express.Router();
var google = require('google')

google.resultsPerPage = 10
var nextCounter = 0

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Google Search Scraper' });
});

router.get('/search', (req, res) => {
	// console.log('q is',req.params.query)
	// console.log('qu is',req.query.q)
	console.log(req.query.q)
	google(req.query.q, function (err, response){
		if (err) console.error(err)
		console.log(response.links)
		res.send(response.links)
	  // for (var i = 0; i < res.links.length; ++i) {
	  //   var link = res.links[i];
	  //   console.log(link.title + ' - ' + link.href)
	  //   console.log(link.description + "\n")
	  // }
	 
	  // if (nextCounter < 4) {
	  //   nextCounter += 1
	  //   if (res.next) res.next()
	  // }
	})
})

module.exports = router;
