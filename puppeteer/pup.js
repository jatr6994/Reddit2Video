const puppeteer = require('puppeteer');
const fs = require('fs');

function delay(time) {
   return new Promise(function(resolve) { 
       setTimeout(resolve, time)
   });
}

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  await page.tracing.start({ screenshots: true, path: 'trace.json' });
  await page.goto('file:///C:/Users/7UR7L3/Documents/MEGAsync/dev/projects/reddit2video/Reddit2Video/cssAnim.html', { timeout: 60000 });
  await delay( 4000 );
  await page.tracing.stop();

  // --- extracting data from trace.json ---
  const tracing = JSON.parse(fs.readFileSync('./trace.json', 'utf8'));
  const traceScreenshots = tracing.traceEvents.filter(x => (
      x.cat === 'disabled-by-default-devtools.screenshot' &&
      x.name === 'Screenshot' &&
      typeof x.args !== 'undefined' &&
      typeof x.args.snapshot !== 'undefined'
  ));
  traceScreenshots.forEach(function(snap, index) {
    fs.writeFile('frames/trace-screenshot-'+index+'.png', snap.args.snapshot, 'base64', function(err) {
      if (err) {
        console.log('writeFile error', err);
      }
    });
  });
  // --- end extracting data from trace.json ---

  await page.close();
})();