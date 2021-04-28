// get CLI args and parse
//start the scraping object

const Scraper = require('./scraper')
const config = require('config') //read the config file
const lineReader = require('line-reader');

const cliArgs = process.argv.slice(2)
const apiKey = cliArgs[0]

lineReader.eachLine(config.get('writeToFile.path'), (line, last) => {
    if(last) {
        const scraper = new Scraper(apiKey, line.split(',')[0]) //intialize the scraper object with the last added match ID from the dataset
        setTimeout(() => scraper.scrape(), 1000) //wait 1 second and then start scraping 
    }
});
