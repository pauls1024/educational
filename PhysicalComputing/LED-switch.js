var Gpio = require('onoff').Gpio,
  led = new Gpio(4, 'out'),
  button = new Gpio(25, 'in', 'both');
 
function exit() {
  led.unexport();
  button.unexport();
  process.exit();
}
 
button.watch(function (err, value) {
  if (err) {
    throw err;
  }
 
  led.writeSync(value);
});
 
process.on('SIGINT', exit);

