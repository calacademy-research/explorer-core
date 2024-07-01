const puppeteer = require('puppeteer');


async function scrapeMedia(url){
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(url);

}

scrapeMedia('https://www.morphosource.org/concern/media/000537957?locale=en');